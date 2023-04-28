from turtle import pd
import streamlit as st
import pandas as pd
import numpy as np
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

st.title("bbriz")
st.write('Hello, *World!* :sunglasses:')
st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    from PIL import Image

image = Image.open('forest.jpg')

st.image(image, caption='forest')

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

df = pd.read_csv("data.csv")
st.dataframe(df)



uri = "mongodb+srv://a01742281:<01-speedyB@cluster0.of1edeq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    st.write("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    st.write(e)
