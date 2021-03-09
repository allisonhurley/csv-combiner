# requires python 3
# This solution is low memory but requires that all input 
# files have the exact same column layout
# Allison Hurley 
# 3/8/2021
import sys
import csv
import os

# flags used to ensure header line printed once
first_file = True
header = True

for filename in sys.argv[1:]:
	with open(filename) as file:
		for line in file:
			if header:
				if first_file:
					print(f'{line.rstrip()},"filename"')
					first_file = False
				header = False
			else:
				print(f'{line.rstrip()},"{os.path.basename(filename)}"')
	header = True
