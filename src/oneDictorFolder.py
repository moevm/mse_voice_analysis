import os as os
import oneDictor as od
import warnings
warnings.filterwarnings("ignore")

def oneDictorFolder(sampleFile, folderPath):
    print('[-iFolder] --> Identify Dictor')
    checkFolder = od.oneDictor()
    arrFiles = []
    resArr = []
    dResTest = {}
    for root, dirs, files in os.walk(folderPath):
        for filename in files:
            arrFiles.append(filename)

    print("Count of files in current folder: ", len(arrFiles) )
    for i, val in enumerate(arrFiles):
        if (len(arrFiles) != i ):
            print("file num = ", i, ", name = ", val)
            checkFolder.oneDictorIdentification(sampleFile, folderPath + arrFiles[i])
            resArr.append(checkFolder.result)
            dResTest[checkFolder.result] = arrFiles[i]
            print()
        else:
            return
    resArr.sort()
    print("The closest sounding speaker: ", dResTest[resArr[0]])
