from PIL import Image, ImageEnhance

def rotate(SS, angle):
    ssIMG = SS.copy()  # Make a copy of the image before rotating
    ssIMG = ssIMG.rotate(angle, expand=True)
    return ssIMG

def background_p_SS(background, SS, resultname):
    backgroundIMG = background.copy()
    backgroundIMG = backgroundIMG.resize((2000, 1500), Image.BICUBIC)
    ssIMG = SS.copy()
    ssIMG = ssIMG.resize((700, 700), Image.BICUBIC)
    x_position = (backgroundIMG.width - ssIMG.width) // 2
    y_position = (backgroundIMG.height - ssIMG.height) // 2
    position = (x_position, y_position)
    backgroundIMG.paste(ssIMG, position)  # Remove ssIMG from paste() arguments
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
