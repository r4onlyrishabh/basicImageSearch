import cv2
import numpy as np

class RGBHist:
	def __init__(self, bins):
		self.bins = bins

	def getHist(self, image):
		hist = cv2.calcHist([image], [0, 1, 2], None, self.bins, [0, 256, 0, 256, 0, 256])
		hist = cv2.normalize(hist)
		
		return hist.flatten() 
