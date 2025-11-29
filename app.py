import streamlit as st 
import pandas as pd 
import pickle 

movies =pickle.load(open("movies_list.pkl",'rb'))
similarity =pickle.load(open("similarity.pkl",'rb'))


movies_list =movies['title'].values
st.header("Movie Recomender System") 

select_value =st.selectbox("Select the movies from dropdown",movies_list) 


def recommand(movies): 
    index = movies[movies['title'] ==movies].index[0]
    
    distance = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1]) 
    recommend_movies =[]
    for i in distance[0:5]: 
        recommend_movies.append(movies.iloc[i[0]].title) 
    return recommend_movies

if st.button("show Recommend") :
    movie_name =recommand(select_value) 
    col1,col2,col3,col4,col5 =st.columns(5) 
    with col1: 
        st.text(movie_name[0])
    with col2: 
        st.text(movie_name[1])
    with col3: 
        st.text(movie_name[2])
    with col4: 
        st.text(movie_name[3])
    with col5: 
        st.text(movie_name[4])
 