from PIL import Image, ImageEnhance , ImageFilter
import os

path = "./imgs"
pathout = "./editedimgs"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    cleanName = os.path.splitext(filename)[0]
    edit.save(f'{pathout}/{cleanName}_edited.jpg')