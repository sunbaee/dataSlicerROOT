from sys import argv;
from json import dump;

from ROOT import RDataFrame, gSystem, Info, std;
 
def FilterEvents(dataFrame):
    """
    Reduce initial dataset to only events which shall be used for training
    """
    return dataFrame;#.Filter("nElectron>=2 && nMuon>=2", "At least two electrons and two muons.");

def SetVariables(dataFrame, label):
    "Sets name of the variables"

    variables = [];
    for columnName in dataFrame.GetColumnNames():
        defName = columnName.replace('.', '_');

        varName = f"{label}_{defName}";
        variables.append(varName);

    return variables;

def DefineVariables(dataFrame, variables):
    """
    Define the variables which shall be used for training.
    """
    for i, columnName in enumerate(dataFrame.GetColumnNames()):
        dataFrame = dataFrame.Define(variables[i], f"{columnName}");
        
    return dataFrame;
 

if __name__ == "__main__":
    # Loading dictionaries.
    gSystem.Load("libdict.so")

    if (len(argv) < 3): print("Signal and background root files required."); exit(1);

    # Initializing variables.
    allVariables = []; 
    for filePath, label in [[argv[1], "signal"] , [argv[2], "background"]]:
        if (gSystem.AccessPathName(filePath)): Info("dataPreparation.py", filePath + " does not exist."); exit();

        print(">>> Extract the training and testing events for {} from the {} dataset.".format(label, filePath));
 
        # Load dataset, filter the required events and define the training variables
        dataFrame = RDataFrame("tree", filePath);
        dataFrame = FilterEvents(dataFrame);

        curVariables = SetVariables(dataFrame, label);
        allVariables.append(curVariables);

        dataFrame = DefineVariables(dataFrame, curVariables);
 
        # Book cutflow report
        report = dataFrame.Report();
 
        # Split dataset by event number for training and testing
        columns = std.vector["string"](curVariables); 

        dataFrame.Filter("rdfentry_ % 2 == 0").Snapshot("tree", f"train_{label}.root", columns);
        dataFrame.Filter("rdfentry_ % 2 == 1").Snapshot("tree", f"test_{label}.root",  columns);
 
        # Print cutflow report
        report.Print();

    with open("variables.json", "w") as file: dump(allVariables, file);

    print(">>> Data preparation was successful.");
