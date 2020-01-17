import cv2, numpy as np
import math
import time
import random
from matplotlib import pyplot as plt
%matplotlib inline
#import imutils
import qrcode
from pyzbar.pyzbar import decode
from bokeh.plotting import figure
#from bokeh.io import output_notebook, show, push_note


files = ['img1.jpg','img2.jpg','img3.jpg']

imgs = []
for file in files:
    img = cv2.imread(file)
    imgs.append(img)
    
stitchs = cv2.Stitcher_create()
status, dst = stitchs.stitch(imgs)
cv2.imwrite("result.img",dst)
imshow("dst",dst)