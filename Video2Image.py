#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 22:58:36 2020

@author: ahmedbingol
"""

import cv2 
import os 

# Read the video from specified path 
#cam = cv2.VideoCapture("/Users/ahmedbingol/Downloads/migcc_bixler_92415_1116_left.MP4")
cam = cv2.VideoCapture("/Users/ahmedbingol/Downloads/Blacksburg_Encounter12.MP4")
#cam = cv2.VideoCapture("/Users/ahmedbingol/Downloads/Blacksburg_Encounter01.MP4")
#cam = cv2.VideoCapture("/Users/ahmedbingol/Downloads/City-Flight.mp4")   
try: 
      
    # creating a folder named data 
    if not os.path.exists('data/VideoEncounter12'): 
        os.makedirs('data/VideoEncounter12') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
counter=0  
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
    print(ret)
    counter +=1
    if ret: 
        # if video is still left continue creating images 
        if (counter > 30):
            name = './data/VideoEncounter12/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name) 
  
            # writing the extracted images 
            cv2.imwrite(name, frame) 
  
            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += 1
            counter=0
    else: 
        if(counter==250):
            break
    
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 