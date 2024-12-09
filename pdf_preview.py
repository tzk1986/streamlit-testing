import streamlit as st
import base64
st.set_page_config(layout="wide")
uploaded_file = st.file_uploader("上传pdf", type=["pdf"])

with st.expander("点我查看资料"):
    # 放PDF嵌入代码
    if uploaded_file is not None:
        base64_pdf = base64.b64encode(uploaded_file.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf">' 
        st.markdown(pdf_display, unsafe_allow_html=True)