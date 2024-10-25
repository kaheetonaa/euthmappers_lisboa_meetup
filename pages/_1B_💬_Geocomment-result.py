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
if st.button('Refresh'):
    #This would empty everything inside the container
    st.empty()

map = folium.Map(
    location=[0,0], zoom_start=5, max_zoom=21)
for _, r in result_polygon.iterrows():
    # Without simplifying the representation of each borough,
    # the map might not be displayed
    sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {"fillColor": "red","stroke-color":"red"})
    folium.Popup(r["comment"]).add_to(geo_j)
    geo_j.add_to(map)

map.fit_bounds(map.get_bounds(), padding=(30, 30))

st_map= st_folium(
    map,
    width='100%',
    height=600,
    returned_objects=[]
)



