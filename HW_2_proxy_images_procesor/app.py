# watcher / observer / listener #####
from os import path, listdir
from time import sleep

extensii_acceptate = [".jpg", ".jpeg", ".png"]


def observe(directory):
    if not path.isdir(directory):
        print("ERROR - directory not found")
        return

    def img(directory):
        imglist = []
        for file in listdir(directory):
            if path.isdir(directory + f"/{file}") is not True:
                if path.splitext(file)[1] in extensii_acceptate:
                    imglist.append(file)
        return imglist

    lastFileList = img(directory)

    while True:
        fileList = img(directory)
        if lastFileList != fileList:
            print(">>> ACHTUNG!!! you have a modification <<<")

        lastFileList = fileList
        sleep(0.5)

observe("./images")
