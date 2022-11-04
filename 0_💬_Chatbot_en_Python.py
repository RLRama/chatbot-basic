import streamlit as st
import transformers
import requests
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from streamlit_chat import message as st_message

st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/robot_1f916.png",
    width=100
)
st.title('¡Chatbot con Python!')
st.markdown('Bienvenido al chatbot. ¡**Todavía estoy aprendiendo**, porfavor tenga paciencia!')

@st.experimental_singleton
def get_models():
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

if "history" not in st.session_state:
    st.session_state.history = []

def generate_answer():
    tokenizer, model = get_models()
    user_message = st.session_state.input_text
    inputs = tokenizer(st.session_state.input_text, return_tensors="pt")
    result = model.generate(**inputs)
    message_bot = tokenizer.decode(
        result[0], skip_special_tokens=True
    )

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})

st.text_input("Hablá con el chatbot", key="input_text", on_change=generate_answer, placeholder = "Sólo entiendo en inglés")

for chat in st.session_state.history:
    st_message(**chat)