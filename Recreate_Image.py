from tkinter.filedialog import test
from Select_Image.Image_Selector import Blank_Canvas_Creator, Select_Image
from skimage import io
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

image_file = Select_Image()

image = cv.imread(image_file)

red = image[..., 2]
green = image[..., 1]
blue = image[..., 0]

blank = np.zeros(image.shape[:2], dtype='uint8')

blank_canvas = Blank_Canvas_Creator(image)

cv.imshow("Blank Canvas", blank_canvas)

# b, g, r = cv.split(image) outro jeito de dividir e separar as cores.

g_r = cv.merge([blank, green, red])
b_g = cv.merge([blue, green, blank])
b_r = cv.merge([blue, blank, red])

cv.imshow('Imagem Real', image)
cv.imshow('Verde + Vermelho', g_r)
cv.imshow('Azul + Verde', b_g)
cv.imshow('Azul + Vermelho', b_r)
cv.waitKey(0)
