from PIL import Image, ImageFilter, ImageDraw, ImageFont
from image.ImageHandler import ImageHandler

class ImageProcessor():

    def __init__(self, image_handler):
        self.image_handler = image_handler

    def add_filter(self):
        self.image_handler.original_img = self.image_handler.original_img.filter(ImageFilter.CONTOUR)

    def add_text(self, position, text, size, color):
        draw_text = ImageDraw.Draw(self.image_handler.original_img)
        font = ImageFont.truetype('arial.ttf', size)
        draw_text.text(position, text, font= font, fill = color)

