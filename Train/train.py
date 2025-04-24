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

def Flatten(listSig, listBkg):
    numVariables = len(listSig);
    if (numVariables != len(listBkg)): return None;

    oldLists = [listSig, listBkg]
    newLists = [[], []];
    for i,_ in enumerate(listSig):
        curType = type(listSig[i]);
        if (curType != type(listBkg[i])): return None;
        
        if (curType != np.ndarray): 
            for j, curList in enumerate(newLists): curList.append(oldLists[j][i]);
            continue;

        maxLength = max(len(listSig[i]), len(listBkg[i]));
        for j, curList in enumerate(newLists):
            for element in oldLists[j][i][: maxLength - 1]: 
                # TODO: Correction: it can have arrays inside arrays
                curList.append(element);
    
    return np.asarray(newLists[0]), np.asarray(newLists[1]);

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
    xSigRaw, xBkgRaw = ConvertData(sigData), ConvertData(bkgData);

    flatDatas = Flatten(xSigRaw, xBkgRaw);
    if (not flatDatas): return None; 
    xSig, xBkg = flatDatas;

    print(xSig, "\n\n", xBkg);

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
    trainData = LoadData("train_signal.root", "train_background.root");
    if (not trainData): print("An error occurred."); exit();

    x, y, w = trainData;
 
    # Fit xgboost model
    bdt = XGBClassifier(max_depth=3, n_estimators=500);
    bdt.fit(x, y, sample_weight=w);
 
    # Save model in TMVA format
    print("Training done on ", x.shape[0], "events. Saving model in model.root");
    TMVA.Experimental.SaveXGBoost(bdt, "myBDT", "model.root", num_inputs=x.shape[1]);

