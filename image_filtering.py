import numpy as np
import random


class ImageFiltering:

    # https://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv
    def sp_noise(self, image,prob):
        '''
        Add salt and pepper noise to image
        prob: Probability of the noise
        '''
        output = np.zeros(image.shape,np.uint8)
        thres = 1 - prob
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                rdn = random.random()
                if rdn < prob:
                    output[i][j] = 0
                elif rdn > thres:
                    output[i][j] = 255
                else:
                    output[i][j] = image[i][j]
        return output

    # https://www.researchgate.net/publication/332574579_Image_Processing_Course_Project_Image_Filtering_with_Wiener_Filter_and_Median_Filter
    def median_filter(self, data, kernel_size):
        temp = []
        indexer = kernel_size // 2
        data_final = []
        data_final = np.zeros((len(data), len(data[0])))

        for i in range(len(data)):
            for j in range(len(data[0])):
                for z in range(kernel_size):
                    if i + z - indexer < 0 or i + z - indexer > len(data) -1:
                        for c in range(kernel_size):
                            temp.append(0)
                    else:
                        if j + z - indexer < 0 or j + indexer > len(data[0]) -1:
                            temp.append(0)
                        else:
                            for k in range(kernel_size):
                                temp.append(data[i + z - indexer][j + k - indexer])
                temp.sort()
                data_final[i][j] = temp[len(temp) // 2]
                temp = []
        return data_final
