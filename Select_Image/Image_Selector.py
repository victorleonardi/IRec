import tkinter as tk
from tkinter import filedialog


def Select_Image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path
