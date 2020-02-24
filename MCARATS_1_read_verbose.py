import numpy as np
import os
import netCDF4
from netCDF4 import Dataset
from multiprocessing import Pool 
import time

# READ THE VERBOSE FILE #################################################
verbose = np.genfromtxt('Z:/home_rad/Katia/MCarats/Teste/own_data/verbose_10008.dat',skip_header=4, max_rows = 93)

atm_p=np.flipud(verbose[:,2])
atm_temp=np.flipud(verbose[:,3])
atm_zgrd=np.flipud(verbose[:,1]*1000)
atm_dz=np.zeros([len(verbose)-1])
atm_abs_l=np.zeros([len(verbose)-1])
atm_sca_l=np.zeros([len(verbose)-1])

for i in range (0,len(verbose)-1):
         atm_dz[i]=atm_zgrd[i+1]-atm_zgrd[i]
    
       
verbose0 = np.genfromtxt('Z:/home_rad/Katia/MCarats/Teste/own_data/verbose_10008.dat',skip_header=102, max_rows = 92)

atm_abs_l=np.flipud(verbose0[:,6]/1000)
atm_sca_l=np.flipud(verbose0[:,4]/1000)
        
#### GET EXTR FLUX SOLAR 
s0f = np.genfromtxt('Y:/NewGuey2003.dat')#,skip_header=295)
wlf=s0f[:,0]
s0f=s0f[:,1]/1000       

with open('Z:/home_rad/Katia/MCarats/Teste/own_data/atmo.dat', 'w') as atmo:    
    atmo.write('# atm_dz='+"\n")
    atmo.write(str(atm_dz)+"\n")
    atmo.write('# atm_p=  \n')
    atmo.write(str(atm_p)+"\n")
    atmo.write('# atm_zgrd='+"\n")
    atmo.write(str(atm_zgrd)+"\n")
    atmo.write('# atm_temp=  \n')
    atmo.write(str(atm_temp)+"\n")
    atmo.write('# atm_abs_l='+"\n")
    atmo.write(str(atm_abs_l)+"\n")
    atmo.write('# atm_sca_l=  \n')
    atmo.write(str(atm_sca_l)+"\n")
    atmo.write('# s0f='+"\n")
    atmo.write(str(s0f)+"\n")
    atmo.write('# wlf=  \n')
    atmo.write(str(wlf)+"\n")
