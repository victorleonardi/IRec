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
    image = np.full((2*rx, 2*ry, 3), 255)
    colors = {'red': (1, 1, 255),
              'blue': (255, 1, 1),
              'green': (1, 255, 1)}
    cv.ellipse(image, (cx, cy), (rx, ry), angle, 0, 360, colors[color], -1)


def create_rec(w, h, color=False):
    image = np.full((h, w, 3), 255)
    colors = {'red': (1, 1, 255),
              'blue': (255, 1, 1),
              'green': (1, 255, 1)}
    cv.rectangle(
        image, (0, 0), (w, h), colors[color], - 1)

    return image
