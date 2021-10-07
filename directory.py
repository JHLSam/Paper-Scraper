import os

for root,dirs,files in os.walk(os.getcwd(), topdown=True):
    for files in dirs:
        print(files)
