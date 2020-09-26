import argparse
import re
import os.path

def oneDictorIdentification():
    print('-i --> Identify Dictor')


def manyDictorsIdentification():
    print('-m --> Identify many Dictors')


def fileDistribution():
    print('-f --> Distribution all dictors into separate files')


def speechRecognition():
    print('-s --> Speech recognition for each dictor')


def fileProcessing(filename):
    if not (re.search(r'\S+.mp3', filename)):
        print("Only mp3 format supported")
        exit(-1)
    if not (os.path.exists(filename)):
        print("No such file")
        exit(-1)
    print('Processing file')
    '''
    #Play mp3 file
        import pyglet
        song = pyglet.media.load(filename)
        song.play()
        pyglet.app.run()
    '''


def keysProcessing(keys):
    if keys['identify']:
        oneDictorIdentification()
    if keys['many']:
        manyDictorsIdentification()
    if keys['distribution']:
        fileDistribution()
    if keys['speech']:
        speechRecognition()


parser = argparse.ArgumentParser()
parser.add_argument('file', help='mp3 file')
parser.add_argument('-i', '--identify', action='store_true', help='Function which can identify dictor')
parser.add_argument('-m', '--many', action='store_true', help='Function which can identify many dictors')
parser.add_argument('-d', '--distribution', action='store_true', help='Function which can distribute all dictors into '
                                                                      'separate files')
parser.add_argument('-s', '--speech', action='store_true', help='Function which provide speech recognition for each '
                                                                'dictor')
args = parser.parse_args()
print(args)

varArgs = vars(args)
file = varArgs['file']
try:
    fileProcessing(file)
    keysProcessing(varArgs)
except FileNotFoundError:
    print("No such file")
    exit(-1)
except EOFError:
    print("Invalid or broken file")
    exit(-1)
