import netCDF4
import numpy as np
import datetime
import matplotlib.pyplot as plt
import os

f = netCDF4.Dataset('Z:/home_rad/Katia/MCarats/Teste/Mie/mie2210.0.cdf')
print(f)

#dimensions(sizes): nlam(1), nmommax(1000), nphamat(4), nreff(25), nthetamax(360), nrho(1)

wavelen=np.array(f.variables['wavelen'])    #(nlam)
reff=np.array(f.variables['reff'])          #(nreff)
ntheta=np.array(f.variables['ntheta'])      #(nlam,nreff,nphamat)
ntheta=ntheta[0,:,0]
theta=np.array(f.variables['theta'])        #(nlam,nreff,nphamat,nthetamax)
theta=theta[0,:,0,:]
phase=np.array(f.variables['phase'])        #(nlam,nreff,nphamat,nthetamax)
phase=phase[0,:,0,:]
nmom=np.array(f.variables['nmom'])          #(nlam,nreff,nphamat)
nmom=nmom[0,:,0]
pmom=np.array(f.variables['pmom'])          #(nlam,nreff,nphamat,nmommax)
pmom=pmom[0,:,0,:]
ext=np.array(f.variables['ext'])            #(nlam,nreff)
ext=ext[0,:]
ssa=np.array(f.variables['ssa'])            #(nlam,nreff)
ssa=ssa[0,:]
gg=np.array(f.variables['gg'])              #(nlam,nreff)
gg=gg[0,:]
refre=np.array(f.variables['refre'])        #(nlam)
refim=np.array(f.variables['refim'])        #(nlam)
rho=np.array(f.variables['rho'])            #(nlam,nreff)
