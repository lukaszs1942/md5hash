import hashlib
import os


Path = "C://Users//m121374//PycharmProjects//gogole//venv"
filelist = os.listdir(Path)
print(filelist)

for element in filelist:
    fullpath = Path+'//' +element
    if not os.path.isdir(fullpath):
        if element.endswith(".exe"):
            try:
                with open(fullpath,'rb') as getmd5:
                    data = getmd5.read()
                    gethash= hashlib.md5(data).hexdigest()
                    print(gethash)
            except:
                pass
