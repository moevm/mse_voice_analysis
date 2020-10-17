import argparse
import re
import os.path

import oneDictor as od
import manyDictors as md
import fileDistr as fd
import speechRec as sr



def fileProcessing(filename):
    if not (re.search(r'\S+.mp3', filename)):
        print("Only mp3 format supported")
        exit(-1)
    if not (os.path.exists(filename)):
        print("No such file")
        exit(-1)
    print('Processing file')
    # Play mp3 file
    song = pyglet.media.load(filename)
    song.play()
    pyglet.app.run()


def keysProcessing(keys):
    if keys['identify']:
        od.oneDictorIdentification()
    if keys['many']:
        md.manyDictorsIdentification()
    if keys['distribution']:
        fd.fileDistribution()
    if keys['speech']:
        sr.speechRecognition()



parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', default="res/", help="select folder with speakers")
parser.add_argument('file', help='select speaker identifier')
parser.add_argument('-i', '--identify', action='store_true', help='Function which can identify dictor')
parser.add_argument('-m', '--many', action='store_true', help='Function which can identify many dictors')
parser.add_argument('-d', '--distribution', action='store_true', help='Function which can distribute all dictors into '
                                                                      'separate files')
parser.add_argument('-s', '--speech', action='store_true', help='Function which provide speech recognition for each '
                                                                'dictor')
args = parser.parse_args()
print(args)

varArgs = vars(args)
file = "../" + varArgs['path'] + '/' + varArgs['file']
try:
    fileProcessing(file)
    keysProcessing(varArgs)
except FileNotFoundError:
    print("No such file")
    exit(-1)
except EOFError:
    print("Invalid or broken file")
    exit(-1)