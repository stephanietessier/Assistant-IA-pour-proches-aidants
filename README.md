
# 🤲 Assistant IA pour proches aidants

Projet progressiste d'IA pour aider les proches aidants à organiser les soins, réduire la charge mentale, repérer les risques d'épuisement et trouver des ressources.

## Fonctionnalités

- Tableau de bord aidant.
- Estimation simple du risque d'épuisement.
- Priorisation des tâches.
- Journal fictif de bien-être.
- Recommandation de ressources par besoin.
- Application Streamlit.
- Notebook Google Colab.
- Données fictives modifiables.

## Avertissement

Ce projet est éducatif.  
Il ne remplace pas un avis médical, psychologique, social ou juridique.

## Structure

```text
assistant_ia_proches_aidants/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── data/
│   ├── aidants_fictifs.csv
│   ├── taches_fictives.csv
│   ├── ressources_fictives.csv
│   └── journal_bien_etre_fictif.csv
├── src/
│   └── caregiver_ai.py
└── notebooks/
    └── Assistant_IA_proches_aidants_Colab.ipynb
```

## Lancer localement

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Utiliser dans Google Colab

1. Ouvrir Google Colab.
2. Importer `notebooks/Assistant_IA_proches_aidants_Colab.ipynb`.
3. Exécuter les cellules.

## Idées d'amélioration

- Ajouter un calendrier de rendez-vous.
- Ajouter des rappels locaux.
- Ajouter un mode hors ligne.
- Ajouter une exportation PDF du plan de soins.
- Ajouter une base de ressources réelles par région.
- Ajouter un système de partage familial sécurisé.
- Ajouter une interface mobile simple.
- Ajouter une gestion stricte de la confidentialité.

## Licence

MIT.
