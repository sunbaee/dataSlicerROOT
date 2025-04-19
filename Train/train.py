# XGBoost has to be imported before ROOT to avoid crashes because of clashing
# std::regexp symbols that are exported by cppyy.
# See also: https://github.com/wlav/cppyy/issues/227
from xgboost import XGBClassifier;
from ROOT import RDataFrame, gSystem, TMVA;

import numpy as np;
import json;

# Converts ROOT data to list with numpy arrays
def ConvertData(item):
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
    # Read data from ROOT files (training).
    data_sig = RDataFrame("tree", signalFile).AsNumpy();
    data_bkg = RDataFrame("tree", backgroundFile).AsNumpy();

    with open("variables.json", "r") as file: allVariables = json.load(file);

    # Getting variable data from data frame.
    sigData = np.vstack([data_sig[var] for var in allVariables[0]]).T;
    bkgData = np.vstack([data_bkg[var] for var in allVariables[1]]).T;

    # Convert inputs to format readable by machine learning tools
    xSig = ConvertData(sigData);
    xBkg = ConvertData(bkgData);

    print(xSig, "\n\n\n", xBkg);

    #xSig = np.array([x for x in sigData]);
    #xBkg = np.array([x for x in bkgData]);

    x = np.vstack([xSig, xBkg]);

    # Create labels
    num_sig = xSig.shape[0];
    num_bkg = xBkg.shape[0];

    y = np.hstack([np.ones(num_sig), np.zeros(num_bkg)]);
 
    # Compute weights balancing both classes
    num_all = num_sig + num_bkg;
    w = np.hstack([np.ones(num_sig) * num_all / num_sig, np.ones(num_bkg) * num_all / num_bkg]);
 
    return x, y, w;
 
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

