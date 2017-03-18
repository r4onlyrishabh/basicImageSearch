from RGBHistogram import RGBHist
import glob
import cv2
import cPickle
import numpy as np

dataset = {}

rgbHist = RGBHist([8, 8, 8])

for path in glob.glob("./dataset/*")
	fileName = path[path.rfind('/') + 1:]
	image = cv2.imread(path)
	hist = rgbHist.getHist(image)
	dataset[fileName] = hist


f = open('dictionary.txt', 'w')
f.write(cPickle.dumps(dataset))
f.close()


