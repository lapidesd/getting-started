import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt

#read data
mydata = Dataset('rce300_snapshot.nc','r')

#store temperature data in array
temparray=mydata.variables['tabs']

#store variables to plot
#temperature array of averages spanning x and y at fixed z
avgarray=[]
height=mydata.variables['z'][0:64]

#find horizontal averages
for i in range(64):
	#temperature array at fixed z, spanning y and x
	tempya=[]
	for j in range(16):
		#temperature array at fixed y and fixed z, spanning x
		tempy=[]
		for k in range(16):
			tempy=tempy+[temparray[0,i,j,k]]
		#average temperature at fixed y and fixed z, spanning x
		avg=sum(tempy)/16
		tempya=tempya+[avg]
	avrg=sum(tempya)/16
	avgarray=avgarray+[avrg]

#save and plot of horizontal averages
plt.plot(avgarray,height)
plt.ylabel('Height (m)')
plt.xlabel('Average Temperature (K)')
plt.title('Horizontal Temperature Profile')
plt.savefig('horiztemp.pdf')

mydata.close()