import numpy as np 
import math
from matplotlib import pyplot as plt
import pandas as pd
import datetime
import glob

##---------------------define the dates and wl---------------------
day='20180928'
Case='4'
# ##---------------------convert the date to doy---------------------
date = pd.to_datetime(day, format='%Y%m%d')
new_year_day = pd.Timestamp(year=date.year, month=1, day=1)
doy = (date - new_year_day).days + 1

##---------------------calculate the factor to multiply the output of leipsic
eps = 0.01673
perh= 2.
pi  = 3.14159

rsun=(1.-eps*math.cos(2*pi*(doy-perh)/365.)) # Earth-Sun distance in AU
solfac = 1./(rsun**2)

s0=np.genfromtxt('C:/Users/Mendes/Desktop/Cases/kurudz_1.0nm.dat',skip_header=11)#, max_rows = 442)
wl=s0[:,0]
s0=s0[:,1]/1000

multiply=s0*solfac
weight_s0=np.transpose(np.array([wl,multiply]))

path='C:/Users/Mendes/Desktop/Cases/'+str(day)+'/Case '+str(Case)+'/Simu/'
file=glob.glob(path+'*.txt')

for i in range (0,len (file)):
    wl0=file[i][57:60]
    time=file[i][70:76] #[71:77]


# ##-----------find the factor to the wl I'm working with---------------------
    k=np.where(wl==int(wl0))
    print(weight_s0[k])

# ##--------------open the output and multiply with the factor and plot-------
    plt.figure(i)
    test=np.load(path+'cloud_'+str(wl0)+'_'+str(day)+'_'+str(time)+'.npy')
    plt.imshow(test[0:90,0:90]*multiply[k],cmap = 'gist_ncar',extent=(0,90,90,0))
    cb = plt.colorbar()
    la=np.save(path+'calib_'+str(wl0)+'_'+str(day)+'_'+str(time)+'.npy',test*multiply[k])
