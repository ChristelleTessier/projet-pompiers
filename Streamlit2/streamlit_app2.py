import streamlit as st
import folium
import pandas as pd
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

@st.cache_data
def charger_donnees():
    url = "https://drive.google.com/file/d/1-BjFCk7Q5b3hAn_oWEvuB1wa0LVJ4d8B/export?format=csv"
    df = pd.read_csv(url, low_memory=False)

    url = "https://drive.google.com/file/d/1-9jQORrkPiSvLwxLwBuX9YqCKq98_yJw/export?format=csv"
    df2 = pd.read_csv(url, low_memory=False)

    df_merged = pd.merge(df, df2, on='IncidentNumber', how='inner')
    df_2024 = df_merged[df_merged['CalYear_x'] == 2024]
    df_2024 = df_2024[['IncGeo_BoroughName', 'ResponseTimeBinary', 'inner', 'Latitude', 'Longitude']]

    url = "https://drive.google.com/file/d/1p3GJaRpEvPZzRP3PbjxB4zdQpVyNnHnG/export?format=csv"
    station = pd.read_csv(url, low_memory=False)
    station = station[["Station name", "Latitude", "Longitude"]]
    station["Station name"] = station["Station name"].str.upper()

    return df_2024, station

# Charger les données en cache
df_2024, station = charger_donnees()

st.title("Carte Interactive des Incidents 🚒")
st.sidebar.header("Filtrer par Caserne")

# Construire la liste des casernes sans l'option "Toutes"
casernes = sorted(df_2024["IncGeo_BoroughName"].unique().tolist())

# Sélection de la caserne (la première est sélectionnée par défaut)
choix_caserne = st.sidebar.selectbox("Choisissez une caserne :", casernes, index=0)

# Filtrage pour la caserne sélectionnée
df_filtered = df_2024[df_2024["IncGeo_BoroughName"] == choix_caserne]

# Récupération de la position de la station correspondante
station_caserne = station[station["Station name"] == choix_caserne]


# Création de la carte centrée sur la moyenne des points filtrés
m = folium.Map(location=[df_filtered["Latitude"].mean(), df_filtered["Longitude"].mean()], zoom_start=12)

# Utiliser MarkerCluster pour optimiser l'affichage
marker_cluster = MarkerCluster().add_to(m)
for _, row in df_filtered.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=row["IncGeo_BoroughName"],
        tooltip="Cliquez pour voir"
    ).add_to(marker_cluster)

# Vérifier si la caserne est trouvée
if station_caserne.empty:
    st.warning(f"⚠️ Attention : La caserne '{choix_caserne}' n'a pas été trouvée dans la base des stations.")
else:
    # Ajouter la caserne en noir
    folium.Marker(
        location=[station_caserne["Latitude"].values[0], station_caserne["Longitude"].values[0]],
        popup=f"Caserne : {choix_caserne}",
        tooltip="Caserne",
        icon=folium.Icon(color="black", icon="home")
    ).add_to(m)


# Ajouter la caserne en noir
if not station_caserne.empty:
    folium.Marker(
        location=[station_caserne["Latitude"], station_caserne["Longitude"]],
        popup=f"Caserne : {choix_caserne}",
        tooltip="Caserne",
        icon=folium.Icon(color="black", icon="home")
    ).add_to(m)


# Afficher la carte dans Streamlit
folium_static(m)
