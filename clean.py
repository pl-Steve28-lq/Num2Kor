import os, shutil

def cleanPycache():
    removes = []
    for root, dirs, files in os.walk('./'):
        for i in dirs:
            if 'pycache' in i:
               removes.append(root + i)
    for i in removes:
       shutil.rmtree(i)

def removeBuilds():
    removes = ['build', 'dist', 'Num2Kor.egg-info']
    for i in removes:
        if os.path.exists(f"./{i}"):
            shutil.rmtree(f'./{i}')

cleanPycache()
removeBuilds()
