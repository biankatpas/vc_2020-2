import numpy as np
import cv2 as cv


class PixelDomain:

    def read(self, path):
        return cv.imread(path)

    def write(self, filename, img):
        cv.imwrite(filename, img)

    def get_pixel(self, img, i, j):
        r = img[i,j,0]
        g = img[i,j,1]
        b = img[i,j,2]
        return r, g, b

    def set_pixel(self, img, i, j, r=None, g=None, b=None):
        if r is not None:
            img[i, j, 0] = r
        if g is not None:
            img[i, j, 1] = g
        if b is not None:
            img[i, j, 2] = b
        return img

    def rgb2gray(self, img, red_constant=0.30, green_constant=0.59, blue_constant=0.11, weighted=True):
        gray_array = []
        row, col, _ = img.shape
        for i in range(row):
            for j in range(col):
                r, g, b = self.get_pixel(img, i, j)
                if weighted:
                    gray_pixel = (r*red_constant + g*green_constant + b*blue_constant)
                else:
                    gray_pixel = int(r/3 + g/3 + b/3)
                gray_array.append(gray_pixel)
        gray_img = np.array(gray_array)
        gray_img = gray_img.reshape(row, col)
        return gray_img

    def negative(self, img):
        negative_img = img.copy()
        row, col, _ = img.shape
        for i in range(row):
            for j in range(col):
                r, g, b = self.get_pixel(img, i, j)
                negative_img[i,j,0] = 255 - r
                negative_img[i,j,1] = 255 - g
                negative_img[i,j,2] = 255 - b
        return negative_img

    def threshold(self, gray_img, t=127):
        threshold_img = gray_img.copy()
        threshold_img[threshold_img > t] = 255
        threshold_img[threshold_img < t] = 0
        return threshold_img

    # https://stackoverflow.com/questions/9652960/difference-in-adding-two-images-in-numpy-and-opencv
    def addition(self, img_1, img_2):
        img_1 = img_1.astype('u2')
        img_2 = img_2.astype('u2')
        addition_img = img_1 + img_2
        addition_img = addition_img.clip(0, 255).astype('u1')
        return addition_img

    # https://stackoverflow.com/questions/26678132/python-numpy-subtraction-no-negative-numbers-4-6-gives-254
    def subtraction(self, img_1, img_2):
        img_1 = img_1.astype(np.int16)
        img_2 = img_2.astype(np.int16)
        subtraction_img = img_1 - img_2
        return subtraction_img
