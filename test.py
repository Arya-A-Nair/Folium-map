import folium
import pandas as pd
data = pd.read_csv("Volcanoes.txt")
lat = data["LAT"].to_list()
lon = data["LON"].to_list()
elev = data["ELEV"].to_list()

def color_marker(elevation):
   if elevation < 1000:
      return "green"
   elif 1000 <= elevation < 3000:
      return "orange"
   else:
      return "red"


map = folium.Map(location = [38, -99], zoom_start = 6, tiles = "OpenStreetMap" )
fg1 = folium.FeatureGroup(name = "My Map") #FeatureGroup acts as a layer.
fg2 = folium.FeatureGroup(name='foo') 


for lt, ln, elv in zip(lat, lon, elev):
   fg1.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup="Elevation: %s m" %elv, fill_color=color_marker(elv), color="grey", fill=True, fill_opacity=0.7))
   
fg2.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function=lambda x:{
   'fillColor':'Green'
   if x['properties']['POP2005']<=10000000
   else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'
}))

map.add_child(fg2)
map.add_child(fg1)
map.add_child(folium.LayerControl())
map.save("Map test.html")