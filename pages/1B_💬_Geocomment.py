from streamlit_folium import st_folium
import folium
import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
<style>
#element-container {
border:1px solid black;
}
</style>
""",
    unsafe_allow_html=True,
)


map = folium.Map(zoom_start=5, max_zoom=21)

st_folium(
            map,
            width="100%",
            height=600
        )


