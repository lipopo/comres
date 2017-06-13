# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 04:11:49 2017

@author: Administrator
"""

import cv2
import os
import numpy as np


blob =  cv2.SimpleBlobDetector_create()
orb = cv2.ORB_create()
fast = cv2.FastFeatureDetector_create()
Train_data = "C:/Users/Administrator/Desktop/comres/Train/data_00/"
for i in os.listdir(Train_data):
    img = cv2.imread(Train_data+i,0)
    img_blur = cv2.medianBlur(img,5)
    keypoints = blob.detect(img_blur)
    keypoints2 = orb.detect(img_blur)
    keypoints3 = fast.detect(img_blur)
    img_out = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    img_out2 = cv2.drawKeypoints(img, keypoints2, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    img_out3 = cv2.drawKeypoints(img, keypoints3, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite(Train_data.replace("00","02")+i,img_out)
    cv2.imwrite(Train_data.replace("00","03")+i,img_out2)
    cv2.imwrite(Train_data.replace("00","04")+i,img_out3)