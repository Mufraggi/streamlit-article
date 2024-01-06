import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html

st.set_page_config(
    page_title="Data vise",
    layout="wide"
)

st.title("Data announcement imo")

init_streamlit_comm()


@st.cache_data
def get_df() -> pd.DataFrame:
    return pd.read_csv("donnees_immobilieres.csv")


df = get_df()


@st.cache_resource
def get_pyg_html(df: pd.DataFrame) -> str:
    html = get_streamlit_html(df, spec="./gw0.json", use_kernel_calc=True, debug=False)
    return html


components.html(get_pyg_html(df), width=1300, height=1000, scrolling=True)
