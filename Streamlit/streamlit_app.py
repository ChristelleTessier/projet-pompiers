import streamlit as st
import pandas as pd
import numpy as np

# Générer des données aléatoires
df = pd.DataFrame(np.random.randn(1000, 2), columns=['x', 'y'])

# Titre de l'application
st.title('Visualisation de données avec Streamlit')

# Choix du type de graphique
chart_type = st.selectbox(
    'Choisissez un type de graphique',
    ('line chart', 'area chart', 'bar chart')
)

# Créer le graphique
if chart_type == 'line chart':
    st.line_chart(df)
elif chart_type == 'area chart':
    st.area_chart(df)
else:
    st.bar_chart(df)