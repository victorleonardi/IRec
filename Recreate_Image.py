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

# colors = ('red', 'green', 'blue')
# channel_ids = (0, 1, 2)
# plt.xlim([0, 256])

# for channel_id, c in zip(channel_ids, colors):
#     histogram, bin_edges = np.histogram(
#         image[:, :, channel_id], bins=256, range=(0, 256)
#     )
#     plt.plot(bin_edges[0:-1], histogram, color=c)

# a sintaxe '...' desempacota tudo até o elemento final, dado por 0 aqui.
red = image[..., 0]
green = image[..., 1]
blue = image[..., 2]

fig, axs = plt.subplots(2, 2)

cax_00 = axs[0, 0].imshow(image)
axs[0, 0].xaxis.set_major_formatter(plt.NullFormatter())  # kill xlabels
axs[0, 0].yaxis.set_major_formatter(plt.NullFormatter())  # kill ylabels

cax_01 = axs[0, 1].imshow(red, cmap='Reds')
fig.colorbar(cax_01, ax=axs[0, 1])
axs[0, 1].xaxis.set_major_formatter(plt.NullFormatter())
axs[0, 1].yaxis.set_major_formatter(plt.NullFormatter())

cax_10 = axs[1, 0].imshow(green, cmap='Greens')
fig.colorbar(cax_10, ax=axs[1, 0])
axs[1, 0].xaxis.set_major_formatter(plt.NullFormatter())
axs[1, 0].yaxis.set_major_formatter(plt.NullFormatter())

cax_11 = axs[1, 1].imshow(blue, cmap='Blues')
fig.colorbar(cax_11, ax=axs[1, 1])
axs[1, 1].xaxis.set_major_formatter(plt.NullFormatter())
axs[1, 1].yaxis.set_major_formatter(plt.NullFormatter())
plt.show()

# Plot histograms
fig, axs = plt.subplots(3, sharex=True, sharey=True)

axs[0].hist(red.ravel(), bins=10)
axs[0].set_title('Red')
axs[1].hist(green.ravel(), bins=10)
axs[1].set_title('Green')
axs[2].hist(blue.ravel(), bins=10)
axs[2].set_title('Blue')

plt.show()
