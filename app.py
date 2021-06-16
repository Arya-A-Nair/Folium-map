import folium
from folium.map import FeatureGroup
import pandas
fg=folium.FeatureGroup(name="Volcanoes")
fg2=folium.FeatureGroup(name="Population")

df=pandas.read_csv("Volcanoes.txt")
latitude=list(df['LAT'])
longitude=list(df['LON'])
elev=list(df['ELEV'])
type=list(df['TYPE'])
status=list(df['STATUS'])

def colour_gen(elevation):
    
    if elevation>1000 and elevation<2000:
        return 'red'
    elif elevation>2000 and elevation<3000:
        return 'cadetblue'
    else:
        return 'blue'

map=folium.Map(location=[38.58,-99.09] ,zoom_start=6, tiles="Stamen Terrain")
#fg2=folium.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read()))

latitude=list(df['LAT'])
longitude=list(df['LON'])

for lat,lon,e,t,s in zip(latitude,longitude,elev,type,status):
    fg.add_child(folium.Marker(location=[lat,lon], popup=f"Elevation:{e}m \n Type:{t} \nStatus:{s}", icon=folium.Icon(colour_gen(e))))
   
fg2.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function=lambda x:{
   'fillColor':'Green'
   if x['properties']['POP2005']<=10000000
   else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'
}))
    
#fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))
map.add_child(fg2)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("index.html")
