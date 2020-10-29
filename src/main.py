import argparse
import os.path
from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import oneDictor as od
import manyDictors as md
import fileDistr as fd
import speechRec as sr

def fileProcessing(filename):
    # if not (re.search(r'\S+.mp3', filename)):
    #     print("Only mp3 format supported")
    #     exit(-1)
    if not (os.path.exists(filename)):
        print("\033[31m\033[1m {}".format("No such file"))
        exit(-1)
    print("Processing file")


def keysProcessing(keys):
    if keys['identify']:
        od.oneDictorIdentification(file, file2)
    if keys['many']:
        a = md.many_dictors()
        wav = preprocess_wav(Path("../" + varArgs['path'], varArgs['file']))
        c, d = a.manyDictorsIdentification(wav, True);
        # print("count of dictors = ", c)
        print("\033[33m\033[1m {}".format("Count of dictors ="), c)
    # if keys['distribution']:
    #     fd.fileDistribution()
    # if keys['speech']:
    #     sr.speechRecognition()

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', default="res/", help="select folder with speakers")
parser.add_argument('-f', '--file', help='select speaker identifier')
parser.add_argument('-f2', '--file2', default="", help='select second speaker identifier')
parser.add_argument('-i', '--identify', action='store_true', help='Function which can identify dictor')
parser.add_argument('-m', '--many', action='store_true', help='Function which can identify many dictors')
# parser.add_argument('-d', '--distribution', action='store_true', help='Function which can distribute all dictors into '
#                                                                       'separate files')
# parser.add_argument('-s', '--speech', action='store_true', help='Function which provide speech recognition for each '
#                                                                 'dictor')
args = parser.parse_args()
print(args)

varArgs = vars(args)
file = "../" + varArgs['path'] + '/' + varArgs['file']
file2 = "../" + varArgs['path'] + '/' + varArgs['file2']
try:
    fileProcessing(file)
    keysProcessing(varArgs)
except FileNotFoundError:
    print("No such file")
    exit(-1)
except EOFError:
    print("Invalid or broken file")
    exit(-1)