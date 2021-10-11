from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = ["The Green Mile", "Mad Max", "Forrest Gump", "Pulp Fiction"]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)