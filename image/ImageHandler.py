from PIL import Image

class ImageHandler():

    def __init__(self, original_img):
        self.original_img = Image.open(original_img)

    def load(self):
        return self.original_img
    
    def change_size(self, size):
        self.original_img.thumbnail(size)

    def save_new(self, image2):
        self.original_img.save(image2)