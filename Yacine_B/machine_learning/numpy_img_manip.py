from scipy import misc
import matplotlib.pyplot as plt
import numpy as np


face = misc.face()
plt.imshow(face)
plt.show()

length, width, _ = face.shape

zoomed_face = face[length//8:7*length//8, width//8:7*width//8, :]
plt.imshow(zoomed_face)
plt.show()


def negative(picture: np.ndarray):
    return 255 - picture


def black_white(picture: np.ndarray):
    treated = picture
    average_luminosity = picture.mean()
    print(treated.flags)

    treated[treated < average_luminosity] = 0
    treated[treated >= average_luminosity] = 255

    return treated


plt.imshow(negative(zoomed_face))
plt.show()

plt.imshow(black_white(zoomed_face))
plt.show()
