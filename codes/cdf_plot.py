#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy
import mpmath as mp

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

#Question-1.2
#def uni_cdf(x):
#	if x > 1:
#		return 1
#	elif x < 0:
#		return 0
#	return x
		
#vec_uni_cdf = scipy.vectorize(uni_cdf, otypes=[float])

#Question-2.2
#def Q(x):
#    return mp.erfc(x/mp.sqrt(2))/2
#def gau_cdf(x):
#	return 1-Q(x)
		
#vec_gau_cdf = scipy.vectorize(gau_cdf, otypes=[float])	

#Question-3.1
def v_cdf(x):
	if x>0: return 1-mp.exp(-x/2.0)
	else: return 0
vec_v_cdf = scipy.vectorize(v_cdf, otypes=[float])
	
plt.plot(x.T,err, 'o')#plotting the CDF

#Question-1.2
#plt.plot(x, vec_uni_cdf(x))

#Question-2.2
#plt.plot(x, vec_gau_cdf(x))

#Question-3.1
plt.plot(x, vec_v_cdf(x))

plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

#Question-1.2
#plt.savefig('uni_cdf.pdf')
#plt.savefig('uni_cdf.eps')

#Question-2.2
#plt.savefig('gau_cdf.pdf')
#plt.savefig('gau_cdf.eps')

#Question-3.1
plt.savefig('v_cdf.pdf')
plt.savefig('v_cdf.eps')

plt.show()
