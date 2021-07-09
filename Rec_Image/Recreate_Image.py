from Select_Image.Image_Selector import Select_Image
import skimage
import numpy as np
import time

image_file = Select_Image()

image = skimage.io.imread(fname=image_file, as_gray=True)
viewer = skimage.viewer.ImageViewer(image)
viewer.show()
time.sleep(5)
