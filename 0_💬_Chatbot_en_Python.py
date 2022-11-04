import streamlit as st
import nltk
import json
import numpy as np
import tensorflow as tf
from streamlit_chat import message
from nltk.stem import WordNetLemmatizer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

nltk.download("punkt")
nltk.download("wordnet")

json_file_path = "intents.json"
with open(json_file_path, 'r').read() as j:
    contents = json.loads(j.read())

st.write(contents)