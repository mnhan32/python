import os

def buildIntermiatePath(path):
    '''
        description:
            make all intermediate folders
            
        param :
          path  (str) : full path in string
    '''
    dirPath = os.path.split(path)[0]
    sw = 1
    missingFolder = []
    while sw:
        if os.path.isdir(dirPath):
            sw = 0
        else:
            missingFolder.append(dirPath)
            tmpSplit = os.path.split( dirPath )            
            dirPath = tmpSplit[0]
            
    if missingFolder:
        for m in missingFolder[::-1]:
            try:
                os.mkdir(m)
            except:
                raise UserWarning('failed create folder %s'%m)
                break
