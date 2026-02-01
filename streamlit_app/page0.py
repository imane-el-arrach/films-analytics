import streamlit as st
from pathlib import Path
# Interface utilisateur avec Streamlit
st.set_page_config(
    layout="wide",
    page_title="MovieLens Data Analysis",
    page_icon="🎬"  
)

# Conteneur pour aligner les éléments horizontalement
col1, col2, col3 = st.columns([1, 4, 1])

BASE_DIR = Path(__file__).parent
# Colonne gauche : Image
st.image(
    BASE_DIR / "icon1.jpg",
    width=80,
    use_container_width=False
)

# Colonne centrale : Titre
with col2:
    st.markdown(
        """
        <h1 style='text-align: center; margin-bottom: 0;'>Exploration des Données MovieLens</h1>
        """,
        unsafe_allow_html=True,
    )

# Colonne droite : Nom et lien LinkedIn
with col3:
    st.markdown(
        """
        <div style='text-align: right;'>
            <a href="https://www.linkedin.com/in/imane-el-arrach-7a88ab325/" target="_blank" style='text-decoration: none; color: #0077b5;'>
                <strong>IMANE EL ARRACH</strong>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write(" ")
st.write(" ")

# Titre
st.markdown("# **Phase 1 : Développeur Python & Architecte API**")
# Afficher l'image séparément
BASE_DIR = Path(__file__).parent
image_path = BASE_DIR / "architectureB.png"

st.image(str(image_path), use_container_width=True)

st.markdown(
        """
        <a href="https://github.com/imane-el-arrach/movie_backend" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📦 Cliquer pour voir le Code de la Phase 1
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.write(" ")
st.write(" ")
st.write(" ")


# Titre
st.markdown("# **Phase 2 : Data Analyst - Exploration et Visualisation**")
# Afficher l'image séparément
st.image(
    BASE_DIR / "architecturephase.png",
    use_container_width=True
)
st.markdown(
        """
        <a href="https://github.com/imane-el-arrach/films-analytics" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📊 Cliquer pour voir le Code de la Phase 2
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )