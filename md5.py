import glob
import hashlib
import os


Path = "."
filelist = os.listdir(Path)
print(filelist)

with open('iexplore.exe','rb') as getmd5:
    data = getmd5.read()
    gethash= hashlib.md5(data).hexdigest()
    print(gethash)
