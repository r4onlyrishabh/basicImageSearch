import numpy as np

def chi2Dist(array1, array2):
	d = 0
	k = 1e-10
	for (a, b) in zip(array1, array2):
		d += ((a-b)**2)/(a+b+k)
	return d		
