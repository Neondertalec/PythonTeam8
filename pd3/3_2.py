import re, os
dir_path = os.path.dirname(__file__)

cereals = open(dir_path + "/cereals2.csv")
title = cereals.readline()

title_list = re.findall('\\w+', title)
# print(title_list)

rating_index = title_list.index('rating')
type_index = title_list.index('type')

# print(type_index)
# print(rating_index)

hot_min = None
hot_min_name = ""
hot_max = None
hot_max_name = ""
hot_avg = 0
hot_cnt = 0

cold_min = None
cold_min_name = ""
cold_max = None
cold_max_name = ""
cold_avg = 0
cold_cnt = 0

for line in cereals:
	full_parse = re.findall('^((?:.(?![A-Z],))+),([A-Z]),([A-Z]),([\\d.]*),([\\d.]*),([\\d.]*),([\\d.]*),([\\d.]*),([\\d.]*),([\\d.]*),([\\d.]*),([\\d.]*),([\\d.]*),([\\d.]*),([\\d.]*),([\\d.]*)', line)
	for m in full_parse:
		if m[type_index] == 'H':
			hot_cnt += 1
			if hot_min == None or hot_min > float(m[rating_index]):
				hot_min = float(m[rating_index])
				hot_min_name = re.sub('_+', ' ', m[0])

			if hot_max == None or hot_max < float(m[rating_index]):
				hot_max = float(m[rating_index])
				hot_max_name = re.sub('_+', ' ', m[0])

			hot_avg += float(m[rating_index])
		else:
			cold_cnt += 1
			if cold_min == None or cold_min > float(m[rating_index]):
				cold_min = float(m[rating_index])
				cold_min_name = re.sub('_+', ' ', m[0])

			if cold_max == None or cold_max < float(m[rating_index]):
				cold_max = float(m[rating_index])
				cold_max_name = re.sub('_+', ' ', m[0])

			cold_avg += float(m[rating_index])

hot_avg /= hot_cnt
cold_avg /= cold_cnt

print(f"""
hot_min: {hot_min}
hot_min_name: {hot_min_name}
hot_max: {hot_max}
hot_max_name: {hot_max_name}
hot_avg: {hot_avg}
hot_cnt: {hot_cnt}

cold_min: {cold_min}
cold_min_name: {cold_min_name}
cold_max: {cold_max}
cold_max_name: {cold_max_name}
cold_avg: {cold_avg}
cold_cnt: {cold_cnt}
""")