import streamlit as st

st.set_page_config(page_title="熱流力實驗", layout="wide")

st.title("熱流力實驗")

st.write("歡迎來到熱流力實驗報告。請從左側選單選擇要查看的實驗項目。")

# 不需要在這裡定義實驗項目列表，因為Streamlit會自動生成側邊欄