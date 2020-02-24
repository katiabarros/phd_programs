import numpy as np
import cv2
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 25, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('*.jpg')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (9,6),None)
    print (ret)

    # If found, add object points, image points (after refining them)
    if ret == True:
         #Add the "true" checkerboard corners
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(20,20),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (9,6), corners2,ret)
        cv2.imshow('img',img)
        cv2.imwrite('Calibration_Image' + str(img) + '.png', img)
        cv2.waitKey(2)

cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

    # Calculate the total reprojection error.  The closer to zero the better.
tot_error = 0  
for i in xrange(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
        tot_error += error
        aa = tot_error/len(objpoints)  
        
print ('Intrinsic Matrix:')
print (str(mtx))
print(' ')
print('Distortion Coefficients: ')
print(str(dist))
print(' ') 
print('Total reprojection error: ')
print (str(aa)) 


#Save data
print ('Saving data file...')
np.savez('calibration_data', dist=dist, mtx=mtx,rvecs=rvecs,tvecs=tvecs)
print ('Calibration complete')

