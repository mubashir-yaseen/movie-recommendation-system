import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Load preprocessed movie data
with open('updated_movie_list.json', 'r') as f:
    movie_data = json.load(f)

# Load preprocessed similarity matrix
try:
    with open('reduced_similarity.json', 'r') as f:
        similarity_data = json.load(f)
except FileNotFoundError:
    print("Error: 'reduced_similarity.json' file not found.")
    similarity_data = []

# Set the threshold value
threshold = 0.5

# TMDB API Key
TMDB_API_KEY = "6c22505b004449fe37e6509b2d4b71ba"

# User feedback data
user_feedback = []

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return None

def recommend(movie_title):
    if not similarity_data:
        return []
    
    if movie_title not in [movie['title'] for movie in movie_data]:
        return []

    # Get the index of the movie
    movie_index = [movie['title'] for movie in movie_data].index(movie_title)

    # Get similarity scores for the given movie
    similarity_scores = similarity_data[movie_index]

    # Filter movies based on the threshold
    recommended_movies = [movie_data[idx] for idx, score in enumerate(similarity_scores) if score > threshold]

    # Exclude the queried movie from recommendations
    recommended_movies = [movie for movie in recommended_movies if movie['title'] != movie_title]

    # Return top 5 recommended movies with posters and similarity scores
    recommended_movies_with_posters = []
    for movie in recommended_movies[:5]:
        movie_id = movie['movie_id']  # Get movie ID from the data
        poster_url = fetch_poster(movie_id)
        similarity_score = similarity_scores[movie_data.index(movie)]  # Get similarity score
        recommended_movies_with_posters.append({'title': movie['title'], 'poster': poster_url, 'score': similarity_score})
    
    return recommended_movies_with_posters

def update_similarity_matrix():
    # Use user feedback to update similarity matrix
    pass  # Add your code here

@app.route('/')
def index():
    return render_template('index.html', movie_list=[movie['title'] for movie in movie_data], name="Muhammad Mubashir")

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    movie_title = request.form['selected_movie']
    recommendations = recommend(movie_title)
    return render_template('recommendations.html', movie_title=movie_title, recommended_movies=recommendations, name="Muhammad Mubashir")

@app.route('/feedback', methods=['POST'])
def collect_feedback():
    feedback = request.json
    user_feedback.append(feedback)
    update_similarity_matrix()  # Update similarity matrix based on user feedback
    return "Feedback received successfully."

# Handle favicon.ico requests
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)
