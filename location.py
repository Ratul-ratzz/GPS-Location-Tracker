import phonenumbers

from mynumber import number

from phonenumbers import geocoder

import folium

rnumber=phonenumbers.parse(number)

ur_location= geocoder.description_for_number(rnumber,"en")
print(ur_location)


# service provider
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

#lati and longitude

key='17271ee3f1734b01904367c4b3cf4ad8'

from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode (key)

query=str(ur_location)
results=geocoder.geocode(query)
# print(results)

#lat and longi results
lat=results[0]['geometry']['lat']

lng=results[0]['geometry']['lng']

print(lat,lng)

#use of folium  
myMap= folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng],popup=ur_location).add_to(myMap)

##save map in html file
myMap.save("MyLocation.html")