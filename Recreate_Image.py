from Select_Image.Image_Selector import Select_Image
from skimage import io
import numpy as np
from matplotlib import pyplot as plt
import time

image_file = Select_Image()

image = io.imread(fname=image_file)
# plt.imshow(image)
# plt.axis('off')
# plt.show()
time.sleep(5)

histogram, bin_edges = np.histogram(image, bins=256, range=(0, 255))

plt.figure()
plt.title("Histograma")
plt.plot(bin_edges[0:-1], histogram)
plt.show()
