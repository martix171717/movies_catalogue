import requests

def get_popular_movies():
    endpoint= "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MjJjNzc0NDZmZDA0NDI3NmI1YjNkMTgzN2FiNzc0ZSIsInN1YiI6IjYxNjE2YWU2ODlkOTdmMDAyOTExMGIyOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QysD4IfN6R-qX8HsR1ejvMwSfPWkmfymAb4mRDJvha8"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

