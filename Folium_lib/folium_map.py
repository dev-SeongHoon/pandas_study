import folium
"""
seoul_map=folium.Map(location=[37.55,126.98],zoom_start=12)

Daegu_map=folium.Map(location=[35.877430, 128.629142],zoom_start=12)
"""
Daegu_map2=folium.Map(location=[35.877430, 128.629142],tiles='Stamen Terrain')
Daegu_map3=folium.Map(location=[35.877430, 128.629142],tiles='Stamen Toner')
#Daegu_map.save('./Daegu.html')
Daegu_map2.save('./Daegu2.html')
Daegu_map3.save('./Daegu3.html')