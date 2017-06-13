# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import os

Train_data = "C:/Users/Administrator/Desktop/comres/Train/data_00/"

a = np.array([])
z = 0
for i in os.listdir(Train_data):
    if z == 0:
        a = cv2.resize(cv2.imread(Train_data+i),(100,200)).reshape(1,200,100,3)
    else:
        a = np.append(a,cv2.resize(cv2.imread(Train_data+i),(100,200)).reshape(1,200,100,3),axis=0)
    z = z + 1

imgs = a
img_hsv = np.array([])
z = 0
for i in imgs:
    if z == 0:
        img_hsv = cv2.cvtColor(i,cv2.COLOR_BGR2HSV).reshape(1,200,100,3)
    else:
        img_hsv = np.append(img_hsv,cv2.cvtColor(i,cv2.COLOR_BGR2HSV).reshape(1,200,100,3),axis=0)
    z = z + 1
    
imgs_h = img_hsv[:,:,:,0]
imgs_s = img_hsv[:,:,:,1]
imgs_v = img_hsv[:,:,:,2]
imgs_gray = np.array([])
z = 0
for i in imgs:
    if z == 0:
        imgs_gray = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY).reshape(1,200,100)
    else:
        imgs_gray = np.append(imgs_gray,cv2.cvtColor(i,cv2.COLOR_BGR2GRAY).reshape(1,200,100),axis=0)
    z = z + 1 
    

imgs_canny = np.array([])
z = 0
for i in imgs_gray:
    if z == 0:
        imgs_canny = cv2.Canny(i,50,150).reshape(1,200,100)
    else:
        imgs_canny = np.append(imgs_canny,cv2.Canny(i,50,150).reshape(1,200,100),axis=0)
    z = z + 1

match_result = np.zeros(imgs.shape[0])
z = 0
for i in imgs_canny:
    if z == 0:
        match_result[0] = cv2.matchShapes(i,i,1,0)
    else:
        match_result[z] = cv2.matchShapes(i,imgs_canny[0],1,0)
    z = z + 1

z = 0
for i in imgs:
    cv2.imwrite(Train_data.replace("00","01")+str(z)+".jpg",i)
    z = z + 1

z = 0
for i in imgs_gray:
    cv2.imwrite(Train_data.replace("00","02")+str(z)+".jpg",i)
    z = z + 1

z = 0
for i in imgs_canny:
    cv2.imwrite(Train_data.replace("00","03")+str(z)+".jpg",i)
    z = z + 1
    
