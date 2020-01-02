import pandas as pd
import folium

df = pd.read_excel('./서울지역 대학교 위치.xlsx')

seoul_map=folium.Map(location=[37.55,126.98],tiles='Stamen Terrain',zoom_start=18)

for name,lat,lng in zip(df.index,df.위도,df.경도):
    folium.CircleMarker([lat,lng],
                        radius=10,          #원의 반지름
                        color='brown',      #원의 둘레색상
                        fill=True,
                        fill_color='coral', #원을 채우는 색
                        fill_opacity=0.7,   #투명도
                        popup=name
    ).add_to(seoul_map)

seoul_map.save('./seoul_colleges2.html')
