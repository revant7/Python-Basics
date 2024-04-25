import webbrowser as web
from geopy.geocoders import Nominatim
import folium

def geolocation_finder():
  entrd_loc = input("Enter A Location : ")
  location = Nominatim(user_agent="GetLoc")
  get_loc = location.geocode(entrd_loc)
  global lat,long,address
  lat = get_loc.latitude
  long = get_loc.longitude
  address = get_loc.address

def map_creator():
  map1 = folium.Map(location = [lat,long])
  folium.Marker(location = [lat,long],popup = address).add_to(map1)
  map1.save("NewMap.html") 
  web.open("NewMap.html") 

geolocation_finder()
map_creator()




