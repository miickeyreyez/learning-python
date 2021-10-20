import folium
import pandas

volcanoes = pandas.read_csv("volcanoes.txt")

lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
elev = list(volcanoes["ELEV"])

html = """
<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

def get_color(el):
  if el < 1000:
    return 'green'
  elif 1000 <= el <= 3000:
    return 'orange'
  return 'red'
  

for lt, ln, el in zip(lat, lon, elev):
  iframe = folium.IFrame(html=html % str(el), width=200, height=100)
  fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), color='grey', fill_opacity=0.7, icon = folium.Icon(color = get_color(el))))

fgp.add_child(folium.GeoJson(
  data=open('world.json', 'r', encoding='utf-8-sig').read(),
  style_function=lambda x: { 'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red' }
  ))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
