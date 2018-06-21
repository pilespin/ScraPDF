
from shutil import copyfile
import os

poolSize = 10000
path = 'source/'
file = 'JPMorgan_AmazoncomAlexa,WhatWillAmazonDisruptNextTakingaCloserLookatRingAmazonsSmartHomeStrategy_Mar_23,_2018 (2) (2).pdf'

def mkdir(path):
	if not os.path.exists(path):
		os.mkdir(path)

mkdir(path)

for i in range(poolSize):
	copyfile(file, path + str(i+1) + file)

