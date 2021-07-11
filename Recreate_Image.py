from tkinter.filedialog import test
from Select_Image.Image_Selector import Select_Image
from skimage import io
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

image_file = Select_Image()

image = cv.imread(image_file)

red = image[..., 2]
green = image[..., 1]

mix = cv.merge((green, red))

cv.imshow('Imagem Real', image)
cv.imshow('Imagem Alterada', mix)
cv.waitKey(0)
