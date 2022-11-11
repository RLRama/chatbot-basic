import streamlit as st
from numpy import load
from numpy import expand_dims
from matplotlib import pyplot
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

st.set_page_config(
    page_title="Chatbot con Python",
    page_icon="💬",
)

st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/paintbrush_1f58c-fe0f.png",
    width=100
)
st.title('Generación de imágenes ASCII con redes generativas antagónicas')
st.markdown("Elige una imagen para convertir a arte ASCII")

uploaded_file = st.file_uploader("Subir archivo de imagen")

def asciiart(in_f, SC, GCF,  out_f, color1='black', color2='blue', bgcolor='white'):

    # El arreglo de símbolos ASCII yendo de blanco a negro
    chars = np.asarray(list(' .,:irs?@9B&#'))

    # Cargar de fuentes y tamaño (ancho y alto) de un símbolo común. Podemos usar distintas fuentes acá
    font = ImageFont.load_default()
    letter_width = font.getsize("x")[0]
    letter_height = font.getsize("x")[1]

    WCF = letter_height/letter_width

     # Abrir el archivo de entrada
    img = Image.open(in_f)


    # De acuerdo a la imagen de salida, calcular cuántas letras ASCII se necesitan para el ancho y alto
    widthByLetter=round(img.size[0]*SC*WCF)
    heightByLetter = round(img.size[1]*SC)
    S = (widthByLetter, heightByLetter)

    # Cambiar el tamaño de imagen con respecto al ancho y alto de los símbolos
    img = img.resize(S)
    
    # Valores de color RGB de punto de pixel de muestra y conversión monocromática usando el método promedio. Más información en https://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
    img = np.sum(np.asarray(img), axis=2)
    
    # Normalización de resultados, mejorar y reducir el contraste del brillo
    img -= img.min()
    img = (1.0 - img/img.max())**GCF*(chars.size-1)
    
    # Generar símbolos de arte ASCII
    lines = ("\n".join( ("".join(r) for r in chars[img.astype(int)]) )).split("\n")

    # Crear bin de color de gradiente
    nbins = len(lines)

    # Crear un objeto imagen, darle ancho y alto
    newImg_width= letter_width *widthByLetter
    newImg_height = letter_height * heightByLetter
    newImg = Image.new("RGBA", (newImg_width, newImg_height), bgcolor)
    draw = ImageDraw.Draw(newImg)

    # Imprimir símbolos a la imagen
    leftpadding=0
    y = 0
    lineIdx=0
    for line in lines:
        color = 'blue'
        lineIdx +=1

        draw.text((leftpadding, y), line, '#0000FF', font=font)
        y += letter_height

    # Guardar el archivo imagen

    newImg.save(out_f)


def load_image(filename, size=(512,512)):
	# Carga de imagen con el tamaño preferido
	pixels = load_img(filename, target_size=size)
	# Conversión a arreglo de numpy
	pixels = img_to_array(pixels)
	# Reescalar de [0,255] a [-1,1]
	pixels = (pixels - 127.5) / 127.5
	# Cambiar forma a una muestra
	pixels = expand_dims(pixels, 0)
	return pixels


def imgGen2(img1):
  inputf = img1  # Nombre de archivo de imagen de entrada

  SC = 0.1    # Tasa de muestreo de píxeles en ancho
  GCF= 2      # Ajuste de contraste

  asciiart(inputf, SC, GCF, "results.png")   # color predeterminado de negro a azul
  asciiart(inputf, SC, GCF, "results_pink.png","blue","pink")
  img = Image.open(img1)
  img2 = Image.open('results.png').resize(img.size)
  return img2	


if uploaded_file is not None:
    image = Image.open(uploaded_file)	
	
    st.image(uploaded_file, caption='Imagen de entrada', use_column_width=True)
    im = imgGen2(uploaded_file)	
    st.image(im, caption='Imagen pero en arte ASCII', use_column_width=True)