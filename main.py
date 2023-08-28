from PIL import Image, ImageEnhance
import random
import os
from func import *
from zipall import *

folder_path = "images/backgrounds"
ss = "images/ss.png"

count1 = 3
fp1 = "generated/"
a = "generated/-1/"

if not os.path.exists(a):
    os.makedirs(a)
count = 0
for background in os.listdir(folder_path):
    way = os.path.join(a, str(count) + ".jpg")
    get = os.path.join(folder_path, background)
    get = Image.open(get)
    get.save(way)
    count += 1


for x in range(count1):
    ssIMG = Image.open(ss)
    count2 = 0
    width, height = ssIMG.size  
    onewidth = width // count1 
    cutwidth1 = x * onewidth  
    cutwidth2 = (x + 1) * onewidth  
    upper = 0  
    cutbox = (cutwidth1, upper, cutwidth2, height)  
    ssIMG = cropSS(ssIMG, cutbox)
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            img = Image.open(os.path.join(folder_path, filename))
            b = random.uniform(0.7, 1.5)
            ssIMG_resized = ssIMG.resize((2000, 1500), Image.BICUBIC)
            ssIMG_brightened = changeBrightness(ssIMG_resized, b)
            r = random.randint(-7, 7)
            ssIMG_rotated = rotate(ssIMG_brightened, r)
            saveloc = os.path.join(fp1, str(x))
            os.makedirs(saveloc, exist_ok=True)
            rn = os.path.join(saveloc, f"{count2}.jpg")
            background_p_SS(img, ssIMG_rotated, rn)
            count2 += 1

zipGenerated(fp1, "generated.zip")