import requests
import re
import streamlit as st
import langid

st.set_page_config(page_title="多语种翻译工具", page_icon="📖", layout="wide")

sysmenu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(sysmenu,unsafe_allow_html=True)

def translate(text, target_language, key):
    url = 'https://translate.google.cn/_/TranslateWebserverUi/data/batchexecute?rpcids=MkEWBc&f.sid=-2984828793698248690&bl=boq_translate-webserver_20201221.17_p0&hl=zh-CN&soc-app=1&soc-platform=1&soc-device=1&_reqid=5445720&rt=c'
    headers = {
      'origin': 'https://translate.google.cn',
      'referer': 'https://translate.google.cn/',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
      'x-client-data': 'CIW2yQEIpbbJAQjEtskBCKmdygEIrMfKAQj2x8oBCPfHygEItMvKAQihz8oBCNzVygEIi5nLAQjBnMsB',
      'Decoded':'message ClientVariations {repeated int32 variation_id = [3300101, 3300133, 3300164, 3313321, 3318700, 3318774, 3318775, 3319220, 3319713, 3320540, 3329163, 3329601];}',
      'x-same-domain': '1'
      }
    data = {'f.req': f'[[["MkEWBc","[[\\"{text}\\",\\"auto\\",\\"{target_language}\\",true],[null]]",null,"generic"]]]'}
    res = requests.post(url, headers=headers, data=data).text
    temp = re.findall(r'\\(.*?)\\', res)
    #st.write(temp)
    yiwen=str(temp[key]).replace('"','')
    return st.success(yiwen)


st.header("多语种翻译工具")
st.info("说明：输入中文得英文，输入英文得中文，输入韩语、日语、俄语、法语、葡萄牙语、西班牙语将得到中文")
text = st.text_input("请输入你要翻译的内容,可输入中文或英文")

if len(text)>0:
    #st.write(langid.classify(text)[0])
    if langid.classify(text)[0] == "en":#英语
        translate(text,"zh",3)
    elif langid.classify(text)[0] == "zh":#中文
        translate(text,"en",3)
    elif langid.classify(text)[0] == "ko":#韩语
        translate(text,"zh",4)
    elif langid.classify(text)[0] == "ja":#日语
        translate(text,"zh",5)
    elif langid.classify(text)[0] == "ru":#俄语
        translate(text,"zh",4)
    elif langid.classify(text)[0] == "fr":#法语
        translate(text,"zh",4)
    elif langid.classify(text)[0] == "ku":#葡萄牙语
        translate(text,"zh",4)
    elif langid.classify(text)[0] == "pt":#西班牙语
        translate(text,"zh",4)