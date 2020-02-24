import numpy as np
import matplotlib.pyplot as plt


#rad=np.memmap('Z:/home_rad/Katia/MCarats/Teste/own_data/shcloud_1.out',dtype='float32',mode='r',shape=(110,90))
rad=np.memmap('Z:/home_rad/Katia/MCarats/Teste/own_data/shcloud90_05.out',dtype='float32',mode='r',shape=(90,90))
rad=np.flip(rad,1)

plt.figure(1,figsize=(15,4))
plt.imshow(rad[40:90,20:70],extent=(20,70,90,40))
plt.colorbar()
