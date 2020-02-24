import numpy as np
import os

path = '/projekt_agmwend/home_rad/Katia/MCarats/Teste/Mie/'
#x=3000
wl=np.array([2.2100, 2.2320, 2.2545, 2.2775, 2.3009, 2.3248, 2.3492, 2.3742, 2.3996, 2.4256, 2.4522, 2.4794, 2.5072, 2.5356, 2.5647, 2.5944, 2.6248, 2.6560, 2.6879, 2.7206, 2.7541, 2.7884, 2.8236, 2.8597, 2.8967, 2.9347, 2.9737, 3.0138, 3.0549, 3.0972, 3.1407, 3.1854, 3.2314, 3.2788, 3.3275, 3.3778, 3.4295, 3.4829, 3.5380, 3.5949, 3.6536, 3.7142, 3.7769, 3.8418, 3.9089, 3.9784, 4.0504, 4.1251, 4.2026, 4.2830, 4.3666, 4.4536, 4.5440, 4.6382, 4.7364, 4.8388, 4.9458, 5.0576, 5.1746, 5.2971, 5.4255, 5.5604, 5.7021, 5.8512, 6.0083, 6.1741, 6.3494, 6.5348, 6.7314, 6.9402, 7.1624, 7.3993, 7.6524, 7.9234, 8.2143, 8.5273, 8.8652, 9.2310, 9.6282, 10.0612, 10.5350, 11.0555, 11.6302, 12.2679, 12.9796, 13.7790, 14.6833, 15.7146, 16.9018, 18.2829, 19.9099, 21.8547, 24.2207, 27.1610, 30.9139, 35.8702, 42.7191, 52.8006, 69.1105, 100.0000])
wl=wl*1000
for i in range (0,100):
    print('SETUP Mie code')
    print('Mie running')
    with open(path+'run_mie.inp', 'w') as the_file:
        the_file.write('mie_program MIEV0 		# Select Mie code by Wiscombe\n')
        the_file.write('refrac water 			# Use refractive index of water   \n')
        the_file.write('r_eff 1.0 25 1 			# Specify effective radius grid\n')
        the_file.write('distribution gamma 7 	# Specify gamma size distribution (alpha=7)\n')
        the_file.write('wavelength '+str(wl[i])+' '+str(wl[i])+'    	# Define wavelength\n')
        the_file.write('nstokes 4 				# Calculate all phase matrix elements\n')
        the_file.write('nmom 1000 				# Number of Legendre terms to be computed\n')
        the_file.write('nmom_netcdf 1000		# Number of Legendre terms to be stored in\n')
        the_file.write('						# netcdf file, must be > number_of_streams\n')
        the_file.write('nthetamax 360 			# Maximum number of scattering angles to be\n')
        the_file.write('						# used to store the phase matrix\n')
        the_file.write('output_user netcdf 		# Write output to netcdf file\n')
        the_file.write('verbose 				# Print verbose output\n')

    os.system('(mie < '+path+'run_mie.inp > '+path+'out_mie.out)')
    os.rename(path+'wc.gamma_007.0.mie.cdf',path+'mie'+str(wl[i])+'.cdf')

