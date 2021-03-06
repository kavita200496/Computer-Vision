# -*- coding: utf-8 -*-
"""MIT2019100_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rVwf0nvNXofVbI_1sgFgT0zk3pJ9cyg7
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('/content/sample_data/iiita1.jpg')

edges = cv2.Canny(img, 100, 200)
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('original Image')
plt.subplot(122),plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image')
plt.show()

cv2.imwrite('iiita1_canny_mit2019100.jpg',edges)

