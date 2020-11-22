from os import mkdir, path
from observer import Observer
from tkinter import filedialog as fd

directory = fd.askdirectory()
print(f">>Mapa de lucru este setata cu calea:\n {directory}")
original_path = directory + "/original"
transformed_path = directory + "/processed"

if not path.isdir(original_path):
    mkdir(original_path)
if not path.isdir(transformed_path):
    mkdir(transformed_path)

obs = Observer(original_path, transformed_path)
obs.observe()
