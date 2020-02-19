import os

def getDir(basePath):
    folders = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(basePath):
        for folder in d:
            folders.append(folder)
    return folders

def getFiles(basePath):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(basePath):
        for files in f:
            folders.append(files)
    return files

basePath = '.'
folders = getDir(basePath)
DIR = []
for folder in folders:
    DIR.append([getFiles(basePath+"/"+folder)])
print(DIR)

# folders = getDir(basePath)





print(getDir("."))