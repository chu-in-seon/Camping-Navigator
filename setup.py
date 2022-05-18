import pandas as pd
import folium

from folium.plugins import MarkerCluster

if __name__ == "__main__":
    camping_sites_csv_data = pd.read_csv('camping_sites_url.csv', encoding='cp949')
    
    # Folium map initialize & display
    m = folium.Map(
    location=[36.344362, 127.948878] # Default location = 36.344362, 127.948878
    , zoom_start=7
    )

    # Marker cluster insert into the folium map
    marker_cluster = MarkerCluster().add_to(m)

    # Add campsites into the map with the detailed information.
    for i in range(camping_sites_csv_data.shape[0]):
        latitude = float(camping_sites_csv_data.iloc[i]['Latitude'])
        longitude = float(camping_sites_csv_data.iloc[i]['Longitude'])
        urlAdd = camping_sites_csv_data.iloc[i]['Homepage']
        if 'nan' == str(urlAdd):
            urlAdd = "https://chuuu-devcamp.tistory.com/"

        folium.Marker(
        [latitude, longitude],
            popup = f'<div style="width:400px">\
                <img width="400px" src="camping_image.jpg"><br>\
                <strong>{camping_sites_csv_data.iloc[i]["Name"]}</strong><br>\
                구분: {camping_sites_csv_data.iloc[i]["Divisions"]}<br>\
                주소: {camping_sites_csv_data.iloc[i]["Address"]}<br>\
                일반사이트: {camping_sites_csv_data.iloc[i]["Normal_site"]}<br>\
                오토캠핑 사이트: {camping_sites_csv_data.iloc[i]["Normal_site"]}<br>\
                글램핑: {camping_sites_csv_data.iloc[i]["Glamping"]}<br>\
                카라반: {camping_sites_csv_data.iloc[i]["Caravan"]}<br>\
                <a href="{urlAdd}">상세 페이지 이동</a>\
                </div>',
            tooltip = 'Click!'
        ).add_to(marker_cluster)

    # Save folium map as html file.
    # m.save('Camping_map.html')
    m.save('index.html')