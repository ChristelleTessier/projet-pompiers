import streamlit as st

def page1():
    st.title("Présentation des données")
    st.write("Les données utilisées proviennent d'une base de dataset \"London Datastore\".Nous avons utilisé deux bases de données différentes :")
    st.markdown("""
        * London Fire Brigade Incident Records (lien)
        * London Fire Brigade Mobilisation Records (lien)
        """)

