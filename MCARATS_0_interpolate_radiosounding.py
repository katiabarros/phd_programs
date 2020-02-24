# -*- coding: utf-8 -*-

import numpy as np


Height_lib = np.array([0,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3600,3700,3800,3900,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000])


print('SETUP LibRadtran Radio Sounding')
DS = np.genfromtxt('C:/Users/Mendes/Desktop/atto/Campanha_2018/RadioSoundings/Libradtran_RS_Manaus0930_00_raw.txt')
DS_Alt  = DS[:,1]
Layer_temp = DS[:,2]
Layer_relhum = DS[:,4]
Layer_pres = DS[:,0]

# Interpolate Temp COARSE PROFILE
T_lib = np.interp(Height_lib,DS_Alt,Layer_temp)
Relh_lib = np.interp(Height_lib,DS_Alt,Layer_relhum)
Pres_lib=np.interp(Height_lib,DS_Alt,Layer_pres)

### WRITE LIBRADTRAN ATMOS FILE
atmos_file = 'Y:/MCarats/test/LibRadtran_ATTO_Temp.dat'
Out_arr =  np.empty((len(Pres_lib),3))
Out_arr[:,0] = np.flipud(Pres_lib)
Out_arr[:,1] = np.flipud(T_lib)+273.15
Out_arr[:,2] = np.flipud(Relh_lib)
Out_file= np.savetxt(atmos_file,Out_arr,fmt='%13.3f')
