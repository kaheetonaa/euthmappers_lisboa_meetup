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
result_point=pd.DataFrame(list(collection.find().sort("_id", -1).limit(5)))
result_point['center'][0]
result_point['Coordinate']=gpd.GeoSeries.from_wkt(result_point['center'])
result_point=gpd.GeoDataFrame(result_point,geometry=result_point['Coordinate'])




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
    location=location, zoom_start=zoom, max_zoom=21)
result_point_json = folium.GeoJson(data=result_point)
org_json.add_to(map)


