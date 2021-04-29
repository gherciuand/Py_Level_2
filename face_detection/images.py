# from tkinter import Tk, filedialog
import os
import urllib.request
from pathlib import Path

# root = Tk().withdraw()
# IMAGE_BASE_FOLDER = filedialog.askdirectory()
IMAGE_BASE_FOLDER = './orig_img_dir'


def saveImage(url, name):
    if not os.path.exists(f'{IMAGE_BASE_FOLDER}/{name}'):
        os.mkdir(f'{IMAGE_BASE_FOLDER}/{name}')                             # creating a new folder if it does not exist
    if len(list(Path(f'{IMAGE_BASE_FOLDER}/{name}').glob('*.jpg'))) == 0:   # check if folder contain image file
        urllib.request.urlretrieve(url, f'{IMAGE_BASE_FOLDER}/{name}/0000.jpg')  # save first image
    else:
        last_img = list(Path(f'{IMAGE_BASE_FOLDER}/{name}').glob('*.jpg'))[-1].stem
        next_img = (last_img.join(['{0:04}'.format((int(last_img) + 1))]))  #set name for the next image
        urllib.request.urlretrieve(url, f'{IMAGE_BASE_FOLDER}/{name}/{next_img}.jpg') # save next image
