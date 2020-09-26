import sys

def oneDictoridentification():
    print('-i and --identify --> Identify Dictor')

def manyDictorsIdentification():
    print('-m and --many --> Identify many Dictors')

def fileDistribution():
    print('-f and --file --> Distribution all dictors into separate files')

def speechRecognition():
    print('-s and --speech --> Speech recognition for each dictor')

if __name__ == '__main__':
    args = sys.argv
    paramFlag = 0
    for param in args:
        if param == '-i' or param == '--identify':
            oneDictoridentification()
            paramFlag = 1
        if param == '-m' or param == '--many':
            manyDictorsIdentification()
            paramFlag = 2
        if param == '-f' or param == '--file':
            fileDistribution()
            paramFlag = 3
        if param == '-s' or param == '--speech':
            speechRecognition()
            paramFlag = 4
    if paramFlag == 0:
        print('no any keys founded')


