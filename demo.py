import datetime
import time
import streamlit as st
import pandas as pd
import numpy as np

# 设置全局属性
st.set_page_config(
    page_title='我是标题',
    page_icon=' ',
    layout='wide'
)

sidebar = st.sidebar
sidebar.title('欢迎来到我的应用')
sidebar.markdown('---')
sidebar.markdown('这是它的特性：\n- feature 1\n- feature 2\n- feature 3')

# st.experimental_set_query_params

## 默认渲染到主界面
st.title('这是主界面')
st.info('这是主界面内容')


# markdown
st.markdown('Streamlit Demo')

# 设置网页标题
st.title('一个傻瓜式构建可视化 web的 Python 神器 -- streamlit')

# 展示一级标题
st.header('1. 安装')

st.text('和安装其他包一样，安装 streamlit 非常简单，一条命令即可')
code1 = '''pip3 install streamlit'''
st.code(code1, language='bash')


# 展示一级标题
st.header('2. 使用')

# 展示二级标题
st.subheader('2.1 生成 Markdown 文档')

# 纯文本
st.text('导入 streamlit 后，就可以直接使用 st.markdown() 初始化')

# 展示代码，有高亮效果
code2 = '''import streamlit as st
st.markdown('Streamlit Demo')'''
st.code(code2, language='python')


df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('第%d列' % (i+1) for i in range(5))
)

st.table(df)

st.dataframe(df.style.highlight_max(axis=0))


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.area_chart(chart_data)

st.bar_chart(chart_data)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [31.23, 121.47],
    columns=['lat', 'lon']
)
st.map(df)

st.button('Say hello')
st.download_button('Download CSV', df.to_csv(), file_name='large_df.csv')
st.file_uploader("Upload CSV")
st.checkbox('I agree')
st.radio('Pick your favorite movie', ['Gone with the Wind', 'Star Wars', 'The Big Lebowski'])
st.selectbox('Pick your favorite movie', ['Gone with the Wind', 'Star Wars', 'The Big Lebowski'])
st.multiselect('Pick your favorite movie', ['Gone with the Wind', 'Star Wars', 'The Big Lebowski'])
st.slider('Pick a number', 0, 100)
size = st.select_slider('Pick a size', options=['S', 'M', 'L'])
st.write("size是", size)
st.text_input('First name')
st.text_area('Email')
st.number_input('Pick a number')
st.date_input('Your birthday',min_value=datetime.date(1950, 1, 1))
st.time_input('Meeting time', step=60)
st.color_picker('Choose your favorite color')


start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
    value=("red", "blue"),
)
st.write("You selected wavelengths between", start_color, "and", end_color)


st.image("https://i.imgur.com/vrsJWhJ.jpg", width=400,caption="测试图片")


col01, col02 = st.columns([1, 1])
with col01:  # 滑块
    age = st.slider('滑块', 0, 130, 25)

with col02:  # 颜色选择器
    color = st.color_picker('选择颜色', '#f95700')
    st.write('当前颜色：', color)


col03, col04 = st.columns([1, 1])
with col03:  # CSV 文件上传
    uploaded_files = st.file_uploader("上传CSV文件", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

with col04:  # 单项选择
    genre = st.radio(
    "选择一个你喜欢的宠物",
    ('猫猫 ', '猪猪 ', '旺财 '))


col05, col06 = st.columns([1, 1])
with col05:  # 数据图
    import pandas as pd
    import numpy as np
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"])

    st.bar_chart(chart_data)
with col06:  # 日期选择器
    from datetime import datetime
    st.date_input('日期选择器', datetime.today().date())

# 对容器进行设定，这个就是用with，
with st.container():
   st.write("This is inside the container")
 
   # 可用于接受 "类文件 "对象的任何地方：
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")


# 对容器进行设定，这个就是用with，
c1=st.container()

with c1:
    st.write("This is inside the container")

    # 可用于接受 "类文件 "对象的任何地方：
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")
c1.write("This is inside the container the second time!")


# 先设定一个标题
@st.experimental_dialog("Cast your vote")

# 定义一个投票系统
def vote(item):
#写入问题，
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
#这里如果点击发送就会展示
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()
# 这里定义初始界面，进行分析
if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
#这里我们将结果输入出你选的内容，并通过输入的的原因展示出来
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"


placeholder = st.empty()

# 用一些文本替换占位符：
placeholder.text("Hello")

# 用图表替换文本：
placeholder.line_chart({"data": [1, 5, 2, 6]})

# 用几个元素替换图表：
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")

# 清除所有这些元素：
placeholder.empty()


tab1, tab2 = st.tabs(["image_background", "image_text_extract"])

with tab2:

    st.write("tab2")
    st.markdown(
        """
        # 静夜思
        床前**明月**光，疑是地上霜。\n
        举头望**明月**，低头思故乡。
        """
    )

    st.text(
        """
    静夜思
    床前明月光，疑是地上霜。
    举头望明月，低头思故乡。
    """
    )
    
    st.markdown('**以下为打印的代码：**')
 
    st.code('''
    def bubble_sort(arr):
        n = len(arr)
        # 遍历所有数组元素
        for i in range(n):
            # 最后 i 个元素已经排好序，不需要再比较
            for j in range(0, n-i-1):
                # 如果元素比下一个元素大，则交换它们
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    # 示例使用
    if __name__ == "__main__":
        # 测试数据
        example_list = [64, 34, 25, 12, 22, 11, 90]
        print("原始数组:", example_list)
        # 调用冒泡排序函数
        bubble_sort(example_list)
        print("排序后的数组:", example_list)
    ''', language='python')
    # 使用empty会导致后续代码都等待，直到empty结束，才会继续执行
    # with st.empty():
    #     for seconds in range(60):
    #         st.write(f"⏳ {seconds} seconds have passed")
    #         time.sleep(1)
    #     st.write("✔️ 1 minute over!")


with tab1:
    #插入一个图表
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
    
    #设定一个扩张器在图表中
    with st.expander("See explanation"):
        st.write('''
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        ''')
        st.image("https://static.streamlit.io/examples/dice.jpg")
        
    with st.popover("Open popover"):
        st.markdown("Hello World  ")
        name = st.text_input("What's your name?")
 
    #不在内部写入
    st.write("Your name:", name)


st.markdown("---")

# st.experimental_data_editor

col1, col2 ,col3= st.columns(3)
with col1:
   with st.form('Form1'):
        a=st.selectbox('选择一束花', ['康乃馨', '月季'], key=1)
        submitted1 = st.form_submit_button('点我提交')
        if submitted1:
           st.write(f'你选择了 {a}')

with col2:
    with st.form('Form2'):
        b=st.selectbox('选择一本书', ['黄河之水天上来', '我在北极光下'], key=2)
        submitted2 = st.form_submit_button('点我提交')
        if submitted2:
          st.write(f'你选择了 {b}')

with col3:
   with st.form('Form3'):
        c=st.selectbox('选择一个方向', ['向上', '向下'], key=3)
        submitted3 = st.form_submit_button('点我提交')
        if submitted3:
          st.write(f'你选择了 {c}')

file=st.file_uploader(label="请上传csv表格",help="仅支持csv格式")
if file is not None:
    df=pd.read_csv(file)
    st.info("原始表格信息如下：")
    st.write(df)
    header=df.columns.to_list()
    a=st.selectbox("请选择要对原始表格的哪一列做透视",(header))
    b=st.selectbox("请选择要对原始表格的哪一列做数据处理",(header))
    if a!=b:
        c=st.selectbox("请选择要对原始表格的值列做什么处理",('sum','max','min','count'))
        st.success("数据透视表结果如下：")
        df1=df.pivot_table(index=[a],values=[b],aggfunc=c)
        st.write(df1)
        st.success("单独取出数据透视结果如下：")
        df2=df.pivot_table(index=[a],values=[b],aggfunc=c).iloc[[0],[0]].values
        st.write(int(df2))
    else:
        st.warning("你不能只选择对一列进行数据透视")

st.write("end")
