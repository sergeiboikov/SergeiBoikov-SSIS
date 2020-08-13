import itertools as it
import sys
import os
status = None
date = None

if os.path.exists(sys.argv[1]):
	new_file = open(os.path.splitext(sys.argv[1])[0] + '_prepared.csv', 'w')

	with open(sys.argv[1], mode='r', encoding='cp1252') as f:
		for line in f.readlines():
			if len(line.strip()) > 0:
				if line.startswith('Status='):
					status_line = line.split(',')[0]
					status = status_line.split('=')[1]
				else:
					#Get date
					date = line.split(',')[0]
					#Get list with Latitudes
					_la = line.split(',')[1::3]
					#Get list with Longitudes
					_lo = line.split(',')[2::3]
					#Get list with counts
					_c = line.split(',')[3::3]
					if len(_la) == len(_lo) == len(_c):
						#Aggregate elements from lists
						for (la, lo, c) in zip(_la, _lo, _c):
							#while lists are not empty
							if len(la) > 0 and len(lo) > 0 and len(c) > 0:
								new_file.write(status.strip() + "," + date.strip() + "," + la.strip() + "," + lo.strip() + "," + c.strip() +"\n")
	new_file.close()