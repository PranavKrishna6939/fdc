import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import glob
import os
from pathlib import Path
import numpy as np
from PIL import Image

data = pd.read_csv(r'C:\Users\Kumar\Desktop\Desktop\Python\icg-freshers-data-science-competition\Dataset\Train\Grid_labels.csv')

def cropBoard(image):
  crop = image[62:425, 148:511]
  return crop

def transformImage(crop):
  kernel =  np.ones((2,2),np.uint8)
  img_g =  cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
  ret,thresh1 = cv2.threshold(img_g,127,255,cv2.THRESH_BINARY)
  thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
  return thresh1

def downImageZero(img, j):
  image = Image.fromarray(img, mode="L")
  image.save(rf"C:\Users\Kumar\Desktop\Desktop\Python\icg-freshers-data-science-competition\Zero_Template\Zero{j}.png")

def downImageCross(img, i):
  image = Image.fromarray(img, mode="L")
  image.save(rf"C:\Users\Kumar\Desktop\Desktop\Python\icg-freshers-data-science-competition\Cross_Template\Cross{i}.png")

i = 0
j = 0

for y in range (0, 25):
    id = data.loc[y, 'ID']
    imgtest = cv2.imread(rf'C:\Users\Kumar\Desktop\Desktop\Python\icg-freshers-data-science-competition\Dataset\Train\Grids\{id}.png')
    #plt.imshow(imgtest)
    print(f'{y} {id}')
    crop = cropBoard(imgtest)
    threshtest = transformImage(crop)
    pos1 = threshtest[0:115,0:115]
    pos2 = threshtest[0:115,121:236]
    pos3 = threshtest[0:115,245:360]
    pos4 = threshtest[122:237,0:115]
    pos5 = threshtest[122:237,121:236]
    pos6 = threshtest[122:237,245:360]
    pos7 = threshtest[245:360,0:115]
    pos8 = threshtest[245:360,121:236]
    pos9 = threshtest[245:360,245:360]
    pos = []
    pos.append(pos1)
    pos.append(pos2)
    pos.append(pos3)
    pos.append(pos4)
    pos.append(pos5)
    pos.append(pos6)
    pos.append(pos7)
    pos.append(pos8)
    pos.append(pos9)
    symbol = []
    symbol.append(data.loc[y, 'POS_1'])
    symbol.append(data.loc[y, 'POS_2'])
    symbol.append(data.loc[y, 'POS_3'])
    symbol.append(data.loc[y, 'POS_4'])
    symbol.append(data.loc[y, 'POS_5'])
    symbol.append(data.loc[y, 'POS_6'])
    symbol.append(data.loc[y, 'POS_7'])
    symbol.append(data.loc[y, 'POS_8'])
    symbol.append(data.loc[y, 'POS_9'])
    for x in range (0, 9):
      if (symbol[x] == 1):
        downImageZero(pos[x], j)
        j = j + 1
      elif (symbol[x] == 0):
        downImageCross(pos[x], i)
        i = i + 1