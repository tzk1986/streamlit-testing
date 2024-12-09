import streamlit as st
import random as _random
import string

st.set_page_config(page_title="密码生成器", page_icon="🔑")

st.markdown(
    "<h1 style='text-align: center; color: blue;'>密码生成器</h1>",
    unsafe_allow_html=True,
)


length = st.number_input("请选择你要设置的密码长度", min_value=10, max_value=100)

title = st.write("请勾选生成的密码包含的类型")


cb1 = st.checkbox("数字")
cb2 = st.checkbox("字母")
cb3 = st.checkbox("特殊字符($%?!)")


empty = st.empty()

if cb1 == True:
    numbers = "0123456789"
else:
    numbers = ""
if cb2 == True:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"
else:
    letters = ""
if cb3 == True:
    symbols = string.punctuation
else:
    symbols = ""
if cb1 and cb1 and cb3 == None:
    st.warning("请至少勾选1种类型")

all = letters + str(numbers) + symbols


# 生成密码列表

try:
    temp = _random.sample(all, length)
except ValueError:
    pass

try:
    temp2 = _random.sample(all, length)
except ValueError:
    pass

try:
    temp3 = _random.sample(all, length)
except ValueError:
    pass

try:
    temp4 = _random.sample(all, length)
except ValueError:
    pass


# 从列表中取出元素组成密码
try:
    password = "".join(temp)
except ValueError and NameError:
    pass
try:
    password2 = "".join(temp2)
except ValueError and NameError:
    pass
try:
    password3 = "".join(temp3)
except ValueError and NameError:
    pass
try:
    password4 = "".join(temp4)
except ValueError and NameError:
    pass

# 打印密码
try:
    st.code(password)
    st.code(password2)
    st.code(password3)
    st.code(password4)

except ValueError and NameError:
    st.warning("请至少勾选1种类型")
