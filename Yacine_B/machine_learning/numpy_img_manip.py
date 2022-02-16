import matplotlib.pyplot as plt
import matplotlib.image as plt_img
import numpy as np


img = plt_img.imread('nature.jpg')


def zoom(picture: np.ndarray, rate: float = None):
    if rate is None:
        rate = 0.50
    else:
        if type(rate) is not float or rate >= 1.0:
            raise ValueError("The zoom rate must be an integer smaller than 1.")

    height, width, _ = picture.shape
    reduced_h = int(height * rate / 2)
    reduced_w = int(width * rate / 2)
    return picture[reduced_h:height-reduced_h, reduced_w:width-reduced_w, :]


def negative(picture: np.ndarray):
    return 255 - picture


def black_white(picture: np.ndarray):
    treated = picture
    average_luminosity = picture.mean()

    for i in range(treated.shape[2]):
        treated[treated[:, :, i] < average_luminosity] = 0
        treated[treated[:, :, i] >= average_luminosity] = 255

    return treated


def rotation(picture: np.ndarray, n: int = None):
    if n is None:
        n = 1
    else:
        if type(n) is not int:
            raise ValueError("Number of 90° rotations must be integer.")
        
    return np.rot90(picture, k=n)


_, subs = plt.subplots(2, 3)

subs[0, 0].imshow(img)
subs[0, 1].imshow(zoom(img))
subs[0, 2].imshow(rotation(img, 2))
subs[1, 0].imshow(negative(img))
subs[1, 1].imshow(black_white(img))

plt.show()
