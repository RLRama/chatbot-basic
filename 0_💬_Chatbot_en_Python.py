import streamlit as st
import transformers
import requests
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from streamlit_chat import message as st_message

st.set_page_config(
    page_title="Chatbot con Python",
    page_icon="💬",
)

st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/robot_1f916.png",
    width=100
)
st.title('¡Chatbot con Python!')
st.markdown('Bienvenido al chatbot. ¡**Todavía estoy aprendiendo**, porfavor tenga paciencia!')

st.sidebar.markdown(
    """
    ### Desarrollado por
    - Rios Lopez Ramiro Ignacio
    - [Perfil en GitHub](https://github.com/RLRama)
    - [Perfil en LinkedIn](https://www.linkedin.com/in/ramiro-ignacio-rios-lopez-bb1006225/)
    ---
    - Dominguez Sotomayor Santiago Ismael
    - [Perfil en GitHub](https://github.com/SantiDominguez1)
    - [Perfil en LinkedIn](https://www.linkedin.com/in/santiago-ismael-dominguez-sotomayor-a55009225//)
    
    """
)
#Caché del modelo de Huggingface
@st.experimental_singleton
def get_models():
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

#Inicializar el estado de sesión de Streamlit
if "history" not in st.session_state:
    st.session_state.history = []

#Generación de respuesta
def generate_answer():
    tokenizer, model = get_models()
    user_message = st.session_state.input_text
    inputs = tokenizer(st.session_state.input_text, return_tensors="pt")
    result = model.generate(**inputs)
    message_bot = tokenizer.decode(
        result[0], skip_special_tokens=True
    )

    #Guardar respuesta en historial de estado
    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})

#Mostrar historial de chat
for chat in st.session_state.history:
    st_message(**chat)

st.text_input("Hablá con el chatbot (¡en inglés!)", key="input_text", on_change=generate_answer, placeholder = "Sólo entiendo en inglés")