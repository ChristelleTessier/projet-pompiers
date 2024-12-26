import streamlit as st
import pandas as pd

from page1 import page1
from page2 import page2
from page3 import page3
from page4 import page4
from page5 import page5
from page6 import page6
from page_intro import page_intro

# Charger les pages
if 'page' not in st.session_state:
    st.session_state.page = page_intro

# Sidebar
pages = {
    "Presentation":page_intro,
    "Presentation des données": page1,
    "Visualisation des données": page2,
    "Prétraitement des données": page3,
    "Modélisation 1 - prédiction variable continue": page4,
    "Modélisation 2 - prédiction variable discrète": page5,
    "Conclusion et prespective": page6
}

selected_page = st.sidebar.selectbox("Menu", pages.keys())

# Layout with Columns
col1, col2, col3 = st.columns([1, 6, 1])


st.sidebar.write("""Auteurs :
* Anne DUBOIS
* Christelle TESSIER
* Hao LA
""")

# Call the selected page function
pages[selected_page]()