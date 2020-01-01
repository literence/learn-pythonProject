import json
from country_codes import get_country_code
import pygal_maps_world.maps
import matplotlib.pyplot as plt

# 设置样式
from pygal.style import RotateStyle
#加亮颜色主题
from pygal.style import LightColorizedStyle
#设置颜色和基本样式
from pygal.style import LightColorizedStyle, RotateStyle

#将数据加载到一个列表中
filename = "population_data.json"

with open(filename) as f:
    pop_data = json.load(f)

    cc_populations = {}

    #打印每个国家 2010 年的人口数量
    for pop_dict in pop_data:
        if pop_dict["Year"] == "2010":
            country_name = pop_dict["Country Name"]
            population = int(float(pop_dict["Value"]))
            code = get_country_code(country_name)
            if code:
                #print(code + ":" + str(population))
                cc_populations[code] = population
            else:
                print("ERROR - " + country_name)

    #根据人口数量分成三组
    cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
    for cc,pop in cc_populations.items():
        if pop<10000000:
            cc_pops_1[cc] = pop
        elif pop<10000000:
            cc_pops_2[cc] = pop
        else:
            cc_pops_3[cc] = pop

   # wm_style = RotateStyle('#336699')

    #加亮颜色主题
    #wm_style = LightColorizedStyle

    wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)

    wm = pygal_maps_world.maps.World(style = wm_style)
    wm.title = 'World Population in 2010, by Country'
    #wm.add("2010",cc_populations)
    wm.add("0-10m",cc_pops_1)
    wm.add("10m-1bn",cc_pops_2)
    wm.add(">1bn",cc_pops_3)

    wm.render_to_file("world_population.svg")

    ccs,pops=[],[]
    for cc,pop in cc_populations.items():
        ccs.append(cc)
        pops.append(pop)

    print(ccs)
    print(pops)
    plt.plot(ccs,pops)
    plt.show()


