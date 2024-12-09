from moviepy import VideoFileClip
import streamlit as st
import struct

st.set_page_config(layout="wide", page_title="在线视频转GIF动画工具")

#获取视频时长信息
def get_video_duration(video_file):
    with open(video_file,'rb') as fp:
        data = fp.read()
    index = data.find(b'mvhd') + 4
    time_scale = struct.unpack('>I', data[index+13:index+13+4])
    durations  = struct.unpack('>I', data[index+13+4:index+13+4+4])
    duration = durations[0] / time_scale[0]
    return duration

#下载按钮效果设置
css = """<style>
.stDownloadButton>button {
    background-color: #0099ff;
    color:#ffffff;
}

.stDownloadButton>button:hover {
    background-color: #00ff00;
    color:#ffffff;
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

#隐藏按钮及底部链接
sysmenu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(sysmenu,unsafe_allow_html=True)

#设置要选择的16:9黄金分辨率和每秒要抽取的帧数
fenbianlv = st.sidebar.selectbox("请选择要设置的GIF图片分辨率",("1280×720","960×540","854×480","320×180","720×405","640×360","480×270"))
zhenshu = st.sidebar.slider('每秒抽取帧数', min_value=5, max_value=15, value=10, step=1)

if fenbianlv == "1280×720":
    set_fenbianlv=(1280,720)
elif fenbianlv == "960×540":
    set_fenbianlv=(960,540)
elif fenbianlv == "854×480":
    set_fenbianlv=(854,480)
elif fenbianlv == "720×405":
    set_fenbianlv=(720,405)
elif fenbianlv == "640×360":
    set_fenbianlv=(640,360)
elif fenbianlv == "320×180":
    set_fenbianlv=(320,180) 


file = st.file_uploader("请上传你要处理的mp4视频文件", type=["mp4"])


if file is not None:
    try:
        time = get_video_duration(file.name)
        #设置裁剪视频的起止时间段
        middle_time = st.sidebar.slider('请选择要裁剪的视频起始时间段',0.0, round(time,1), (round(time,1)/3, round(time,1)/2))

        st.sidebar.subheader("上传的视频")
        st.sidebar.video(file)

        clip =VideoFileClip(file.name).subclip(middle_time[0],middle_time[1]).resize((set_fenbianlv))
        clip.write_gif("movie.gif",fps=zhenshu)

        st.image("movie.gif")

        with open("movie.gif", "rb") as giffile:
            btn = st.download_button(
                label="点我下载生成的动图",
                data=giffile,
                file_name="生成的动图.gif",
                mime="image/gif"
        )

    except RuntimeError:
        st.warning("GIF文件大小超过限制，分辨率或帧数过高，请调低")