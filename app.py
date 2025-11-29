import streamlit as st 
import pandas as pd 
import pickle 

movies =pickle.load(open("movies_list.pkl",'rb'))

movies_list =movies['title'].values
st.header("Movie Recomender System") 

st.selectbox("Select the movies from dropdown",movies_list) 



if st.button("show Recommend") :
    pass
 