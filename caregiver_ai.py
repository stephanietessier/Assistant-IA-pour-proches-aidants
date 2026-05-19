
"""
Assistant IA pour proches aidants.

Prototype éducatif :
- ne remplace pas un avis médical, social ou juridique ;
- ne stocke pas de données sensibles ;
- aide à prioriser, organiser et orienter vers des ressources.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    aidants = pd.read_csv("data/aidants_fictifs.csv")
    taches = pd.read_csv("data/taches_fictives.csv")
    ressources = pd.read_csv("data/ressources_fictives.csv")
    journal = pd.read_csv("data/journal_bien_etre_fictif.csv")
    return aidants, taches, ressources, journal


def fatigue_risk(niveau_fatigue, heures_aide_semaine, soutien_famille):
    score = niveau_fatigue * 1.5 + heures_aide_semaine / 5
    if str(soutien_famille).lower() == "faible":
        score += 3
    elif str(soutien_famille).lower() == "moyen":
        score += 1

    if score >= 18:
        return "élevé", "Risque d'épuisement élevé : chercher du répit et de l'aide humaine rapidement."
    if score >= 11:
        return "modéré", "Risque modéré : réduire les tâches non essentielles et demander du soutien."
    return "faible", "Risque faible à modéré : maintenir les routines de repos et de soutien."


def prioritize_tasks(taches):
    priority_map = {"haute": 3, "moyenne": 2, "basse": 1}
    df = taches.copy()
    df["score_priorite"] = df["priorite"].map(priority_map).fillna(1)
    return df.sort_values(["score_priorite", "categorie"], ascending=[False, True])


def recommend_resources(besoin, ressources, top_n=3):
    texts = ressources["type"].astype(str) + " " + ressources["description"].astype(str) + " " + ressources["ville"].astype(str)
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(texts)
    query = vectorizer.transform([besoin])
    scores = cosine_similarity(query, matrix).flatten()

    result = ressources.copy()
    result["score_pertinence"] = scores
    return result.sort_values("score_pertinence", ascending=False).head(top_n)


def daily_suggestions(stress, sommeil_heures):
    suggestions = []
    if stress >= 8:
        suggestions.append("Faire une pause courte maintenant, respirer, puis contacter une personne de confiance.")
    if sommeil_heures < 6:
        suggestions.append("Alléger la journée si possible et déplacer une tâche non urgente.")
    if not suggestions:
        suggestions.append("Préserver une pause personnelle aujourd'hui, même courte.")
    suggestions.append("Noter une seule demande d'aide concrète à faire à l'entourage.")
    return suggestions
