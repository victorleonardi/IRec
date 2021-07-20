from tkinter.filedialog import test
from Select_Image.Image_Selector import Blank_Canvas_Creator, Select_Image
from skimage import io
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from Shape_Creator.Shape_Creator import *

image_file = Select_Image()

image = cv.imread(image_file)

# red = image[..., 2]
# green = image[..., 1]
# blue = image[..., 0]

# blank = np.zeros(image.shape[:2], dtype='uint8')

blank_canvas = Blank_Canvas_Creator(image)
overlay = blank_canvas.copy()

cv.imshow("Blank Canvas", blank_canvas)

while True:
    x0 = eval(input('xo= '))
    y0 = eval(input('yo= '))
    w = eval(input('w= '))
    h = eval(input('h= '))
    num = eval(input('num= '))
    color = input('color= ')
    shape_created = create_rec(w, h, color)
    blank_canvas[y0:y0+h, x0:x0 +
                 w] = (blank_canvas[y0:y0+h, x0:x0+w]+shape_created)/num
    cv.imshow("Blank Canvas", blank_canvas)
    cv.waitKey(1)
