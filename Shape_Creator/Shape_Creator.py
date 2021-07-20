from tkinter import image_names
import numpy as np
import cv2 as cv


def create_circle(cx, cy, r, color):
    image = np.full((2*r, 2*r, 3), 255)
    colors = {'red': (1, 1, 255),
              'blue': (255, 1, 1),
              'green': (1, 255, 1)}
    cv.circle(image, (cx, cy), r, colors[color], -1)
    return image


def create_ellipse(cx, cy, rx, ry, angle, color):
    image = np.full((2*ry, 2*rx, 3), 255)
    colors = {'red': (1, 1, 255),
              'blue': (255, 1, 1),
              'green': (1, 255, 1)}
    cv.ellipse(image, (cx, cy), (rx, ry), angle, 0, 360, colors[color], -1)
    return image


def create_rec(w, h, color):
    image = np.full((h, w, 3), 255)
    colors = {'red': (1, 1, 255),
              'blue': (255, 1, 1),
              'green': (1, 255, 1)}
    cv.rectangle(
        image, (0, 0), (w, h), colors[color], - 1)
    return image


def create_triangle(b, h, color):
    image = np.full((h, b, 3), 255)
    # Continuar pensando como fazer e quais inputs usar.
    # https://stackoverflow.com/questions/51875114/triangle-filling-in-opencv
    return image


def draw_shape(shape_info, color, w=None, h=None, r=None, cx=None, cy=None, angle=0):
    match shape_info:
        case 'rectangle':
            shape = create_rec(w, h, color)
        case 'ellipse':
            shape = create_ellipse(cx, cy, w, h, angle, color)
        case 'circle':
            shape = create_circle(cx, cy, r)
        case 'triangle':
            print('not ready, yet')
            shape = None
    return shape
