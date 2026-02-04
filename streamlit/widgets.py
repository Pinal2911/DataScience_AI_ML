import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name : ")
if name:
    st.write(f"Name ={name} ")
#slider
age=st.slider("Select your age : ",0,100,30)
st.write("Age = ",age)

#dropdown select
options = ["Python","Java","C++","JS"]
choice=st.selectbox("Choose your fav language : ",options)
st.write(f"Fav Language = {choice}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("choose a CSV file to updaload",type='csv')
if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.write(df)

