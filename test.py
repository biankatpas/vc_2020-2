"""
Usage:
IMG=/home/biankatpas/Pictures/a.jpg IMG2=/home/biankatpas/Pictures/b.jpg python3 run.py
"""

import os

from filter import Filter


if 'IMG' not in os.environ:
    raise KeyError('Environment variable IMG not defined. Good luck.')
img_path = os.environ['IMG']

filter = Filter()

raw_img = filter.read(img_path)
filter.write('raw.png', raw_img)

gray_img = filter.rgb2gray(raw_img)
filter.write('gray.png', gray_img)
# gray_img = filter.rgb2gray(raw_img, 0.07, 0.72, 0.21)
# filter.write('gray_2.png', gray_img)
# gray_img = filter.rgb2gray(raw_img, weighted=False)
# filter.write('gray_3.png', gray_img)

negative_img = filter.negative(raw_img)
filter.write('negative.png', negative_img)

# threshold_img = filter.threshold(gray_img)
# filter.write('threshold.png', threshold_img)
# threshold_img = filter.threshold(gray_img, 150)
# filter.write('threshold_2.png', threshold_img)
threshold_img = filter.threshold(gray_img, 100)
filter.write('threshold_3.png', threshold_img)

if 'IMG2' in os.environ:
    raw_img_2 = filter.read(os.environ['IMG2'])
    addition_img = filter.addition(raw_img, raw_img_2)
    filter.write('addition.png', addition_img)

    subtraction_img = filter.subtraction(raw_img, raw_img_2)
    filter.write('subtraction.png', subtraction_img)
