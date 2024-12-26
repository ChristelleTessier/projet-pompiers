import streamlit as st

def page3():
    st.markdown("""
    ## Mon premier titre
    ### Sous-titre

    * Élément 1
    * Élément 2

    **Texte en gras** et *texte en italique*

    [Lien vers Streamlit](https://www.streamlit.io)

    <p style='color:red;'>Texte en rouge</p>
    """, unsafe_allow_html=True)