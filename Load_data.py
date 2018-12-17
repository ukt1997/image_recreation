# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 01:48:05 2018

@author: Ujjwal Kumar and Adnan Jaseem 

program for: my_utils
"""

import os
import cv2
import numpy as np

def load_data(folder_name):
    imgs = []
    for file in os.listdir(folder_name):
        #print(file)
        img = cv2.imread(os.path.join(folder_name,file))
        """cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()"""
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        """cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()"""
        imgs.append(img)
    imgs_arr = np.array(imgs)
    print(imgs_arr.shape)
    return imgs_arr
