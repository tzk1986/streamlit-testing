import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="图片漫化处理", layout="wide")

#取图像轮廓
@st.cache_data
def sketch_img(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #中值滤波
    img_gray = cv2.medianBlur(img_gray,5)
    #检测图片
    edges = cv2.Laplacian(img_gray,cv2.CV_8U,ksize =5)
    #获取图像阈值
    ret, thresholded = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)
    return thresholded

#对图像进行卡通处理
@st.cache_data
def cartoonize_image(img, gray_mode = False):
    thresholded = sketch_img(img)
    #应用双边滤波算法对图像进行卡通化处理
    filtered= cv2.bilateralFilter(img,s1,s2,s3)
    cartoonized = cv2.bitwise_and(filtered, filtered, mask=thresholded)
    if gray_mode:
        return cv2.cvtColor(cartoonized, cv2.COLOR_BGR2GRAY)
    return cartoonized

st.title('使用OpenCV对图片进行漫化处理')

img_file_buffer = st.file_uploader("上传图片", type=[ "jpg", "jpeg",'png'])

s1 = st.sidebar.slider(label="像素的邻域直径", min_value=0, max_value=255, value=10)
s2 = st.sidebar.slider(label="颜色空间的标准方差，一般尽可能大", min_value=10, max_value=255, value=250)
s3 = st.sidebar.slider(label="坐标空间的标准方差(像素单位)，一般尽可能小", min_value=0, max_value=255, value=50)
s4 = st.sidebar.slider(label="图像平滑参数", min_value=0, max_value=200, value=60)
s5 = st.sidebar.slider(label="颜色平衡度，数值越大，同颜色的区域就会越大", min_value=0.00, max_value=1.00, value=0.05)
s6 = st.sidebar.slider(label="铅笔画亮度参数，值越大，图像越亮", min_value=0.00, max_value=0.10, value=0.03)


if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))
    st.sidebar.image(image, caption=f"原始图片", use_container_width=True)
    custom_sketch_image = sketch_img(image)
    custom_cartonized_image = cartoonize_image(image)
    custom_cartonized_image_gray = cartoonize_image(image, True)

    sketch_gray, sketch_color = cv2.pencilSketch(image, sigma_s=30, sigma_r=0.1, shade_factor=s6)
    stylizated_image = cv2.stylization(image, sigma_s=s4, sigma_r=s5)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader('轮廓图')
        st.image(custom_sketch_image, caption=f"轮廓图", use_container_width=True)

        st.subheader('漫画图')
        st.image(custom_cartonized_image, caption=f"漫画图", use_container_width=True)

    with c2:
        st.subheader('灰度漫画图')
        st.image(custom_cartonized_image_gray, caption=f"灰度漫画图", use_container_width=True)

        st.subheader('定制化图像')
        st.image(stylizated_image, caption=f"定制化图像", use_container_width=True)

    with c3:
        st.subheader('铅笔风格灰度图')
        st.image(sketch_gray, caption=f"铅笔风格灰度图", use_container_width=True)

        st.subheader('铅笔风格轮廓图')
        st.image(sketch_color, caption=f"铅笔风格轮廓图", use_container_width=True)

else:
    st.warning("请上传要处理的图像！")