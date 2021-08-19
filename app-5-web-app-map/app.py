import folium
import pandas

volcanoes = pandas.read_csv("volcanoes.txt")

lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My map")

for lt, ln in zip(lat, lon):
  fg.add_child(folium.Marker(location=[lt,ln], popup="Wizeline MXC", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
