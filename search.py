from operator import itemgetter
import numpy as np
from maths import *

class Searcher:
	def __init__(self, datasetDict):
		self.datasetDict = datasetDict

	def search(self, queryHist):
		result = dict()
		for (i, hist) in self.datasetDict.items():
			result[i] = maths.chi2Dist(hist, queryHist)
		
		result = sorted(result.items(), key = itemgetter(1))
		return result
