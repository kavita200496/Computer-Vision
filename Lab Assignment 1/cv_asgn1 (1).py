# -*- coding: utf-8 -*-
"""cv_asgn1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/0BwWVBBcdeuSdWFR3SkgySWZVR0VIOEFJa3hQVFVTRTI1Z0VR
"""

import numpy as np
from matplotlib import pyplot as plt 
import cv2
img=cv2.imread("/content/sample_data/images.jpeg")
original=img.copy()
print("dimensions of image=",img.shape)
#plt.imshow(img)
#plt.show

##converting image to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
plt.show

##Finding the pixels having value 6 in original image
print("Indexes of pixels bearing value 6 in original image")
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        for k in range(0,img.shape[2]):
            if(img[i][j][k]==6):
                print(i,",",j,",",k)

##Finding the pixels having value 6 in grayscale image
print("grayscale image shape=",gray.shape)
print("Indexes of pixels bearing value 6 in grayscale image")
for i in range(0,gray.shape[0]):
    for j in range(0,gray.shape[1]):
            if(gray[i][j]==6):
                print(i,",",j)

##Finding the darkest spot in image
(minval,maxval,minloc,maxloc)=cv2.minMaxLoc(gray)
cv2.circle(img,minloc,20,(255,0,0),2)
plt.imshow(img)
cv2.circle(gray,minloc,20,(255,0,0),2)
print("location with darkest pixel in original image and grayscale image =",minloc)

##editing the 30*30 range into white
for i in range(0,30):
    for j in range(0,30):
        for k in range(0,3):
            img[i][j][k]=255
plt.imshow(img)

##drawing gray square with pixel 100 at the middle of square
img=original.copy()
startpoint=((img.shape[0]+1)//2-25,img.shape[1]//2-25)
endpoint=((img.shape[0]+1)//2 +25,img.shape[1]//2+25)
print(startpoint,endpoint)
cv2.rectangle(img, startpoint, endpoint, (211, 211, 211), -1)
plt.imshow(img)

##calculating average RGB value
img=original.copy()
plt.imshow(img)
temp=np.mean(img,axis=0)
avgrgb=np.mean(temp,axis=0)
print("The average RGB value is",avgrgb)
##subtracting the average RGB from its corresponding channel
img=img-avgrgb
print("image after subtracting")
plt.imshow(img)

img=original.copy()
(h,w)=(img.shape[0],img.shape[1])
M = cv2.getRotationMatrix2D((w/2,h/2), 30, 1.0)
rotated90 = cv2.warpAffine(img, M, (h, w))
##rotating image by 30 degrees anticlockwise
plt.imshow(rotated90)

##compare above with the original image below
plt.imshow(original)

##upscaling by a factor of 2
img=original
mwidth=int(img.shape[1]*200/100)
mheight=int(img.shape[0]*200/100)
modified_shape=(mwidth,mheight)
resized=cv2.resize(img,modified_shape,interpolation=cv2.INTER_AREA)
plt.imshow(resized)
print(resized.shape)

##shifting image 0,0 to 10,10
img[10][10]=img[0][0]
plt.imshow(img)

##applying canny edge detector 
edges=cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('original Image')
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Edge Image')

plt.show()