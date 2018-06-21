
import os
import re
import subprocess

path_src = 'source/'
path_dst = 'target/'

def mkdir(path):
	if not os.path.exists(path):
		os.mkdir(path)

#pdftotext -enc 'UTF-8' aa.pdf - | sed 's/\x0c.*/___endOfPage___/gm' | grep -m 1 -B 10000 '___endOfPage' > aa.txt

mkdir(path_dst)

for file in os.listdir(path_src):
	# if file[0] != '.':
	name, ext = os.path.splitext(file)
	print(file)
	cmd = "pdftotext -enc 'UTF-8' '" + path_src + file + "' - | sed 's/\x0c.*/___endOfPage___/gm' | grep -m 1 -B 10000 '___endOfPage___' | sed 's/___endOfPage___//'> '" + path_dst + name + ".txt'"
	# os.system(cmd)
	subprocess.call(cmd, shell=True)
