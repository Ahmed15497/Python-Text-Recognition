# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:24:56 2020

@author: ahmed
"""

import cv2
import csv
import os
import sys

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

import easyocr



if len(sys.argv) > 2:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 2:
    print('You need to specify the path to be listed')
    sys.exit()

input_path = sys.argv[1]

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

#print('\n'.join(os.listdir(input_path)))



img_list = os.listdir(input_path)




reader = easyocr.Reader(['en'])


with open(f'{input_path}/output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["File Name", "Date taken", "Title", "Artist", "Current time"])
    for img_name in img_list:

      try:
          image = cv2.imread(f'{input_path}/{img_name}')
          title = image[825:925,275:950, :]
          artist = image[900:1000,275:950, :]
          current_time = image[1000:1250,10:300, :]
          date_taken = image[550:680,250:850,:]
    
          date_taken_str = ' '.join(map(str, reader.readtext(date_taken, detail=0))) 
          title_str = ' '.join(map(str, reader.readtext(title, detail=0))) 
          artist_str = ' '.join(map(str, reader.readtext(artist, detail=0))) 
          current_time_str = ' '.join(map(str, reader.readtext(current_time, detail=0))) 
          writer.writerow([img_name, date_taken_str, title_str, artist_str, current_time_str])
      except:
          print(f'{img_name} is not an image')

print('The output is saved to output.csv')

#cv2.imshow('a', image)
#cv2.waitKey()




