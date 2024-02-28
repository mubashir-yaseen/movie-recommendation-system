import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Load preprocessed movie data
with open('updated_movie_list.json', 'r') as f:
    movie_data = json.load(f)

# Load preprocessed similarity matrix
with open('reduced_similarity.json', 'r') as f:
    similarity_data = json.load(f)

# Set the threshold value
threshold = 0.5

def recommend(movie_title):
    if movie_title not in [movie['title'] for movie in movie_data]:
        return []
    
    # Get the index of the movie
    movie_index = [movie['title'] for movie in movie_data].index(movie_title)
    
    # Get similarity scores for the given movie
    similarity_scores = similarity_data[movie_index]
    
    # Filter movies based on the threshold
    recommended_movies = [movie_data[idx]['title'] for idx, score in enumerate(similarity_scores) if score > threshold]
    
    # Exclude the queried movie from recommendations
    recommended_movies = [movie for movie in recommended_movies if movie != movie_title]
    
    # Return top 5 recommended movies
    return recommended_movies[:5]

@app.route('/')
def index():
    return render_template('index.html', movie_list=[movie['title'] for movie in movie_data])

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    movie_title = request.form['selected_movie']
    recommendations = recommend(movie_title)
    return render_template('recommendations.html', movie=movie_title, recommended_movies=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
