import numpy as np 
from matplotlib import pyplot as plt
import cv2
from matplotlib.lines import Line2D  
 
image = cv2.imread('C:/Users/Mendes/Desktop/Test case/Gopro ATTO/undis_G0017656.jpg')
#plt.imshow(image)

#------------------------------------------------------------------------------
#First open the image above and select the pixels where your cloud is on the values below
#--------------------------------------------------------------------------------
x1=1010
x2=2000
y2=1360
y1=2040

#plt.figure
#plt.imshow(image[y2:y1,x1:x2],extent=(x1,x2,y1,y2))

dx=x2-x1
dy=y1-y2

#-----------------------change here the number of pixels in x and y------------------
px=30
py=17

dummyx=dx/px
dummyy=dy/py

xlines=[]
ylines=[]

for i in range (x1,x2,dummyx):
    xlines.append(i)

for i in range (y2,y1,dummyy):
    ylines.append(i)    

xplot=np.zeros([len(xlines),dy])
yplot=np.zeros([dx,len(ylines)])


fig=plt.figure()
ax=fig.add_subplot(111)
ax.imshow(image[y2:y1,x1:x2],extent=(x1,x2,y1,y2))

for l in range (0,len(xlines)): 
        for i in range (y2,y1):
           ax.plot(xlines[l],i,'r.',markersize=0.4)


for k in range (0,len(ylines)):        
    for j in range (x1,x2):
        ax.plot(j,ylines[k],'g.',markersize=0.4)  
        
fig.savefig('C:/Users/Mendes/Desktop/cloud_173626.png', bbox_inches='tight',dpi=300)         
