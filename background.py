from streamlit_lottie import st_lottie
import json
import streamlit as st
from streamlit.elements.image import image_to_url

st.set_page_config(page_title="背景和动画设置", layout="wide")

#加载背景图
img_url = image_to_url('beach.jpg',width=-3,clamp=False,channels='RGB',output_format='auto',image_id='',allow_emoji=False)

st.markdown('''
<style>
.css-fg4pbf {background-image: url(''' + img_url + ''');}</style>
''', unsafe_allow_html=True)

#加载动画
with open("35109-plane-ticket.json", "r",errors='ignore') as f:
    data1 = json.load(f)
    st_lottie(data1, key="1")

c1, c2, c3 = st.columns(3)

with c1:
    with open("tree-in-the-wind.json", "r",errors='ignore') as f:
        data2 = json.load(f)
        st_lottie(data2, key="2")
with c2:
    with open("people-communicating.json", "r",errors='ignore') as f:
        data3 = json.load(f)
        st_lottie(data3, key="3")
with c3:
    with open("78714-plane.json", "r",errors='ignore') as f:
        data4 = json.load(f)
        st_lottie(data4, key="4")