import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import glob
import os
from pathlib import Path

data = pd.read_csv(r'\Dataset\Sample_submission.csv')


def cropBoard(image):
  crop = image[62:425, 148:511]
  return crop

def transformImage(crop):
  kernel =  np.ones((2,2),np.uint8)
  img_g =  cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
  ret,thresh1 = cv2.threshold(img_g,127,255,cv2.THRESH_BINARY)
  thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
  return thresh1

def isEmpty(cell_image):
  mean, std = cv2.meanStdDev(cell_image)
  if (std < 10):
    return True
  else:
    return False
  
def solution(imgtest, y, data):
  threshtest = cropBoard(imgtest)
  #threshtest = transformImage(crop)
  pos1 = threshtest[0:115,0:115]
  pos2 = threshtest[0:115,121:236]
  pos3 = threshtest[0:115,245:360]
  pos4 = threshtest[122:237,0:115]
  pos5 = threshtest[122:237,121:236]
  pos6 = threshtest[122:237,245:360]
  pos7 = threshtest[245:360,0:115]
  pos8 = threshtest[245:360,121:236]
  pos9 = threshtest[245:360,245:360]
  postest1 = pos1
  postest2 = pos2
  postest3 = pos3
  postest4 = pos4
  postest5 = pos5
  postest6 = pos6
  postest7 = pos7
  postest8 = pos8
  postest9 = pos9
  symbol1 = detect_symbol(postest1)
  symbol2 = detect_symbol(postest2)
  symbol3 = detect_symbol(postest3)
  symbol4 = detect_symbol(postest4)
  symbol5 = detect_symbol(postest5)
  symbol6 = detect_symbol(postest6)
  symbol7 = detect_symbol(postest7)
  symbol8 = detect_symbol(postest8)
  symbol9 = detect_symbol(postest9)
  data.loc[y, 'POS_1'] = symbol1
  data.loc[y, 'POS_2'] = symbol2
  data.loc[y, 'POS_3'] = symbol3
  data.loc[y, 'POS_4'] = symbol4
  data.loc[y, 'POS_5'] = symbol5
  data.loc[y, 'POS_6'] = symbol6
  data.loc[y, 'POS_7'] = symbol7
  data.loc[y, 'POS_8'] = symbol8
  data.loc[y, 'POS_9'] = symbol9
  print(y)

def detect_symbol(cell_image):
  image_dir_o = r'\Zero_Template'
  image_files_o = glob.glob(image_dir_o + '/*.png')
  corr_o = 1000000000000000

  img = transformImage(cell_image)
  img_float = img.astype(np.float32)

  for x in image_files_o:
    image = cv2.imread(x)
    temp_o = transformImage(image)
    templ_o_float = temp_o.astype(np.float32)
    diff_o = img_float-templ_o_float
    norm_o = np.mean(sum(abs(diff_o)))


    if (norm_o < corr_o):
      corr_o = norm_o


  image_dir_x = r'\Cross_Template'
  image_files_x = glob.glob(image_dir_x + '/*.png')
  corr_x = 1000000000000000

  for x in image_files_x:
    image = cv2.imread(x)
    temp_x = transformImage(image)
    templ_x_float = temp_x.astype(np.float32)
    diff_x = img_float-templ_x_float
    norm_x = np.mean(sum(abs(diff_x)))


    if (norm_x < corr_x):
      corr_x = norm_x


  if (isEmpty(img)):
      return 2
  elif (corr_o < corr_x):
      return 1
  else:
      return 0
  
image_dir = r'\Dataset\Test'
image_files = glob.glob(image_dir + '/*.png')

for x in image_files:
  image = cv2.imread(x)
  index = int(Path(os.path.basename(x)).stem)
  for x in range (0, 4495):
    if (index == data.loc[x, 'ID']):
      y = x
  solution(image, y, data)
  
data.to_csv("pranav_solution_V3.csv", index=False)
print(data.head(20))
