from os import listdir
from os.path import isfile, join
import pickle
mypath = "C:/Users/Cabbageman/PycharmProjects/NitrogenGame/music-ogg"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

library = []

for f in onlyfiles:
    if f[-4:] == ".ogg":
        artist, album, track = f.strip(".ogg").split(" - ")
        with open(f, mode='rb') as fd:
            library.append([artist, album, track, fd.read()])

with open("music.pickle", mode='wb') as fd:
    pickle.dump(library, fd)
