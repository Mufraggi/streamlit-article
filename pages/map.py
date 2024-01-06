import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import folium


@st.cache_data
def get_df() -> pd.DataFrame:
    return pd.read_csv("donnees_immobilieres.csv")


st.set_page_config(page_title="Mapping Demo", page_icon="🌍")

m = folium.Map(location=[43.7, 7.2], zoom_start=10)
data = get_df()

col1, col2 = st.columns(2)

with col1:
    st.header("m² Filter")
    min_area = st.slider("Minimum", min_value=data['floorSize.value'].min(),
                         max_value=data['floorSize.value'].max(), value=data['floorSize.value'].min())
    max_area = st.slider("Maximum", min_value=data['floorSize.value'].min(),
                         max_value=data['floorSize.value'].max(), value=data['floorSize.value'].max())

with col2:
    st.header("Price filter")
    min_price = st.slider("Minimum Price", min_value=data['announce_detail.price'].min(),
                          max_value=data['announce_detail.price'].max(), value=data['announce_detail.price'].min())
    max_price = st.slider("Maximum Price", min_value=data['announce_detail.price'].min(),
                          max_value=data['announce_detail.price'].max(), value=data['announce_detail.price'].max())

filtered_data = data[(data['announce_detail.price'] >= min_price) & (data['announce_detail.price'] <= max_price) &
                     (data['floorSize.value'] >= min_area) & (data['floorSize.value'] <= max_area)]
for index, row in filtered_data.iterrows():
    long = row['geo.longitude']
    lat = row['geo.latitude']
    price = row['announce_detail.price']
    area = row['floorSize.value']
    address = row['address.addressLocality']
    url = row['url']
    msg_popup = f"<b>Price:</b> {price} €<br><b>Area:</b> {area} m²<br><b>Address:</b> {address}<br><a href='{url}' target='_blank'>Link to Listing</a>"
    msg_tooltip = f"Price: {price} €, Area: {area} m²"

    folium.Marker([lat, long], popup=msg_popup, tooltip=msg_tooltip).add_to(m)

st_data = st_folium(m, width=800, height=600)


