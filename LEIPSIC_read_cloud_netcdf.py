import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import xarray as xr
import matplotlib.patches as mpatches
from scipy.io import netcdf

c='60'
cloud=Dataset('Y:/LEIPSIC/bin/inputs/Clouds_for_LEIPSIC/scan_'+c+'liq_0.cdf','r')

#print cloud.dimensions
#print cloud.variables.keys()
#x=151 y=71  z=68

x=np.array(cloud.variables['x'][:])
y=np.array(cloud.variables['y'][:])
z=np.array(cloud.variables['z'][:])
lwc=np.array(cloud.variables['lwc'][:])
reff=np.array(cloud.variables['r_eff_wc'][:])
cloud.close()

ilwc=np.sum(lwc,axis=0)  

for i in range (0,len(x)):
    for j in range (0,len(y)):
        for k in range (0,len(z)):
          if reff[k,j,i]==0:
              reff[k,j,i]=('nan')
          if lwc[k,j,i]==0:
              lwc[k,j,i]=('nan')
          if ilwc[j,i]==0:
              ilwc[j,i]=('nan')              

plt.figure(1,figsize=(7.5,3.5))
plt.imshow(reff[:,:,120],cmap = 'plasma')
plt.gca().invert_yaxis()
plt.colorbar(orientation='vertical', pad = 0.05, label='Effective radius [um]')
plt.title('Effective radius at x = 24 km (120 px) for cloud '+c)
plt.xlabel(r'y')
plt.ylabel('z')
plt.savefig('C:/Users/Mendes/Desktop/LEIPSIC/bin/inputs/Clouds_for_LEIPSIC/reff_'+c+'.png', bbox_inches='tight',dpi=300)

plt.figure(2,figsize=(10,4))
plt.imshow(ilwc,cmap = 'inferno')
plt.gca().invert_yaxis()
plt.colorbar(orientation='vertical', pad = 0.05, label='Liquid water path [kg/m$^3$]')
plt.title('Liquid water path over domain for cloud '+c)
plt.xlabel(r'x')
plt.ylabel('y')
plt.savefig('C:/Users/Mendes/Desktop/LEIPSIC/bin/inputs/Clouds_for_LEIPSIC/ilwc_'+c+'.png', bbox_inches='tight',dpi=300)
