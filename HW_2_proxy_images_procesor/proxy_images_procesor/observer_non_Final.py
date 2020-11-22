from os import path, listdir, mkdir
from time import sleep

extensii_acceptate = [".jpg", ".jpeg", ".png"]


class Observer:
    def __init__(self, directory, transformer):
        self.directory = directory
        self.transform = transformer

    def set_dir(self, name_dir):
        fin_dir = self.directory + f"/{name_dir}"
        if not path.isdir(fin_dir):
            mkdir(fin_dir)
        return fin_dir

    def observe(self):
        name = "original"

        def img():
            imglist = []
            for file in listdir(self.set_dir(name)):
                if path.isdir(self.set_dir(name) + f"/{file}") is not True:
                    if path.splitext(file)[1] in extensii_acceptate:
                        imglist.append(file)
            return imglist

        lastFileList = []

        while True:
            fileList = img()
            if lastFileList != fileList:
                print(">>> You have a modification <<<")
                for fileim in fileList:
                    print(f"<<<<processed image --- {fileim}")
                    self.transform.transform(fileim)

            lastFileList = fileList
            sleep(0.5)
