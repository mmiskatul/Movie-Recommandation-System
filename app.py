import streamlit as st 
import pandas as pd 
import pickle 

movies =pickle.load(open("movies_list.pkl",'rb'))


st.header("Movie Recomender System") 

st.selectbox("Select the movies from dropdown",movies) 


if st.button("show Recommend") :
    pass
 