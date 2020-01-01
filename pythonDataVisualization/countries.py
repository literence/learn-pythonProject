from pygal_maps_world.i18n import COUNTRIES

#按字母排序输出国别码和对应的国家
for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])