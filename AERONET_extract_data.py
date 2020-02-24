import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

aer_2016=pd.read_csv('C:/Users/Mendes/Desktop/atto/Campanha_2018/AERONET/2.0/20160101_20161231_Amazon_ATTO_Tower.txt', skiprows=7, header=None, sep=",",engine='python')
aer_2017=pd.read_csv('C:/Users/Mendes/Desktop/atto/Campanha_2018/AERONET/2.0/20170101_20171231_Amazon_ATTO_Tower.txt', skiprows=7, header=None, sep=",",engine='python')
aer_2018=pd.read_csv('C:/Users/Mendes/Desktop/atto/Campanha_2018/AERONET/2.0/20180101_20181231_Amazon_ATTO_Tower.txt', skiprows=7, header=None, sep=",",engine='python')

doy_16=np.array(aer_2016[2][:])
AOD_500nm_16=np.array(aer_2016[17][:])
doy_17=np.array(aer_2017[2][:])
AOD_500nm_17=np.array(aer_2017[17][:])
doy_18=np.array(aer_2018[2][:])
AOD_500nm_18=np.array(aer_2018[17][:])

for i in range (0,len(aer_2016)):
    if AOD_500nm_16[i]<0:
        AOD_500nm_16[i]=np.nan
        
for i in range (0,len(aer_2017)):
    if AOD_500nm_17[i]<0:
        AOD_500nm_17[i]=np.nan
        
for i in range (0,len(aer_2018)):
    if AOD_500nm_18[i]<0:
        AOD_500nm_18[i]=np.nan        
        
plt.figure (1,figsize=(10,8))        
plt.plot(doy_16,AOD_500nm_16,'o',label='2016')
plt.plot(doy_17,AOD_500nm_17,'o',label='2017')
plt.plot(doy_18,AOD_500nm_18,'o',label='2018')
plt.ylabel('AOD 500 nm',fontsize=20)
plt.xlabel('Day of the year',fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlim(0,365)
plt.ylim(0,1.1)
plt.legend(loc=2, prop={'size': 16})
plt.title('Aerosol optical depth at ATTO',fontsize=24)

#AOD_1640nm=np.array(aer_2016[3][:])
#AOD_1020nm=np.array(aer_2016[4][:])
#AOD_870nm=np.array(aer_2016[5][:])
#AOD_675nm=np.array(aer_2016[8][:])
#AOD_440nm=np.array(aer_2016[20][:])
#pw=np.array(aer_2016[25][:])  #precipitable water [cm]
