import streamlit as st
from PIL import Image
st.title("實驗3.伯努利文氏管實驗")

st.write("實驗目的:驗證伯努利定律，即流體速度與壓力之間的反比關係。觀察並測量不同流速下，流體在不同管道截面（寬窄處）中的壓力變化。")
st.write("實驗設備:文氏管、壓力計、流量計、水、泵浦裝置")
st.write("實驗步驟:1.設備準備 2.測量並設置流量 3.測量壓力 4.記錄數據")

# 在這裡添加實驗一的具體內容，如圖表、數據等
st.video("picture/1.mp4")

image = Image.open('picture/4.jpg')
st.image(image, caption='圖片1')
image = Image.open('picture/5.jpg')
st.image(image, caption='圖片2')