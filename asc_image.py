import streamlit as st
from numpy import load
from numpy import expand_dims
from matplotlib import pyplot
from PIL import Image, ImageDraw, ImageFont, ImageFile
import numpy as np
import os
from PIL import ImageFile
from keras.preprocessing.image import load_img, img_to_array
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

st.set_page_config(page_title='ASCII字符画生成器', page_icon="🅰", layout="wide")

st.header("上传一张图片生成ASCII字符画")

ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

color_fornt = st.sidebar.color_picker('选择前景色', '#00b8e6')

color_background = st.sidebar.color_picker('选择背景色', '#ffffff')

sc_control = st.sidebar.slider('选择密度参数1', 0.1, 0.9, 0.5, 0.1)
gcf_control = st.sidebar.slider('选择密度参数2', 0.5, 4.5, 2.1, 0.1)

uploaded_file = st.file_uploader("选择一张图片", type=["png","jpg","bmp","jpeg"])

@st.cache_data
def asciiart(in_f, SC, GCF,  out_f, bgcolor=color_background):

    chars = np.asarray(list(' .,:irs?@9B&#*$%!~'))

    font = ImageFont.load_default()
    letter_width = font.getsize("x")[0]
    letter_height = font.getsize("x")[1]
    WCF = letter_height/letter_width
    img = Image.open(in_f)
    widthByLetter=round(img.size[0]*SC*WCF)
    heightByLetter = round(img.size[1]*SC)
    S = (widthByLetter, heightByLetter)
    img = img.resize(S)
    img = np.sum(np.asarray(img), axis=2)
    img -= img.min()
    img = (1.0 - img/img.max())**GCF*(chars.size-1)
    lines = ("\n".join( ("".join(r) for r in chars[img.astype(int)]) )).split("\n")
    nbins = len(lines)
    newImg_width= letter_width *widthByLetter
    newImg_height = letter_height * heightByLetter
    newImg = Image.new("RGBA", (newImg_width, newImg_height), bgcolor)
    draw = ImageDraw.Draw(newImg)
    leftpadding=0
    y = 0
    lineIdx=0

    for line in lines:
        color = color_fornt
        lineIdx +=1
        draw.text((leftpadding, y), line, color, font=font)
        y += letter_height

    newImg.save(out_f)

@st.cache_data
def load_image(filename, size=(512,512)):
    pixels = load_img(filename, target_size=size)
    pixels = img_to_array(pixels)
    pixels = (pixels - 127.5) / 127.5
    pixels = expand_dims(pixels, 0)
    return pixels

@st.cache_data
def imgGen2(img1):
  inputf = img1
  SC = sc_control
  GCF= gcf_control
  asciiart(inputf, SC, GCF, "results.png",color_background)
  img = Image.open(img1)
  img2 = Image.open('results.png').resize(img.size)
  return img2    

#下载按钮效果设置
css = """<style>
.stDownloadButton>button {
    background-color: #0099ff;
    color:#ffffff;
}

.stDownloadButton>button:hover {
    background-color: green;
    color:white;
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)


if uploaded_file is not None:
    st.sidebar.image(uploaded_file, caption='原始图片', use_column_width=True)
    im = imgGen2(uploaded_file)    
    st.image(im, width=700)
    with open("results.png", "rb") as file:
        #st.image("图片.jpg")
        btn = st.download_button(
            label="点我下载生成的ASCII字符画",
            data=file,
            file_name="ASCII字符画.png",
            mime="image/png"
            )