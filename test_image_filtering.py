"""
Usage:
IMG=~/Pictures/a.jpg python3 test_image_filtering.py
"""


import cv2 as cv
import numpy as np

import os

from image_filtering import ImageFiltering


if 'IMG' not in os.environ:
    raise KeyError('Environment variable IMG not defined.')
img_path = os.environ['IMG']

prob = 0.05
if 'PROB' in os.environ:
    prob = float(os.environ['PROB'])

filtering = ImageFiltering()

# Only for grayscale image
image = cv.imread(img_path, 0)
noise_img = filtering.sp_noise(image, prob)
cv.imwrite('sp_noise.jpg', noise_img)

median_using_cv = cv.medianBlur(noise_img, 5)
cv.imwrite('median_cv.jpg', median_using_cv)

median_using_function = filtering.median_filter(noise_img, 5)
cv.imwrite('median_function.jpg', median_using_function)
