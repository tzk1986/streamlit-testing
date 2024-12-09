import streamlit as st  # 导入 Streamlit 库，用于创建 Web 应用
import pandas as pd  # 导入 Pandas 库，用于数据处理
import numpy as np  # 导入 NumPy 库，用于数值计算

# 设置应用的标题
st.title('Uber pickups in NYC')

# 定义日期列的名称
DATE_COLUMN = 'date/time'
# 数据的 URL 地址
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# 使用缓存装饰器，优化数据加载
@st.cache_data
def load_data(nrows):
    # 从 URL 加载数据，限制行数为 nrows
    data = pd.read_csv(DATA_URL, nrows=nrows)
    # 将列名转换为小写
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # 将日期列转换为 datetime 格式
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# 显示加载数据的状态
data_load_state = st.text('Loading data...')
# 调用加载数据的函数
data = load_data(10000)
# 数据加载完成后更新状态
data_load_state.text("Done! (using st.cache_data)")

# 创建一个复选框，允许用户选择是否显示原始数据
if st.checkbox('Show raw data'):
    st.subheader('Raw data')  # 显示原始数据的子标题
    st.write(data)  # 显示原始数据

# 显示每小时接送次数的子标题
st.subheader('Number of pickups by hour')
# 计算每小时的接送次数
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
# 使用条形图显示接送次数
st.bar_chart(hist_values)

# 创建一个滑块，允许用户选择小时（0-23）
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
# 根据选择的小时过滤数据
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# 显示地图的子标题，标明选择的小时
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# 在地图上显示过滤后的接送数据
st.map(filtered_data)