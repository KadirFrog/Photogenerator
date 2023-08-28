from PIL import Image, ImageEnhance
import random

def rotate(SS, angle):
    x, y = 200, 200
    ssIMG = SS.copy().convert("RGBA")  # Make a copy of the image before rotating
    rgb = ssIMG.getpixel((x, y))
    ssIMG = ssIMG.rotate(angle, expand=True, fillcolor=rgb)
    return ssIMG

def background_p_SS(background, SS, resultname):
    backgroundIMG = background.copy()
    backgroundIMG = backgroundIMG.resize((2000, 1500), Image.BICUBIC)
    ssIMG = SS.copy()
    a = random.randint(-100, 100)
    ssIMG = ssIMG.resize((700 - a, 700 - a), Image.BICUBIC)
    a = random.randint(-500, 500)
    b = random.randint(-250, 250)
    x_position = ((backgroundIMG.width - ssIMG.width) // 2) + a 
    y_position = ((backgroundIMG.height - ssIMG.height) // 2) + b
    position = (x_position, y_position)
    backgroundIMG.paste(ssIMG, position)  # Remove ssIMG from paste() arguments
    backgroundIMG.resize((224, 224), Image.BICUBIC)
    backgroundIMG.save(resultname)
    print("Image successfully saved")


def changeBrightness(SS, value):
    ssIMG = SS.copy()
    brightMacher = ImageEnhance.Brightness(ssIMG)
    modifiedSSIMG = brightMacher.enhance(value)
    return modifiedSSIMG

def cropSS(ssMain, cropValues):
    ssMainIMG = ssMain.copy()
    ss = ssMainIMG.crop(cropValues)
    return ss
