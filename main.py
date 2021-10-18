from flask import Flask, render_template, request, redirect, url_for
import tmdb_client
import random
import datetime

app = Flask(__name__)

@app.route('/')
def homepage():
    types=['popular', 'now_playing', 'top_rated', 'upcoming']
    selected_list = request.args.get('list_type', "popular")
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, selected_list=selected_list, types=types)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
   details = tmdb_client.get_single_movie(movie_id)
   cast = tmdb_client.get_single_movie_cast(movie_id)
   movie_images = tmdb_client.get_movie_images(movie_id)
   selected_backdrop = random.choice(movie_images['backdrops'])
   return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)

@app.route("/search")
def search():
    search_query = request.args.get("qry", "")
    if search_query:
        movies = tmdb_client.search(search_query=search_query)
    else:
        movies=[]
    return render_template("search.html", movies=movies, search_query=search_query)

@app.route('/today')
def today():
    movies=tmdb_client.get_airing_today()
    today = datetime.date.today()
    return render_template("today.html", movies=movies, today=today)

if __name__ == '__main__':
    app.run(debug=True)
