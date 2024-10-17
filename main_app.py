import os
import time

import requests
from flask import Flask, jsonify, Blueprint

API_KEY = os.getenv("API_KEY_TMDB")
BASE_URL = "https://api.themoviedb.org/3"

app = Flask(__name__)

movie_details_route = Blueprint("movie_details_route", __name__)


@app.route("/movie/<int:movie_id>", methods=["GET"])
def movie_details(movie_id):
    movie = get_movie_details(movie_id)
    return jsonify(movie)


def get_movie_details(movie_id):
    if not API_KEY:
        return {"error": "L'API TMDB n'est pas configurée."}
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY}
    response = get_with_retry(url, params=params)

    if response and "title" in response:
        return {
            "title": response.get("title"),
            "release_date": response.get("release_date"),
            "genres": [genre["name"] for genre in response.get("genres", [])],
            "popularity": response.get("popularity"),
            "vote_average": response.get("vote_average"),
        }
    else:
        return {"error": f"Impossible de récupérer les détails du film."}


def get_with_retry(url, params=None, max_retries=3, backoff_factor=2):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                print("Trop de requêtes. Attente avant de réessayer...")
                time.sleep(5)
            elif response.status_code in [500, 503]:
                print(f"Erreur serveur. Attente avant de réessayer...")
                time.sleep(5)
            elif response.status_code in [400, 401, 403, 404]:
                print(f"Erreur client. Impossible de continuer.")
                break
            else:
                print(f"Erreur inconnue : {response.status_code}")
                break
        except requests.exceptions.RequestException as e:
            print(f"Une erreur est apparue : {e}")
        retries += 1
    return None


if __name__ == "__main__":
    app.run(debug=True)
