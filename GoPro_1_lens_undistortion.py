# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:55:41 2017

@author: Kátia Mendes
"""

import numpy as np
import cv2
import glob

#Open the calibration from the other program
npz_calib_file = np.load('calibration_data.npz')
dist = npz_calib_file['dist']
mtx = npz_calib_file['mtx']
npz_calib_file.close()


crop=1
image_size=(4000,3000)


images = glob.glob('*.jpg')


for fname in images:
    img2 = cv2.imread(fname)
    h,  w = img2.shape[:2]
    newMat, ROI = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 0, centerPrincipalPoint = 1)
    mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newMat, (w,h), m1type = cv2.CV_32FC1)
    dst = cv2.remap(img2, mapx, mapy, cv2.INTER_LINEAR)
    outfile = 'undis_' + fname
    print('Undistorted image written to: %s' % outfile)
    cv2.imwrite (outfile, dst)
    
    
   
    
   # cv2.imwrite( img2 + 'und.png',dst)
   # char = cv2.waitKey(0)
    cv2.destroyAllWindows()
  
   #cv2.imshow('Undisorted Image',dst)
