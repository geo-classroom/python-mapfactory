#Import the folium library
import folium
from folium.plugins import BeautifyIcon

#Import the OS python library
import geopandas as gpd
#import json
import json



#Create a map object, set starting coordinates and the starting zoom level
m = folium.Map(location=[39.8283,-98.5795],
           zoom_start=4,
           tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
           attr='Tiles &cop; Esri &mdash; Source: Esri, i-cubed, USDA, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community')


#Import the US states data in the json format
geojson = r"C:\Users\riell\OneDrive\Desktop\Folium_Map\data\states_provinces.json"

#Render the data on the map through the folium GeoJson request
folium.GeoJson(
    geojson,
    name= 'geojson'
).add_to(m)


#The goal is to create a quiz type map of a few US states. 
#When a user hovers over a marker, a unique tooltip will give a hint about what state it is

#Create map markers along with popups of information when the marker is clicked
#Creat Star marker
icon_star = BeautifyIcon(
    icon= 'star',
    inner_icon_style='color:white; font-size:50px;',
    background_color='transparent',
    border_color='transparent'
)

#For state of California
folium.Marker([38.5816, -121.4944], 
popup='<strong>State of California!: This marker is in Sacramento</strong>',
tooltip= 'Hint: home to Holywood',
icon=folium.Icon(icon= 'star')).add_to(m)

#For state of Oregon
folium.Marker([42.9729, -120.7778], 
popup='<strong>State of Oregon: This marker is in Summer Lake</strong>', 
tooltip= 'Hint: home to Portland',
icon=folium.Icon(icon='star')).add_to(m)

#For state of Washington
folium.Marker([47.4235, -120.3103], 
popup='<strong>State of Washington: This marker is in Wenatchee</strong>', 
tooltip= 'Hint: home to Seattle',
icon=folium.Icon(icon='star')).add_to(m)

#For state of Nevada
folium.Marker([39.5125, -115.9608], 
popup='<strong>State of Nevada: This marker is in Eureka</strong>', 
tooltip= 'Hint: home to Vegas',
icon=folium.Icon(icon='star')).add_to(m)

#For state of Arizona
folium.Marker([33.4484, -112.0740], 
popup='<strong>State of Arizona: This marker is in Phoenix</strong>', 
tooltip= 'Hint: home to Phoenix',
icon=folium.Icon(icon='star')).add_to(m)

#For state of Utah
folium.Marker([37.9221, -111.4395], 
popup='<strong>State of Utah: This marker is in Boulder</strong>', 
tooltip= 'Hint: home to Salt Lake city',
icon=folium.Icon(icon='star')).add_to(m)

#For state of New Mexico
folium.Marker([33.3673, -105.6588], 
popup='<strong>State of New Mexico: This marker is in Ruidoso</strong>', 
tooltip= 'Hint: home to Albuquerque',
icon=folium.Icon(icon='star')).add_to(m)

#For state of Texas
folium.Marker([29.4252, -98.4946], 
popup='<strong>State of Texas: This marker is in San Antonio</strong>', 
tooltip= 'Hint: home to Fort Worth',
icon=folium.Icon(icon='star')).add_to(m)

#For state of Louisiana
folium.Marker([30.2241, -92.0198], 
popup='<strong>State of Louisiana: This marker is in Lafayette</strong>', 
tooltip= 'Hint: home to Lafayette',
icon=folium.Icon(icon='star')).add_to(m)

#For state of Mississippi
folium.Marker([32.2988, -90.1848], 
popup='<strong>State of Mississippi: This marker is Jackson</strong>', 
tooltip= 'Hint: home to Memphis',
icon=folium.Icon(icon='star')).add_to(m)

#For state of Alabama
folium.Marker([32.3792, -86.3077], 
popup='<strong>State of Alabama: This marker is Montgomery</strong>', 
tooltip= 'Hint: home to Birmingham',
icon=folium.Icon(icon='star')).add_to(m)

#For state of Georgia
folium.Marker([32.8407, -83.6324], 
popup='<strong>State of Georgia: This marker is Macon</strong>', 
tooltip= 'Hint: home to Atlanta',
icon=folium.Icon(icon='star')).add_to(m)

#For state of Florida 
folium.Marker([28.5384, -81.3789], 
popup='<strong>State of Florida: This marker is Orlando</strong>', 
tooltip= 'Hint: home to Tampa',
icon=folium.Icon(icon='star')).add_to(m)


#Generate the map page
m.save("map.html")

