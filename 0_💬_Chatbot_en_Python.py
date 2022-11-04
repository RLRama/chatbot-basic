import streamlit as st
import nltk
import json
import string
import random
import numpy as np
import tensorflow as tf
from streamlit_chat import message
from nltk.stem import WordNetLemmatizer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

nltk.download("punkt")
nltk.download("wordnet")

data_file = open('chatbot\intents.json').read()
data = json.loads(data_file)