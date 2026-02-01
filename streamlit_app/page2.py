import streamlit as st
import pandas as pd
import plotly.express as px
import os
from pathlib import Path
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

# Définir le répertoire de sortie
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

st.title("🏷️ Tags Insights")

# Chargement des datasets
tag_df = load_csv_data("user_tag_stats.csv")
tags_good_rating_df = load_csv_data("tags_good_rating.csv")
tags_compare_df = load_csv_data("tags_compare.csv")
tags_by_genre_df = load_csv_data("tags_by_genre.csv")

# Graphique 1 : Top tags utilisés par les utilisateurs
fig_user_tags = px.bar(
    tag_df, x="count", y="tag", orientation="h",
    title="Top tags utilisés par les utilisateurs",
    labels={"count": "Nombre d’utilisations", "tag": "Tag"},
    color="count", color_continuous_scale="viridis"
)
fig_user_tags.update_layout(yaxis={'categoryorder': 'total ascending'}, height=500)

#st.plotly_chart(fig_user_tags, use_container_width=True)

# Graphique 2 : Tags dans films bien notés
fig_good_tags = px.bar(
    tags_good_rating_df,
    x="count",
    y="tag",
    orientation="h",
    title="Tags les plus fréquents dans les films bien notés (note ≥ 4)",
    labels={"count": "Nombre d’occurrences", "tag": "Tag"},
    color="count",
    color_continuous_scale="viridis"
)
fig_good_tags.update_layout(yaxis={'categoryorder': 'total ascending'}, height=500)
#st.plotly_chart(fig_good_tags, use_container_width=True)


# Graphique 3 : Comparaison des tags films bien notés vs mal notés
tags_compare_melted = tags_compare_df.melt(
    id_vars="tag",
    value_vars=["count_good", "count_bad"],
    var_name="Type",
    value_name="count"
)
fig_compare_tags = px.bar(
    tags_compare_melted,
    x="count",
    y="tag",
    color="Type",
    barmode="group",
    title="Comparaison des Tags : Films bien notés vs mal notés",
    labels={"count": "Nombre d’occurrences", "tag": "Tag"},
    height=500
)
fig_compare_tags.update_layout(yaxis={'categoryorder': 'total ascending'})
#st.plotly_chart(fig_compare_tags, use_container_width=True)

# Affichage en 3 colonnes
col1, col2, col3 = st.columns(3)
with col1:
    st.plotly_chart(fig_user_tags, use_container_width=True)
with col2:
    st.plotly_chart(fig_good_tags, use_container_width=True)
with col3:
    st.plotly_chart(fig_compare_tags, use_container_width=True)

st.divider()

# Préparation des données pour le graphique final
top_tags_by_genre = tags_by_genre_df.groupby("genre").apply(
    lambda g: g.nlargest(3, 'count')
).reset_index(drop=True)
top_tags_by_genre["tag_label"] = top_tags_by_genre["tag"] + " (" + top_tags_by_genre["genre"] + ")"

# Multi-sélecteur de genres
all_genres = sorted(top_tags_by_genre["genre"].unique())
selected_genres = st.multiselect(
    "🎯 Sélectionnez les genres à afficher :",
    options=all_genres,
    default=all_genres
)

# Dataframe réactive en fonction du ou des genres sélectionnés par l'utilisateur de l'app
filtered_tags = top_tags_by_genre[top_tags_by_genre["genre"].isin(selected_genres)]

# Graphique final : Top 3 tags par genre
fig_tags_by_genre = px.bar(
    filtered_tags.sort_values("count"),
    x="count",
    y="tag_label",
    color="genre",
    orientation="h",
    title="Top 3 Tags les plus utilisés par Genre",
    labels={"count": "Nombre d'occurrences", "tag_label": "Tag (Genre)"},
    height=800
)
fig_tags_by_genre.update_layout(yaxis=dict(categoryorder='total ascending'))

# Affichage du graphique en pleine largeur
st.plotly_chart(fig_tags_by_genre, use_container_width=True)