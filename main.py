from PIL import Image, ImageFilter, ImageDraw, ImageFont
from image.ImageHandler import ImageHandler
from image.ImageProcessor import ImageProcessor

def main():

    image = ImageHandler('image.jpg')
    image.change_size((200, 200))
    
    rezult_img  = ImageProcessor(image)
    rezult_img.add_filter()
    rezult_img.add_text((50,100), "Вариант 3", size = 15, color = 'black')

    rezult_img = image
    image.save_new('image2.jpg')

main()