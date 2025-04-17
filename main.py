from ROOT import gSystem, Info, TMVA, TCanvas, TGraph;
 
from Train.train import LoadData;
 
def CheckFile(filePath:str) -> None:
    if (gSystem.AccessPathName(filePath)):
        Info("test.py", filePath + " does not exist."); exit();
     
# Load data (for testing).
rootFiles = ["test_signal.root", "test_background.root"];
for rootFile in rootFiles: CheckFile(rootFile);

x, y_true, w = LoadData(rootFiles[0], rootFiles[1]);
 
# Load trained model
modelFile = "model.root";
CheckFile(modelFile);
 
bdt = TMVA.Experimental.RBDT("myBDT", modelFile);
 
# Make prediction
y_pred = bdt.Compute(x);
 
# Compute ROC using sklearn
from sklearn.metrics import roc_curve, auc;

false_positive_rate, true_positive_rate, _ = roc_curve(y_true, y_pred, sample_weight=w);
score = auc(false_positive_rate, true_positive_rate);
 
# Plot ROC
c = TCanvas("roc", "", 600, 600)
g = TGraph(len(false_positive_rate), false_positive_rate, true_positive_rate);

g.SetTitle("AUC = {:.2f}".format(score));
g.SetLineWidth(3);
g.SetLineColor("kRed");
g.Draw("AC");

g.GetXaxis().SetRangeUser(0, 1);
g.GetYaxis().SetRangeUser(0, 1);
g.GetXaxis().SetTitle("False-positive rate");
g.GetYaxis().SetTitle("True-positive rate");

c.Draw();

