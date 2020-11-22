class TransformerProxy:

    def __init__(self, original_path, transformed_path):
        self.transformed_path = transformed_path
        self.original_path = original_path

        self.real_transformer = None

    def transform(self, file):
        if self.real_transformer is None:
            from image_transformer import ImageTrasformer

            self.real_transformer = ImageTrasformer(self.original_path, self.transformed_path)
        self.real_transformer.transform(file)
        # print("Fake transformer!!!")
