import streamlit as st
import pandas as pd
import numpy as np
import os

def page1():
    st.title("Présentation des données")
    st.markdown("""
    Les données utilisées proviennent d'une base de dataset London Datastore.
        
    Les données sont réparties en fonction d'un regroupement d'année.

    La description des variables est donnée [ici](https://docs.google.com/spreadsheets/d/1wPR7s0LJfrpkzEoixS6dLpxL19sDMqqu/edit?gid=476720423#gid=476720423)        
    """)
    
    # Fonction pour afficher le contenu de chaque page
    def show_incident_page():
        st.markdown("""
        Le premier jeu de données fourni contient les détails de chaque incident traité depuis janvier 2009.
         Des informations sont fournies sur la date et le lieu de l'incident ainsi que sur le type d'incident traité. 
         Les données peuvent être récupérées sur London DataStore : [London Fire Brigade Incident Records](https://data.london.gov.uk/dataset/london-fire-brigade-incident-records).
         Elles sont stockées dans deux fichiers :

        *   LFB Incident data from 2009 - 2017.xlsx
        *   LFB Incident data from 2018 onwards.csv
        """)
        data = pd.read_excel("Data/info_incident.xlsx", header=1)
        # Afficher le tableau
        st.dataframe(data)

    def show_mobilisation_page():
        st.markdown("""
        Le second jeu de données contient les détails de chaque camion de pompiers envoyé sur les lieux d'un incident depuis janvier 2009.
         Des informations sont fournies sur l'appareil mobilisé, son lieu de déploiement et les heures d'arrivée sur les lieux de l'incident.
         Les données peuvent être récupérées sur London DataStore : [London Fire Brigade Mobilisation Records](https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records).
         Elles sont stockées dans trois fichiers :

        *   LFB Mobilisation data from January 2009 - 2014.xlsx
        *   LFB Mobilisation data from 2015 - 2020.xlsx
        *   LFB Mobilisation data from 2021 - 2024 .xlsx
        """)
        data = pd.read_excel("Data/info_mobilisation.xlsx", header=1)
        # Afficher le tableau
        st.dataframe(data)

    def show_dataintermediaire_page():
        st.markdown("""
        Pour construire le jeu de données intermédiaire, regroupant les informations incidents 
        et les informations mobilisation nous avons utilisé des jointures en lignes et en colonnes.
        Nous avons garder uniquement les incident/mobilisation réalisés après le 9 janvier 2014.
        Nous avons pris pour critères de jointure :

        * même IncidentNumber
        * NumPumpsAttending dans incident = max(PumpOrder) dans mobilisation
                    
        A ce stade nous avons concervé uniquement les informations connues a priori.
        """)
        data = pd.read_excel("Data/info_incident_mobilisation.xlsx", header=1)
        # Afficher le tableau
        st.dataframe(data)
        

        

        

    # Créer la barre de navigation horizontale avec des onglets
    tab1, tab2, tab3 = st.tabs(["Incident", "Mobilisation","Jeu de données intermédiaire"])

    # Afficher le contenu en fonction de l'onglet sélectionné
    with tab1:
        show_incident_page()
    with tab2:
        show_mobilisation_page()
    with tab3 :
        show_dataintermediaire_page()


