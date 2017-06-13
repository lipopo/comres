# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 03:19:09 2017

@author: Administrator
"""

import cv2
import os
import numpy as np

Train_data = "C:/Users/Administrator/Desktop/comres/Train/data_00/"
shape_use = cv2.imread("C:/Users/Administrator/Desktop/comres/Train/shape/shape_02.png",0)
match_result = np.array([])
z = 0
for i in os.listdir(Train_data):
    img = cv2.imread(Train_data+i)
    use = cv2.bitwise_and(img[:,:,2],img[:,:,2],mask=((img[:,:,2]>100)*255).astype(np.uint8))
    edge = cv2.Canny(use,50,150)
    edge_match = cv2.matchShapes(shape_use,edge,1,0)
    if z == 0:
        match_result = np.array([edge_match])
    else:
        match_result = np.append(match_result,np.array([edge_match]))
    cv2.imwrite(Train_data.replace("00","01")+i,edge)
    z = z + 1
    