# XGBoost has to be imported before ROOT to avoid crashes because of clashing
# std::regexp symbols that are exported by cppyy.
# See also: https://github.com/wlav/cppyy/issues/227
from sklearn.preprocessing import OneHotEncoder;
from xgboost import XGBClassifier, DMatrix;

from ROOT import RDataFrame, gSystem, TMVA;

import pandas as pd;
import numpy as np;
import json;

# Converts ROOT data to list with numpy arrays
def ConvertData(item):
    # TODO: Make this function faster (np arrays)
    # TODO: Remove list with no information (*list of list of lists)

    # Exits if current item is a real number.
    if ( type(item) == float or type(item) == int ): return item;

    if ( type(item) == list or type(item) == np.ndarray ): 
        newItem = [];
        for i,_ in enumerate(item): newItem.append(ConvertData(item[i]));
        
        # Returns lists or arrays inside item.
        return newItem;

    # Converts ROOT Vectors to numpy arrays by iterating them and returns.

    # Finding type of vector
    typeStr = type(item).__cpp_name__;
    vecTypeIdx = typeStr.find('<');

    vecType = typeStr[vecTypeIdx + 1 : -1];

    if (vecType == "float" or vecType == "int"): return np.asarray([x for x in item]);

    # Vector Type is a Lorentz Vector.
    return np.asarray([np.asarray([x.Px(), x.Py(), x.Pz(), x.E()]) for x in item]);

# Loads data from root files
def LoadData(signalFile, backgroundFile):
    print(">>> Reading data...");

    with open("variables.json", "r") as file: allVariables = json.load(file);

    # Read data from ROOT files (training).
    rootDataSig = RDataFrame("tree", signalFile).AsNumpy();
    rootDataBkg = RDataFrame("tree", backgroundFile).AsNumpy();

    print(">>> Data loaded.");

    # Getting variable data from data frame.
    sigData = np.vstack([rootDataSig[var] for var in allVariables[0]]).T;
    bkgData = np.vstack([rootDataBkg[var] for var in allVariables[1]]).T;

    # Convert inputs to format readable by machine learning tools
    sigRaw, bkgRaw = ConvertData(sigData), ConvertData(bkgData);
    print(">>> Converted");

    print(sigRaw, "\n\n", bkgRaw);

    idxArr = range(len(allVariables));

    # Stacking each variable separately
    xValues = [np.vstack([sigRaw[idx], bkgRaw[idx]]) for idx in idxArr];

    # Create labels for each variable 
    numSigs = [sigRaw[idx].shape[0] for idx in idxArr];
    numBkgs = [bkgRaw[idx].shape[0] for idx in idxArr];

    yValues = [ np.hstack([np.ones(numSigs[idx]), np.zeros(numBkgs[idx])]) for idx in idxArr];
 
    # Compute weights balancing both classes for each variable
    numAll = numSigs + numBkgs;
    wValues = [np.hstack([ np.ones(numSigs[idx]) * numAll[idx] / numSigs[idx] , 
                     np.ones(numBkgs[idx]) * numAll[idx] / numBkgs[idx] ]) for idx in idxArr];
 
    return xValues, yValues, wValues;
 
if __name__ == "__main__":
    # Loading dictionaries.
    gSystem.Load("libdict.so");

    # Load data.
    x, y, w = LoadData("train_signal.root", "train_background.root");
 
    # Fit xgboost model
    bdt = XGBClassifier(max_depth=3, n_estimators=500);
    bdt.fit(x, y, sample_weight=w);
 
    # Save model in TMVA format
    print("Training done on ", x.shape[0], "events. Saving model in model.root");
    TMVA.Experimental.SaveXGBoost(bdt, "myBDT", "model.root", num_inputs=x.shape[1]);

