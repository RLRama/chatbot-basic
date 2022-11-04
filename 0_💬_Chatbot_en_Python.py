import streamlit as st
import nltk
import numpy as np
import tensorflow as tensorF
from streamlit_chat import message
from nltk.stem import WordNetLemmatizer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

nltk.download("punkt")
nltk.download("wordnet")

lm = WordNetLemmatizer() # para obtener palabras
# listas
ourClasses = []
newWords = []
documentX = []
documentY = []
# cada intención es tokenizada en palabras y los patrones y sus etiquetas asociadas se añaden a sus listas respectivas
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        ournewTkns = nltk.word_tokenize(pattern)
        newWords.extend(ournewTkns)
        documentX.append(pattern)
        documentY.append(intent["tag"])

# añade etiquetas inexistentes a sus clases respectivas
    if intent["tag"] not in ourClasses:
        ourClasses.append(intent["tag"])

newWords = [lm.lemmatize(word.lower()) for word in newWords if word not in string.punctuation] # set words to lowercase if not in punctuation
newWords = sorted(set(newWords)) # ordena palabras
ourClasses = sorted(set(ourClasses)) # ordena clases