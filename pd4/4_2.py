import os
dir_path = os.path.dirname(__file__)

mbox_short = open(dir_path + "/mbox-short.txt")

domains = {}
max_length = 0

for line in mbox_short:
	if(line.startswith('From ')):
		domain_name = line.split()[1].split('@')[1]
		
		if len(domain_name) > max_length: max_length = len(domain_name)

		if domain_name not in domains:
			domains[domain_name] = 1
		else: domains[domain_name] += 1

print(f'SORTED:')
for key in sorted(domains.keys()):
	print(f'{key.rjust(max_length, ' ')}: {domains[key]} {'*'*domains[key]}')
