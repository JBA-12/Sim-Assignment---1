#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy
import mpmath as mp

x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list

randvar = np.loadtxt('V.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list


def v_cdf(x):
	if x>0: return 1-mp.exp(-x/2.0)
	else: return 0
vec_v_cdf = scipy.vectorize(v_cdf, otypes=[float])
	
plt.plot(x.T,err, 'o')#plotting the CDF

plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])


plt.savefig('v_cdf.pdf')
plt.savefig('v_cdf.eps')

plt.show()
