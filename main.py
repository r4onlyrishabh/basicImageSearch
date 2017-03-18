from search import Searcher
from RGBHistogram import RGBHist
import numpy as np
import cPickle
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True, help = "Path to input image")
arg = vars(ap.parse_args())

f = open('dictionary.txt', 'r')
dataset = cPickle.loads(f.read())

queryImage = cv2.imread(arg["query"])
cv2.imshow("QueryImage", queryImage)
print "Query :: %s" %(arg["query"][arg["query"].rfind('/') + 1:])

rgbHist = RGBHist([8, 8, 8])
queryHist = rgbHist.getHist(queryImage)

searcher = Searcher(dataset)
results = searcher.search(queryHist)
	
set1 = np.zeros((150*5, 400, 3), dtype = 'unit8')
set2 = np.zeros((150*5, 400, 3), dtype = 'unit8')

for i in xrange(0, 10):
	(fileName, dist) = results[i]
	print "Result %d :: %s, Score :: %f" %(i, fileName, dist)
	path = './dataset/' + fileName
	image = cv2.imread(path)
	if i < 5:
		set1[150*i:150*(i+1), :, :] = image
	else:
		set2[150*(i-5):150*(i-4), :, :] = image
	
cv2.imshow("SearchResults 1-5", set1)
cv2.imshow("SearchResults 6-10", set2)
cv2.waitKey(0)
