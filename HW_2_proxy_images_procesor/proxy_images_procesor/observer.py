from os import path, listdir
from time import sleep
from transformer_proxy import TransformerProxy


extensii_acceptate = [".jpg", ".jpeg", ".png"]


class Observer:
    def __init__(self, original_dir, transformed_path):
        self.original = original_dir
        self.transformer = TransformerProxy(self.original, transformed_path)

    def observe(self):

        def img(orig_dir):
            imglist = []
            for file in listdir(orig_dir):
                if path.isdir(orig_dir + f"/{file}") is not True:
                    if path.splitext(file)[1] in extensii_acceptate:
                        imglist.append(file)
            return imglist

        lastFileList = []

        while True:
            fileList = img(self.original)
            if lastFileList != fileList:
                print(">>> ACHTUNG!!! you have a modification <<<")


                for fileim in fileList:
                    print(f"<<<processed image --- {fileim}")
                    self.transformer.transform(fileim)

            lastFileList = fileList
            sleep(0.5)
