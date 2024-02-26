import pickle
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": "8265bd1679663a7ea12ac168da84d2e8", "language": "en-US"}
    response = requests.get(url, params=params)
    data = response.json()
    poster_path = data.get('poster_path')
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None

# Function to recommend similar movies
def recommend(movie):
    selected_movies = movies.loc[movies['title'] == movie]
    if selected_movies.empty:
        return []  # Return an empty list if no movie matches the given title
    
    index = selected_movies.index[0]
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i, (movie_index, score) in enumerate(distances[1:6], start=1):
        movie_data = movies.iloc[movie_index]
        recommended_movies.append({
            'name': movie_data['title'],
            'poster': fetch_poster(movie_data['movie_id']),
            'score': score
        })
    return recommended_movies


# Load movie data and similarity scores
with open('movie_list.pkl', 'rb') as file:
    movies = pickle.load(file)
with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_movies = []
    if request.method == 'POST':
        selected_movie = request.form.get('selected_movie')
        recommended_movies = recommend(selected_movie)
    # Load the movie list for the dropdown
    with open('movie_list.pkl', 'rb') as file:
        movie_list = pickle.load(file)['title'].tolist()
    return render_template('index.html', recommended_movies=recommended_movies, movie_list=movie_list)


if __name__ == '__main__':
    app.run(debug=True)
