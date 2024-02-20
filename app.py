import pickle
import streamlit as st
import requests

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
    index = movies.loc[movies['title'] == movie].index[0]
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

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title('Movie Recommender System')

selected_movie = st.selectbox(
    "Select a movie from the dropdown",
    movies['title'].values
)

if st.button('Get Recommendations'):
    recommended_movies = recommend(selected_movie)
    num_cols = min(len(recommended_movies), 5)
    cols = st.columns(num_cols)
    for i, col in enumerate(cols):
        if i < len(recommended_movies):
            with col:
                st.image(recommended_movies[i]['poster'], use_column_width=True)
                st.write(recommended_movies[i]['name'])
                st.write(f"Similarity Score: {recommended_movies[i]['score']:.2f}")
