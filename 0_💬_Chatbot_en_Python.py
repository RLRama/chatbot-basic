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

dataPath = "intents.json"

with open(dataPath,'r') as j:
    contents = json.loads(j.read())