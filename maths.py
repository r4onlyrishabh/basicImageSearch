import numpy as np

def chi2Dist(array1, array2):
	d = 0
	k = 1e-10
	for (a, b) in zip(array1, array2):
		num = (a-b)**2
		den = a+b+k
		d += (float)(num/den)
	return d		
