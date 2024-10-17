import requests
import streamlit as st

API_URL = "http://127.0.0.1:5000"

st.title("Détails d'un film avec Streamlit")
movie_id = st.text_input("Entrer l'ID d'un film", value="550")

if st.button("Détails du film"):
    if not movie_id:
        st.error("Entrer un ID de film.")
    else:
        response = requests.get(f"{API_URL}/movie/{movie_id}")
        if response.status_code == 200:
            movie = response.json()
            if "error" in movie:
                st.error(movie["error"])
            else:
                st.write(f"**Title**: {movie['title']}")
                st.write(f"**Release Date**: {movie['release_date']}")
                st.write(f"**Genres**: {', '.join(movie['genres'])}")
                st.write(f"**Popularity**: {movie['popularity']}")
                st.write(f"**Average Vote**: {movie['vote_average']}")
        else:
            st.error("Impossible de récupérer les détails du film.")
