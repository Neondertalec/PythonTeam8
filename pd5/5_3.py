import requests, json
lat = None
lon = None
while lat == None:
	try: lat = float(input("lat: "))
	except:pass
while lon == None:
	try: lon = float(input("lon: "))
	except:pass


resp = requests.get(f"https://nominatim.openstreetmap.org/reverse", params={
	'lat': lat,
	'lon': lon,
	'format': "json"
}, headers={
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
})

def deepFind(json_data, *paths, default = "", validate = lambda data: bool(data.strip())):
	for path in paths:
		if isinstance(path, str):
			if path in json_data and validate(json_data[path]):
				return json_data[path]
		else:
			temp = json_data
			for pathed in path:
				if hasattr(temp, '__iter__') and pathed in temp:
					temp = temp[pathed]
				else: break
			else:
				if validate(temp):
					return temp
	
	return default

resp.raise_for_status()
json_data = resp.json()
print(json_data)
print('Name of the place: ' + deepFind(json_data, 'name', ['address', 'isolated_dwelling'], ['address', 'suburb'], ['address', 'village'], default='unset'))
print('Type: ' + deepFind(json_data, 'type', 'class', default='unset', validate=lambda data: bool(data.strip()) and data != 'yes' ))
print('House number: ' + deepFind(json_data, ['address', 'house_number'], default='unset'))
print('Street name: ' + deepFind(json_data, ['address', 'road'], ['address', 'district'], default='unset'))
print('City: ' + deepFind(json_data, ['address', 'city'], ['address', 'civil_parish'], ['address', 'municipality'], ['address', 'state'], default='unset'))
print('Postcode: ' + deepFind(json_data, ['address', 'postcode'], default='unset'))
print('Country name: ' + deepFind(json_data, ['address', 'country'], default='unset'))
print('Country code: ' + deepFind(json_data, ['address', 'country_code'], default='unset'))