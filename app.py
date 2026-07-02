import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key = lambda x:x[1])[1:6]

    recomended_movies = []

    for i in movies_list:
        recomended_movies.append(movies.iloc[i[0]].title)
    
    return recomended_movies

movie_dict = pickle.load(open("./notebook/movies.pkl", "rb"))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open("./notebook/similarity.pkl", "rb"))

st.title('CineMatch Movie Recommender')

selected_movie_name = st.selectbox(
("Select a movie name "),
movies['title'].values
)

if st.button('Recommend'):
   recomendatoins = recommend(selected_movie_name)
   for i in recomendatoins:
       st.write(i)
