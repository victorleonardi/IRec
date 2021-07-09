import tkinter as tk
from tkinter import filedialog, image_names
from matplotlib import pyplot as plt
import numpy as np

import time


def Select_Image():
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
