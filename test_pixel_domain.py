"""
Usage:
METHOD=read,gray,weighted-gray,threshold=60,negative,addition,subtraction IMG=~/Pictures/a.jpg IMG2=~/Pictures/b.jpg python3 test_pixel_domain.py
"""

import os

from pixel_domain import PixelDomain


if 'IMG' not in os.environ:
    raise KeyError('Environment variable IMG not defined.')
img_path = os.environ['IMG']

if "METHOD" not in os.environ:
    raise KeyError('Environment variable METHOD [raw,gray,weighted-gray,negative,threshold=int,addition,subtraction] not defined.')
method = os.environ["METHOD"]

pd = PixelDomain()

raw_img = None
raw_img_2 = None
gray_img = None
negative_img = None
threshold_img = None
addition_img = None
subtraction_img = None

if 'read' in method:
    raw_img = pd.read(img_path)
    pd.write('raw.png', raw_img)
if 'gray' in method:
    gray_img = pd.rgb2gray(raw_img, weighted=False)
    pd.write('gray.png', gray_img)
if 'weighted-gray' in method:
    gray_img = pd.rgb2gray(raw_img)
    pd.write('weighted-gray.png', gray_img)
    # gray_img = pd.rgb2gray(raw_img, 0.07, 0.72, 0.21)
    # pd.write('gray_2.png', gray_img)
if 'negative' in method:
    negative_img = pd.negative(raw_img)
    pd.write('negative.png', negative_img)
if 'threshold' in method:
    for m in method.split(','):
        if 'threshold' in m:
            t = int(m.split('=')[-1])
    threshold_img = pd.threshold(gray_img, t)
    pd.write('threshold.png', threshold_img)
if 'addition' in method:
    if 'IMG2' not in os.environ:
        raise KeyError('Environment variable IMG not defined.')
    raw_img_2 = pd.read(os.environ['IMG2'])
    addition_img = pd.addition(raw_img, raw_img_2)
    pd.write('addition.png', addition_img)
if 'subtraction' in method:
    if 'IMG2' not in os.environ:
        raise KeyError('Environment variable IMG not defined.')
    subtraction_img = pd.subtraction(raw_img, raw_img_2)
    pd.write('subtraction.png', subtraction_img)
