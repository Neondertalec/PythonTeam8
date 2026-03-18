import re, os
dir_path = os.path.dirname(__file__)

descr = open(dir_path + "/cereals_dataset_description.txt")
namings = re.finditer('(?P<key>\\S)\\s*=\\s*(?P<value>([^;\\d\n](?!=[\\d]))+)', descr.read())

named_groupings = {}

for m in namings:
	print(m.group('key') + ': ' + m.group('value'))
	named_groupings[m.group('key')] = m.group('value')

print(named_groupings)

cereals = open(dir_path + "/cereals2.csv")
cereals.readline()
for line in cereals:
	namings2 = re.finditer('(?P<name>^(.(?![A-Z],))+),(?P<mfr>[A-Z])', line)
	for m in namings2:
		print(named_groupings[m.group('mfr')] + ': ' +  re.sub('_+', ' ', m.group('name')))