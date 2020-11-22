from PIL import Image


class ImageTrasformer:

    def __init__(self, original_path, transformed_path):
        self.transformed_path = transformed_path
        self.original_path = original_path

    def transform(self, file):
        im = Image.open(self.original_path + f"/{file}")
        im.thumbnail((100, 100))
        im.save(self.transformed_path + f"/{file}", "JPEG")
