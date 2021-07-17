import tkinter as tk
from tkinter import filedialog, image_names
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

import time


def Select_Image():
    '''Função que permite selecionar uma imagem nos arquivos da maquina'''
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


# def Open_Image(path, show=True):
#     image_array = io.imread(fname=path)
#     match show:
#         case True:
#             plt.imshow(image_array)
#             plt.axis('off')
#             plt.show()
#     return image_array
# Ver como atualizar o python da venv

def Blank_Canvas_Creator(img):
    '''Função que cria um quadro branco a ser preenchido no formato da imagem passada'''
    # Cria um array com o formato passado, preenchido com o valor informado
    blank = np.full(img.shape[:2], 255, dtype='uint8')
    blank_canvas = cv.merge([blank, blank, blank])
    return blank_canvas
