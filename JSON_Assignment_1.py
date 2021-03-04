import json

infile = open("US_fires_9_1.json", 'r')
outfile = open("readable_fire_data1.json", 'w')

fire_data = json.load(infile)

json.dump(fire_data,outfile, indent=4)

datalons, datalats, databright = [], [], []
for x in fire_data:
    lon = x["logitude"]
    lat = x["latitude"]
    bright = x["brightness"]
    if bright > 450:
        databright.append(bright)
        datalons.append(lon)
        datalats.append(lat)

list_of_fire = fire_data['features']

brightness,longitude,latitude = [],[],[]

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [Scattergeo(longitude=lons, latitude=lats)]

my_layout = Layout(title="US Fires from 9-1-2020 to 9-13-2020")

fig = {"data":data, 'layout':my_layout}

offline.plot(fig,filename='US_fires_9_1.html')

print (fires_data['features'][0]['properties']['brightness'])


