# movies-analytics
# **Phase 2 : Data Analyst - Exploration et Visualisation**  

![](architecturephase.png)

## Introduction

**Objectif : Explorer et analyser les données en interrogeant l’API.**  

🔹 **Analyse Exploratoire des Données (EDA)** :  
- Utiliser le **SDK Python** pour requêter l’API et récupérer les données.  
- Identifier les tendances dans les notes des films.  
- Étudier les genres les plus populaires et les préférences des utilisateurs.  

🔹 **Construction d’une Data App avec Streamlit** :  
- Créer une **application interactive** qui permet de visualiser les tendances du cinéma.  
- Intégrer des **tableaux dynamiques** et des **graphiques interactifs**.  
- Offrir une **recherche avancée** des films en fonction des notes et des genres.  

**Livrables** :  
- Un notebook d'analyse exploratoire interactif.  
- Une **application web Streamlit** connectée à l’API qui présente, de manière interactive, les insights aux parties prenantes.


## Mise en place de l’environnement d’analyse

 nous utilisons **VSCode** comme éditeur principal et organisons chaque phase dans un répertoire Git dédié. Pour cette phase 2 (*Data Analyst – Exploration & Visualisation*), j'ai travailler dans un nouveau projet nommé par exemple `films-analytics` 

### 1. Cloner le dépôt GitHub du projet
git clone https://github.com/imane-el-arrach/films-analytics


## Intégration de l'API dans une application Streamlit
Le fichier `get_movie_poster.py` permet de générer le fichier "output/links_enriched.csv" contenant pour chaque film son lien vers sa page IMDb ainsi que le lien de son image d'affiche.

