#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list

#Question-1.2
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')

#Question-2.2
#randvar = np.loadtxt('gau.dat',dtype='double')

#Question-3.1
randvar = np.loadtxt('V.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
plt.plot(x.T,err)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#Question-1.2
#plt.savefig('uni_cdf.pdf')
#plt.savefig('uni_cdf.eps')

#Question-2.2
#plt.savefig('gau_cdf.pdf')
#plt.savefig('gau_cdf.eps')

#Question-3.1
#plt.savefig('v_cdf.pdf')
#plt.savefig('v_cdf.eps')

plt.show()
