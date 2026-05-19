
import streamlit as st
import pandas as pd
from src.caregiver_ai import (
    load_data,
    fatigue_risk,
    prioritize_tasks,
    recommend_resources,
    daily_suggestions,
)

st.set_page_config(
    page_title="Assistant IA pour proches aidants",
    page_icon="🤲",
    layout="wide"
)

st.title("🤲 Assistant IA pour proches aidants")
st.caption("Prototype progressiste pour organiser les soins, réduire la charge mentale et prévenir l'épuisement.")

st.warning(
    "Ce prototype ne remplace pas un avis médical, psychologique, social ou juridique. "
    "Il sert à organiser l'information et à orienter vers des ressources."
)

aidants, taches, ressources, journal = load_data()

tab1, tab2, tab3, tab4 = st.tabs([
    "🧭 Tableau de bord",
    "✅ Tâches prioritaires",
    "💚 Bien-être",
    "📍 Ressources"
])

with tab1:
    st.subheader("Profil aidant fictif")
    aidant = st.selectbox("Choisir un profil", aidants["prenom"].tolist())
    row = aidants[aidants["prenom"] == aidant].iloc[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("Heures d'aide/semaine", int(row["heures_aide_semaine"]))
    col2.metric("Fatigue /10", int(row["niveau_fatigue"]))
    col3.metric("Soutien familial", row["soutien_famille"])

    level, advice = fatigue_risk(row["niveau_fatigue"], row["heures_aide_semaine"], row["soutien_famille"])
    st.write("**Niveau de risque estimé :**", level)
    st.info(advice)

with tab2:
    st.subheader("Priorisation des tâches")
    st.write("L'IA classe les tâches selon leur priorité déclarée.")
    st.dataframe(prioritize_tasks(taches), use_container_width=True)

with tab3:
    st.subheader("Suggestions de bien-être")
    stress = st.slider("Stress aujourd'hui /10", 1, 10, 7)
    sommeil = st.slider("Sommeil cette nuit", 0, 12, 6)

    for suggestion in daily_suggestions(stress, sommeil):
        st.checkbox(suggestion)

    st.subheader("Journal fictif")
    st.dataframe(journal, use_container_width=True)

with tab4:
    st.subheader("Rechercher une ressource")
    besoin = st.text_input("Besoin", "répit écoute transport rendez-vous")
    recs = recommend_resources(besoin, ressources)
    st.dataframe(recs, use_container_width=True)

    st.subheader("Toutes les ressources fictives")
    st.dataframe(ressources, use_container_width=True)
