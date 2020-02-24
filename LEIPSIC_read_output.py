#program written by Katia Mendes on 21.05.2019
#first look at LEIPSIC outputs

import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt

#column_names = ['detectorPos', 'x', 'y', 'z', 'detectorRecvDir', 'sza','azimuth','solarIncident','sza','phi0','relErr','eI','eQ','eU','I','Q','U','ivar','qvar','uvar','hasCloudOnSight?','yes/no','dont']

data_blue=pd.read_table('Y:/LEIPSIC/bin/cloud15_446_180_105.txt', skiprows=16, header=None, sep=r"\s*",engine='python')

szab=180-np.array(data_blue[5][:])
azimuthb=np.array(data_blue[6][:])
Ib=np.array(data_blue[17][:])
Qb=np.array(data_blue[18][:])
Ub=np.array(data_blue[19][:])
cloudb=np.array(data_blue[21][:])
pathb=np.array(data_blue[22][:])
errorIb=np.array(data_blue[11][:])*100

     
nIb=np.zeros([90,180])
neIb=np.zeros([90,180])

for k in range (0,len(data_blue)):
    for i in range (0,180):
        for j in range (0,90):   
            if azimuthb[k]==i+90 and szab[k]==j:
               nIb[j,i]=Ib[k]
               neIb[j,i]=errorIb[k]


np.save('cloud15_446_180_105.npy',nIb)
np.save('cloud15_446_180_error_105.npy',neIb)


plt.figure(1)
plt.plot(azimuthb,Ib,'.')
plt.ylim(0,0.2)
plt.xlabel(r'Azimuth [$^\circ$]')
plt.ylabel('Radiance in 446 nm [mW.m$^2$]')
plt.title('Radiance around ATTO, SZA=30$^\circ$, SAA=90$^\circ$')
plt.savefig('C:/Users/Mendes/Desktop/LEIPSIC/bin/inputs/Clouds_for_LEIPSIC/cloud15_446_180_saa.png', bbox_inches='tight',dpi=300)

plt.figure(2)
plt.plot(Ib,szab,'.')
plt.xlim(0,0.2)
plt.gca().invert_yaxis()
plt.ylabel(r'Zenith Angle [$^\circ$]')
plt.xlabel('Radiance in 446 nm [mW.m$^2$]')
plt.title('Radiance around ATTO, SZA=30$^\circ$, SAA=90$^\circ$')
plt.savefig('C:/Users/Mendes/Desktop/LEIPSIC/bin/inputs/Clouds_for_LEIPSIC/cloud15_446_180_sza.png', bbox_inches='tight',dpi=300)

