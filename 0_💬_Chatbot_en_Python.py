import streamlit as st
import nltk
import numpy as np
import tensorflow as tensorF
from streamlit_chat import message
from nltk.stem import WordNetLemmatizer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout