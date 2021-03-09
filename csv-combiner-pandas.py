# This solution collects all files into memory
# Files can have different column layouts and will be correctly joined
# Allison Hurley 
# 3/8/2021
import sys
import csv
import os
import pandas as pd

files = sys.argv[1:]
frames = []

for filename in files:
	df = pd.read_csv(filename)
	df['filename'] = os.path.basename(filename)
	frames.append(df)

output = pd.concat(frames, ignore_index=True)

output.to_csv(sys.stdout,index=False,quoting=csv.QUOTE_NONNUMERIC)

