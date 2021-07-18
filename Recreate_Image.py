from tkinter.filedialog import test
from Select_Image.Image_Selector import Blank_Canvas_Creator, Select_Image
from skimage import io
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv


def create_rec(w, h, color=False):
    image = np.full((h, w, 3), 255)
    overlay = image.copy()
    alpha = 0.3
    colors = {'red': (0, 0, 255),
              'blue': (255, 0, 0),
              'green': (0, 255, 0)}
    cv.rectangle(
        image, (0, 0), (w, h), colors[color], - 1)
    # cv.addWeighted(overlay, alpha, image, 1-alpha, 0, image)

    return image


image_file = Select_Image()

image = cv.imread(image_file)

form = image.shape

red = image[..., 2]
green = image[..., 1]
blue = image[..., 0]

blank = np.zeros(image.shape[:2], dtype='uint8')

blank_canvas = Blank_Canvas_Creator(image)
overlay = blank_canvas.copy()

cv.imshow("Blank Canvas", blank_canvas)

# Desse jeito, eu consigo apenas atualizar a janela já existente. Trabalhar com um caso de while True
while True:
    x0 = eval(input('xo= '))
    y0 = eval(input('yo= '))
    w = eval(input('w= '))
    h = eval(input('h= '))
    num = eval(input('num= '))
    color = input('color= ')
    shape_created = create_rec(w, h, color)
    # cv.addWeighted(overlay, alpha, blank_canvas, 1-alpha, 0, blank_canvas)
    blank_canvas[y0:y0+h, x0:x0 +
                 w] = (blank_canvas[y0:y0+h, x0:x0+w]+shape_created)/num
    # overlay = Blank_Canvas_Creator(image)
    cv.imshow("Blank Canvas", blank_canvas)
    cv.waitKey(1)
    # b, g, r = cv.split(image) outro jeito de dividir e separar as cores.

# g_r = cv.merge([blank, green, red])
# b_g = cv.merge([blue, green, blank])
# b_r = cv.merge([blue, blank, red])

# cv.imshow('Imagem Real', image)
# cv.imshow('Verde + Vermelho', g_r)
# cv.imshow('Azul + Verde', b_g)
# cv.imshow('Azul + Vermelho', b_r)
# cv.waitKey(0)
