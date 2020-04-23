from geopy.geocoders import ArcGIS
nom = ArcGIS()


abha = nom.geocode('King Faisl, Abha, Saudi Arabia', timeout=10000)
print(abha.latitude, abha.longitude)
print(abha.raw)
# print(abha.raw.keys())
print(abha.raw['address'])
print(abha.raw['location'])
print(abha.raw['score'])
print(abha.raw['attributes'])
print(abha.raw['extent'])




lat = input('Enter lat ... ')
long = input('Enter long ... ')
city = nom.reverse(f'{lat}, {long}', timeout=10000)
print(dir(city))
print(city.address)
print(city.latitude)
print(city.longitude)
print(city.raw)
# print(city.raw.keys())
print(city.raw['City'])

