import os
dir_path = os.path.dirname(__file__)

cereals = open(dir_path + "/cereals2.csv")
title = cereals.readline()

for line in cereals:
	pass