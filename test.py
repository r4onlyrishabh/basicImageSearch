from search import Searcher
import numpy as np
import cPickle
import cv2

f = open('dictionary.txt', 'r')
dataset = cPickle.loads(f.read())

searcher = Searcher(dataset)

for (queryImage, queryHist) in dataset.items():
	results = searcher.search(queryHist)
	
	path = './dataset/' + queryImage
	image = cv2.imread(path)
	cv2.imshow("QueryImage", image)
	
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
