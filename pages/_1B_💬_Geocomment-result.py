import streamlit as st
from pymongo import MongoClient
import pandas as pd
import geopandas as gpd
from shapely import wkt
import folium
from folium.features import GeoJsonPopup
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

@st.cache_resource
def init_connection():
    return MongoClient("mongodb+srv://kuquanghuy:quanghuy123456@cluster0.6mzug.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

client = init_connection()

db=client['EuthMappers_Geocomment']
collection=db['EuthMappers_Geocomment']
result_polygon=pd.DataFrame(list(collection.find().sort("_id", -1).limit(5)))

result_polygon['Polygon']=gpd.GeoSeries.from_wkt(result_polygon['bounds'])
result_polygon=gpd.GeoDataFrame(result_polygon,geometry=result_polygon['Polygon']).set_crs(epsg=4326)
result_polygon



st.markdown("""

<style>
    @import url('https://fonts.googleapis.com/css?family=Comfortaa:wght@100&display=swap'); 

    html, body, h1,h2,h3,p{
        font-family: 'Comfortaa', sans-serif; 
        
    }
    div[data-baseweb="select"] > div {
    background-color: #62cbec;
            color:white;
            font-family: 'Comfortaa', sans-serif;
    }

    body{
        font-size: 18px;
    }

    [role=radiogroup]{
        gap: 1rem;
    }
    h1 {
        text-align: center
    }
    h2 {
        text-align: center
    }
    h3 {
        text-align: center
    }
    
    div[data-testid='stAppViewBlockContainer']{
        background-color: #62cbec10;
    }
            .center {
    display: block;
    margin-left: auto;
    margin-right: auto;
        width:200px;
}
</style>
""", unsafe_allow_html=True)


map = folium.Map(
    location=[0,0], zoom_start=5, max_zoom=21)
result_polygon_json = folium.GeoJson(data=result_polygon)
org_json.add_to(map)

st_map= st_folium(
    map,
    width='100%',
    height=600
)


