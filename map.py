import geopandas as gpd
import streamlit as st
import leafmap.foliumap as leafmap
import folium
import os
import uuid
import tempfile

st.set_page_config(page_title="KML显示工具", layout="centered")
data = st.file_uploader("上传要显示的KML文件", type=["kml"])

def save_uploaded_file(file_content, file_name):
    _, file_extension = os.path.splitext(file_name)
    file_id = str(uuid.uuid4())
    file_path = os.path.join(tempfile.gettempdir(), f"{file_id}{file_extension}")

    with open(file_path, "wb") as file:
        file.write(file_content.getbuffer())

    return file_path

if data is not None:

    width = 700
    height = 500

    file_path = save_uploaded_file(data, data.name)
    layer_name = os.path.splitext(data.name)[0]

    if file_path.lower().endswith(".kml"):
        gpd.io.file.fiona.drvsupport.supported_drivers["KML"] = "rw"
        gdf = gpd.read_file(file_path, driver="KML")

    #获取KML文件中心点坐标
    lon = gdf.centroid.iloc[0].x
    lat = gdf.centroid.iloc[0].y

    #以中心坐标确定地图显示范围
    m = leafmap.Map(center=(lat, lon), draw_export=True)

    basemaps = {
            'Esri Satellite': folium.TileLayer(
                tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                attr = 'Esri',
                name = 'Esri Satellite',
                overlay = True,
                control = True
            )
        }

    choose = st.selectbox("是否要加载卫星地图",("是","否"))

    if choose == "是":
        basemaps['Esri Satellite'].add_to(m)
        m.add_gdf(gdf, layer_name=layer_name)
        m.to_streamlit(width, height)

    else:
        m.add_gdf(gdf, layer_name=layer_name)
        m.to_streamlit(width, height)