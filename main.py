from PIL import Image, ImageEnhance
import random
import os
from func import *

# Function definitions here...

folder_path = "images/backgrounds"
ss = "ss.png"
ssIMG = Image.open(ss)

count1 = 3
fp1 = "generated/"

for x in range(count1):
    count2 = 0
for x in range(count1):
    count2 = 0
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            img = Image.open(os.path.join(folder_path, filename))
            b = random.uniform(0.7, 1.5)
            ssIMG_resized = ssIMG.resize((2000, 1500), Image.BICUBIC)
            ssIMG_brightened = changeBrightness(ssIMG_resized, b)
            r = random.randint(0, 360)
            ssIMG_rotated = rotate(ssIMG_brightened, r)
            saveloc = os.path.join(fp1, str(x))
            os.makedirs(saveloc, exist_ok=True)
            rn = os.path.join(saveloc, f"{count2}.jpg")
            background_p_SS(img, ssIMG_rotated, rn)
            count2 += 1

