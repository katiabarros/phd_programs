import numpy as np 
from matplotlib import pyplot as plt
import math

x=[]
y=[]

#Create X
m=144
for j in range (124,145):
    n=j
    m=m+1
    for i in range (n,m):
        x.append(i) 
    for i in range (n+1,m+1):
        x.append(i)         

#Create Y
p=122
for k in range (144,165):     
    o=k
    p=p+1
    for l in range (o,p,-1):
        y.append(l) 
    for l in range (o,p,-1):
        y.append(l)

x=np.array(x)
y=np.array(y)

val=len(x)
z=np.zeros(val)
lwc=np.zeros(val)
reff=np.zeros(val)

for le in range (0,val):
    lwc[le]=1#random.uniform(0.1,1)
    reff[le]=10#random.uniform(2,14)
    z[le]=32

cloud=np.flipud(np.array([reff,lwc,z,y,x]))
cloud=np.transpose(cloud)

la=[]
raiz=int(math.sqrt(len(x)/2))
for i in range (0,len(x),raiz):
    la.append(i)

nx=[]
ny=[]
nz=[]
nlwc=[]
nreff=[]
k=2


#create a for outside for how many times I want it to run, so I'll only need one of this
for i in range (0,k):
    for j in range (0,len(x)):
       nz.append(z[j]-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])

for i in range (0,k):
    for j in range (la[1],len(x)):
       nz.append(z[j]-k-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])

for i in range (0,k):
    for j in range (la[2],len(x)):
       nz.append(z[j]-(2*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])


for i in range (0,k):
    for j in range (la[3],len(x)):
       nz.append(z[j]-(3*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])
  
for i in range (0,k):
    for j in range (la[4],len(x)):
       nz.append(z[j]-(4*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])
       
for i in range (0,k):
    for j in range (la[5],len(x)):
       nz.append(z[j]-(5*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])       

for i in range (0,k):
    for j in range (la[6],len(x)):
       nz.append(z[j]-(6*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])
       
for i in range (0,k):
    for j in range (la[7],len(x)):
       nz.append(z[j]-(7*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])       
  
for i in range (0,k):
    for j in range (la[8],len(x)):
       nz.append(z[j]-(8*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j]) 
    
for i in range (0,k):
    for j in range (la[9],len(x)):
       nz.append(z[j]-(9*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])     
       
for i in range (0,k):
    for j in range (la[10],len(x)):
       nz.append(z[j]-(10*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])       
  
for i in range (0,k):
    for j in range (la[11],len(x)):
       nz.append(z[j]-(11*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j]) 
    
for i in range (0,k):
    for j in range (la[12],len(x)):
       nz.append(z[j]-(12*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])    
       
for i in range (0,k):
    for j in range (la[13],len(x)):
       nz.append(z[j]-(13*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j])       
  
for i in range (0,k):
    for j in range (la[14],len(x)):
       nz.append(z[j]-(14*k)-i)
       nx.append(x[j])
       ny.append(y[j])
       nreff.append(reff[j])
       nlwc.append(lwc[j]) 
    
       
       
#count=0
#for i in range (0,len(x),la[1]):
#    count=count+1
#    nreff.append(np.array(reff[i:len(x)]))
#    nx.append(np.array(x[i:len(x)]))
#    nlwc.append(np.array(lwc[i:len(x)])) 
#    ny.append(np.array(y[i:len(x)]))
#    nz.append(np.array(z[i:len(x)]-count))


nreff=np.hstack(nreff)
nlwc=np.hstack(nlwc)
nz=np.hstack(nz)
ny=np.hstack(ny)
nx=np.hstack(nx)

new_cloud=np.flipud(np.array([nreff,nlwc,nz,ny,nx]))
new_cloud=np.transpose(new_cloud)

#plt.figure(1)
#plt.plot(x,y,'.')
#plt.xlim(120, 170)
#plt.ylim(120, 170)
#            
##Plot     
#fig=plt.figure(3)
#ax=fig.add_subplot(111,projection='3d')
#ax.scatter(nx,ny,nz,c='r',marker='o')
#ax.set_xlabel('y axis')
#ax.set_ylabel('x axis')
#ax.set_zlabel('z axis')
#plt.gca().invert_xaxis()   
#plt.show


#np.savetxt('Y:/LEIPSIC/bin/inputs/Clouds_for_LEIPSIC/build_cloud_173626.dat', new_cloud)
