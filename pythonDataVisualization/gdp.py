import csv
from country_codes import get_country_code
import pygal_maps_world.maps

# 将数据加载到一个列表中
filename = "gdp.csv"


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    gdp={}
    for row in reader:
        try:
            country_name=row[0]
            value=int(row[62])
        except ValueError:
            print("Error-"+country_name)
        else:
            code = get_country_code(country_name)
            if code:
                gdp[code]=value

    wm = pygal_maps_world.maps.World()
    wm.add("gdp",gdp)

    wm.render_to_file('world_gdp.svg')


