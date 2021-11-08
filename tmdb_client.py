import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MjJjNzc0NDZmZDA0NDI3NmI1YjNkMTgzN2FiNzc0ZSIsInN1YiI6IjYxNjE2YWU2ODlkOTdmMDAyOTExMGIyOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QysD4IfN6R-qX8HsR1ejvMwSfPWkmfymAb4mRDJvha8"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many,list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")["cast"]

def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return get_movies_list(list_type="popular")
    return response.json()

def search(search_query):
    endpoint = f"https://api.themoviedb.org/3/search/movie/?query={search_query}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["results"]

def get_airing_today():
    endpoint = "https://api.themoviedb.org/3/tv/airing_today"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()['results']
