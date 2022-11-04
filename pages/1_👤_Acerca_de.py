import streamlit as st

st.balloons()

st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/memo_1f4dd.png",
    width = 100
)

st.title("Acerca del proyecto")
st.markdown(
    """
    ### Herramientas utilizadas
    - Programado en Python
    - Streamlit
    - Transformers
    - Streamlit-chat
    - Huggingface
    ---
    ### Información académica
    - Carrera: Ingeniería en Sistemas de Información
    - Cátedra: Seminario de Actualización II
    - Año académico: 2022
    - Prof.: Mg. Ms. Lic. Marcelo Fabio Roldán
    - Prof.: Lic. Cristina Gramajo
    """
)

st.markdown("### Integrantes del proyecto")
tab1, tab2 = st.tabs(["Dominguez Sotomayor Santiago Ismael", "Rios Lopez Ramiro Ignacio"])

with tab1:
    st.image("DSSI.png")
    st.markdown(
        """
        ### Nombre
        - Dominguez Sotomayor Santiago Ismael
        ---
        ### Matrícula
        - EISI782
        ---
        ### Fecha de nacimiento
        - 04/05/01
        ---
        ### Redes sociales
        - [Perfil en Instagram](https://www.instagram.com/santidominguez01/)
        - [Perfil en GitHub](https://github.com/SantiDominguez1)
        - [Perfil en LinkedIn](https://www.linkedin.com/in/santiago-ismael-dominguez-sotomayor-a55009225//)
        ---
        ### Correo electrónico
        - santiuni04@gmail.com
        """
    )

with tab2:
    st.image("RLRI.png")
    st.markdown(
        """
        ### Nombre
        - Rios Lopez Ramiro Ignacio
        ---
        ### Matrícula
        - EISI801
        ---
        ### Fecha de nacimiento
        - 11/06/01
        ---
        ### Redes sociales
        - [Perfil en Instagram](https://www.instagram.com/rama.riosl/)
        - [Perfil en GitHub](https://github.com/RLRama)
        - [Perfil en LinkedIn](https://www.linkedin.com/in/ramiro-ignacio-rios-lopez-bb1006225/)
        ---
        ### Correo electrónico
        - santiuni04@gmail.com
        """
    )