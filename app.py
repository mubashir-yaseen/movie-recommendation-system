import json
import pandas as pd
from flask import Flask, render_template, request
from reduce_similarity import reduce_similarity


app = Flask(__name__)

# Load movie data from JSON
with open('movie_list.json', 'r') as f:
    movie_data = json.load(f)

# Load reduced similarity matrix from JSON
with open('reduced_similarity.json', 'r') as f:
    similarity_data = json.load(f)

# Convert similarity matrix back to numpy array
similarity_matrix = pd.DataFrame(similarity_data)

# Set the threshold value (you need to define the threshold)
threshold = 0.5

# Reduce similarity data
reduce_similarity(similarity_matrix, threshold)

def recommend(movie_title):
    # Find the index of the movie
    movie_index = movie_data.index[movie_data['title'] == movie_title][0]
    # Get similarity scores for the given movie
    similarity_scores = similarity_matrix.iloc[movie_index]
    # Sort movies based on similarity scores
    recommended_movies = similarity_scores.sort_values(ascending=False).index[1:6]
    # Return the titles of recommended movies
    return movie_data.iloc[recommended_movies]['title'].tolist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    movie_title = request.form['movie_title']
    recommended_movies = recommend(movie_title)
    return render_template('recommendations.html', movie_title=movie_title, recommended_movies=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
