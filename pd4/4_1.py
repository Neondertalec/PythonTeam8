import os
dir_path = os.path.dirname(__file__)

mbox_short = open(dir_path + "/mbox-short.txt")

count = 0

for line in mbox_short:
	if(line.startswith('From ')):
		print(line.split()[1])
		count += 1

print(f"There wre {count} lines in the file with From as the first word")