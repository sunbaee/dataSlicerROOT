# XGBoost has to be imported before ROOT to avoid crashes because of clashing
# std::regexp symbols that are exported by cppyy.
# See also: https://github.com/wlav/cppyy/issues/227
from xgboost import XGBClassifier;
from ROOT import RDataFrame, gSystem, TMVA;

from json import load;
import numpy as np;
 
def LoadData(signalFile, backgroundFile):
    # Read data from ROOT files (training).
    data_sig = RDataFrame("tree", signalFile).AsNumpy();
    data_bkg = RDataFrame("tree", backgroundFile).AsNumpy();

    with open("variables.json", "r") as file: allVariables = load(file);

    # TODO: Convert variables values to float (RVec<Int>).

    # [np.asarray(e) for e in vec1]
    # Convert inputs to format readable by machine learning tools
    x_sig = np.vstack([data_sig[var] for var in allVariables[0]]).T;
    x_bkg = np.vstack([data_bkg[var] for var in allVariables[1]]).T;
    x = np.vstack([x_sig, x_bkg]);
 
    # Create labels
    num_sig = x_sig.shape[0];
    num_bkg = x_bkg.shape[0];

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

