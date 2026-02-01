import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os
from utils import load_csv_data
st.markdown(
    """
    <style>
        .block-container {
            padding-left: 3rem;
            padding-right: 3rem;
            padding-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Définition du dossier de sortie
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

st.title("🎬 Analyse Générale des Films et Évaluations")


# Fonction cache pour charger les fichiers parquet
# @st.cache_data
# def load_parquet_data(file_name):
#     file_path = OUTPUT_DIR / file_name
#     return pd.read_parquet(file_path)

# Chargement des données
genre_df = load_csv_data("genre_df.csv")


#chargement des datasets
genre_rating_stats = load_csv_data("genre_rating_stats.csv")
movies_by_year = load_csv_data("movies_by_year.csv")
top_movies = load_csv_data("top_movies_by_ratings.csv")
ratings_df = load_csv_data("ratings.csv")

# Graphique 1 : Top 10 genres par nombre de films
fig_genre = px.bar(
    genre_df,
    x="count",
    y="genre",
    title="Top 10 genres par nombre de films",
    labels={"genre": "Genre", "count": "Nombre de films"},
    color="count",
    color_continuous_scale="viridis",
    orientation='h'
)
fig_genre.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=350
)

# Graphique 2 : Top 10 genres par nombre d’évaluations et note moyenne
top10_genre_stats = genre_rating_stats.sort_values("rating_count", ascending=False).head(10)
fig_genre_rating = px.bar(
    top10_genre_stats,
    x="rating_count",
    y="genre",
    orientation="h",
    color="avg_rating",
    color_continuous_scale="viridis",
    title="Top 10 genres par nombre d’évaluations et note moyenne",
    labels={"genre": "Genre", "rating_count": "Nombre d'évaluations", "avg_rating": "Note moyenne"}
)
fig_genre_rating.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=350
)



# Graphique 4 : Top 20 des films par nombre d’évaluations
fig_top_movies = px.bar(
    top_movies.sort_values("rating_count", ascending=True),
    x="rating_count",
    y="title",
    color="avg_rating",
    orientation="h",
    title="Top 20 des films par nombre d'évaluations",
    labels={"title": "Titre du film", "rating_count": "Nombre d'évaluations", "avg_rating": "Note moyenne"},
    color_continuous_scale="viridis"
)
fig_top_movies.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=700
)

# Graphique 5 : Nombre de films par année
fig_by_year = px.bar(
    movies_by_year,
    x="year",
    y="movie_count",
    title="Nombre total de films par année (basé sur le titre)",
    labels={"year": "Année", "movie_count": "Nombre de films"},
)
fig_by_year.update_layout(
    xaxis_title="Année",
    yaxis_title="Nombre de films",
    height=500
)

st.markdown("##  Exploration des genres")
st.markdown(
    "Cette section analyse la répartition des films et l’engagement des utilisateurs selon les genres."
)

st.plotly_chart(fig_genre, use_container_width=True)

st.markdown(
    " Ce graphique montre quels genres dominent le catalogue en volume."
)

st.plotly_chart(fig_genre_rating, use_container_width=True)

st.markdown(
    " Ici, on observe l’engagement des utilisateurs et la qualité perçue par genre."
)

st.divider()
st.markdown("##  Films les plus évalués")
st.markdown(
    "Focus sur les films qui concentrent le plus d’attention et leur qualité moyenne."
)

st.plotly_chart(fig_top_movies, use_container_width=True)

st.markdown(
    " Popularité et qualité ne vont pas toujours de pair."
)

st.divider()
st.markdown("##  Évolution du catalogue")
st.markdown(
    "Analyse de l’évolution du nombre de films au fil des années."
)

st.plotly_chart(fig_by_year, use_container_width=True)

st.markdown(
    " Mise en évidence des périodes de forte croissance de la production."
)


