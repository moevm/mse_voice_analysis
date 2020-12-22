import argparse
import os.path
from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import oneDictor as oned
import manyDictors as md
import oneDictorFolder as odf
import re
import warnings
warnings.filterwarnings("ignore")

onlyOneDictor = True;

def fileProcessing(filename):
    if not (re.search(r'\S+.mp3', filename)  or (re.search(r'\S+.wav', filename)) or (re.search(r'\S+.ogg', filename)) ):
        print("Only mp3, wav and ogg formats sound supported")
        exit(-1)
    if not (os.path.exists(filename)):
        print("No such file")
        exit(-1)
    print("Processing file")


def keysProcessing(keys):
    mFirst = True

    if keys['many']:        # -m
        onlyOneDictor = True
        mFirst = False
        identification = md.SeveralSpeakers()
        path = Path(varArgs['path'], varArgs['file'])
        identification.several_speakers_identification(path, recognition=True, export=True, min_duration=1)
        res_file = open(str(path) + str('.txt'))
        if(identification.speakers_number != 1):
            onlyOneDictor = False

        if(varArgs['file2'] != ""):
            identification2 = md.SeveralSpeakers()
            path = Path(varArgs['path'], varArgs['file2'])
            identification2.several_speakers_identification(path, recognition=True, export=True, min_duration=1)
            res_file = open(str(path) + str('.txt'))
            if (identification2.speakers_number != 1):
                onlyOneDictor = False

    if keys['identify']:    # -i
        od = oned.oneDictor()
        if(mFirst):
            identification1 = md.SeveralSpeakers()
            path = Path(varArgs['path'], varArgs['file'])
            identification1.several_speakers_identification(path, recognition=True, export=True, min_duration=1)

            identification2 = md.SeveralSpeakers()
            path = Path(varArgs['path'], varArgs['file2'])
            identification2.several_speakers_identification(path, recognition=True, export=True, min_duration=1)
            if(identification1.speakers_number == 1 and identification2.speakers_number == 1): #один диктор в файле
                od.oneDictorIdentification(file, file2)  # контрольные образцы
            else:
                print("[-i error] Several dictors on audio, you should use [-m] to recognize multiple speakers")

        else: # -m работал уже
            if(onlyOneDictor):
                od.oneDictorIdentification(file, file2)
            else:
                print("[-i error] Several dictors on audio, [-i] can compare only 2 single speakers")

    if keys['pathMany']:
        odf.oneDictorFolder(file, folderPath)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', default="res/", help="select folder with speakers")
parser.add_argument('-f', '--file', help='select speaker identifier')


parser.add_argument('-i', '--identify', action='store_true', help='Function can identify and compare 2 dictors')
parser.add_argument('-m', '--many', action='store_true', help='Function can identify many dictors, distribute all dictors into separate and create text file')
parser.add_argument('-iSeveral', '--identifySeveral', action='store_true', help='Function can found the closest sounding speaker in folder')
parser.add_argument('-pMany', '--pathMany', default="", help='select folder with speaker for [-iSeveral]')
parser.add_argument('-f2', '--file2', default="", help='select second speaker identifier')
args = parser.parse_args()
print(args)

varArgs = vars(args)
path = varArgs['path'] + '/'
file = varArgs['path'] + '/' + varArgs['file']
file2 = varArgs['path'] + '/' + varArgs['file2']
folderPath = varArgs['pathMany'] + '/'

try:
    fileProcessing(file)
    keysProcessing(varArgs)
except FileNotFoundError:
    print("No such file")
    exit(-1)
except EOFError:
    print("Invalid or broken file")
    exit(-1)