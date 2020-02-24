import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

cloud_micro=pd.read_csv('Y:/LEIPSIC/bin/inputs/Clouds_for_LEIPSIC/square_100_21px.dat', skiprows=2, header=None, sep="\t",engine='python')

x=np.array(cloud_micro[0][:])
y=np.array(cloud_micro[1][:])
z=np.array(cloud_micro[2][:])
lwc=np.array(cloud_micro[3][:])
reff=np.array(cloud_micro[4][:])


nreff=np.zeros(len(x))

adiabatic_profile=np.genfromtxt('C:/Users/Mendes/Desktop/LEIPSIC/adiabatic_150637.dat')

a=[]
b=[]
for i in range (40,11,-1):
    a.append(i)
for j in range (0,len(adiabatic_profile)):
    b.append(j)
la=np.transpose(np.flipud(np.array([a,b])))


for k in range (0,len(x)):
    for i in range (0,len(adiabatic_profile)):              
            if z[k]==la[i,1]: 
                nreff[k]=adiabatic_profile[la[i,0],1]  #random.uniform(1.23,22.8)
                lwc[k]=adiabatic_profile[la[i,0],2] #random.uniform(0.0009,3.313)
       
cloud=np.transpose(np.flipud(np.array([reff,nreff,z,y,x])))


test=[]

for k in range (0,len(x),21):              
    if z[k]==40:        
       a=k+8
       b=k+11
       c=k+14
       d=k+15           
       new=cloud[a:b]
       test.append(new)
       new=cloud[c:d]
       test.append(new)        

    if z[k]==39:        
       a=k+7
       b=k+12
       c=k+14
       d=k+15
       new=cloud[a:b]
       test.append(new)
       new=cloud[c:d]
       test.append(new)       
       
    if z[k]==38:           
       a=k+6
       b=k+18         
       new=cloud[a:b]
       test.append(new)     

    if z[k]==37:          
       a=k+6
       b=k+18
#       c=k+10
#       d=k+18         
       new=cloud[a:b]
       test.append(new)
#       new=cloud[c:d]
#       test.append(new) 
       
    if z[k]==36:          
       a=k+5
       b=k+19      
       new=cloud[a:b]
       test.append(new) 
       
    if z[k]==35:          
       a=k+4
       b=k+18    
       new=cloud[a:b]
       test.append(new)  
       
    if z[k]==34:   
       a=k+4
       b=k+17            
       new=cloud[a:b]
       test.append(new)        
       
    if z[k]==33:        
       a=k+2
       b=k+16      
       new=cloud[a:b]
       test.append(new)       
       
    if z[k]==32:         
       a=k+2
       b=k+16      
       new=cloud[a:b]
       test.append(new)       

    if z[k]==31:         
       a=k
       b=k+16
       new=cloud[a:b]
       test.append(new) 
       
    if z[k]==30:         
       a=k+2
       b=k+17    
       new=cloud[a:b]
       test.append(new)        
       
    if z[k]==29:           
       a=k+1
       b=k+18       
       new=cloud[a:b]
       test.append(new)       
       
    if z[k]==28:          
       a=k+3
       b=k+18      
       new=cloud[a:b]
       test.append(new)       
       
    if z[k]==27:        
       a=k+3
       b=k+18       
       new=cloud[a:b]
       test.append(new)       
       
    if z[k]==26:          
       a=k+3
       b=k+19   
       new=cloud[a:b]
       test.append(new)  
    
    if z[k]==25:        
       a=k+1
       b=k+20    
       new=cloud[a:b]
       test.append(new) 
       
    if z[k]==24:          
       a=k+1
       b=k+19           
       new=cloud[a:b]
       test.append(new)        

    if z[k]==23:          
       a=k+1
       b=k+18      
       new=cloud[a:b]
       test.append(new)       
       
    if z[k]==22:          
       a=k+1
       b=k+20        
       new=cloud[a:b]
       test.append(new)        

    if z[k]==21:          
       a=k
       b=k+20      
       new=cloud[a:b]
       test.append(new) 
       
    if z[k]==20:          
       a=k+1
       b=k+20        
       new=cloud[a:b]
       test.append(new)        

    if z[k]==19:        
       a=k+2
       b=k+20       
       new=cloud[a:b]
       test.append(new)

    if z[k]==18:           
       a=k+2
       b=k+18        
       new=cloud[a:b]
       test.append(new)

    if z[k]==17:          
       a=k+3
       b=k+17
       new=cloud[a:b]
       test.append(new)
     
    if z[k]==16:          
       a=k+2
       b=k+17      
       new=cloud[a:b]
       test.append(new) 
       
    if z[k]==15:          
       a=k+2
       b=k+20           
       new=cloud[a:b]
       test.append(new)        
       
    if z[k]==14:   
       a=k
       b=k+19   
       new=cloud[a:b]
       test.append(new) 
       
    if z[k]==13:        
       a=k
       b=k+16      
       new=cloud[a:b]
       test.append(new)       
       
    if z[k]==12:         
       a=k
       b=k+15     
       new=cloud[a:b]
       test.append(new)       

     
test=np.vstack(test)
#test[:,2]=test[:,2]  
plt.plot(test[:,0],test[:,1],'.')
plt.plot(100,100,'.')
plt.xlim(120, 170)
plt.ylim(120, 170)

#
#
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(test[:,0],test[:,1],test[:,2],c='r',marker='o')
#ax.scatter(cloud[:,0],cloud[:,1],cloud[:,2],c='r',marker='o')
ax.set_xlabel('y axis')
ax.set_ylabel('x axis')
ax.set_zlabel('z axis')
plt.gca().invert_xaxis()   
plt.show
##
##np.savetxt('Y:/LEIPSIC/bin/inputs/Clouds_for_LEIPSIC/build_cloud_173626.dat', test)
