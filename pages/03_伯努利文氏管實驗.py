import streamlit as st
from PIL import Image
st.title("實驗3.伯努利文氏管實驗")

file_paths = {
    "doc": "file/第11組 實驗3. 伯努利文氏管實驗.doc",
    "pdf": "file/第11組 實驗3. 伯努利文氏管實驗.pdf"
}

def create_download_button(file_path, label, mime_type):
    with open(file_path, "rb") as f:
        file_content = f.read()
    st.download_button(
        label=label,
        data=file_content,
        file_name=file_path.split("/")[-1],  # 檔案名稱
        mime=mime_type
    )

create_download_button(file_paths["doc"], "第11組 實驗3. 伯努利文氏管實驗.doc", "application/msword")  # doc 檔案
create_download_button(file_paths["pdf"], "第11組 實驗3. 伯努利文氏管實驗.pdf", "application/pdf")   # pdf 檔案

st.markdown("""
### 一、實驗目的
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;目的是為了驗證柏努力定理在流體中的應用，特別是在流速與壓力之間的關係。藉由文氏管的壓力與速度的量測，來檢驗伯努利方程式能量守恆與質量守恆的概念。
### 二、儀器與設備
1. 控制箱與操作面板
2. 水柱壓力計
3. 標準流量產生器用AMCA噴嘴 
4. 標準流量產生裝置
""")
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/2.jpg')
    st.image(image, caption='圖1. 控制箱與操作面板')
with col2:
    image = Image.open('picture/3.jpg')
    st.image(image, caption='圖2. 水柱壓力計')
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/38.jpg')
    st.image(image, caption='圖3. 標準流量產生器用AMCA噴嘴')
with col2:
    image = Image.open('picture/39.jpg')
    st.image(image, caption='圖4. 標準流量產生裝置')
st.markdown("""
### 三、實驗原理
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;伯努利定理描述流體在流動過程中的壓力、流速和位能之間的關係。文氏管是一種流體管道設計，其特徵是中央部分收縮，並在入口和出口處直徑較大。通過伯努利定理，當流體進入管道的收縮部分時，流速會增加，而靜壓力會下降；反之，在出口處流速減少，壓力回升。實驗過程中，通過測量管道不同位置的壓力差，可以觀察流速和壓力變化的關係，驗證伯努利定理。
### 四、實驗步驟
1. 根據噴嘴上標示的流量範圍，選擇所需風量的噴嘴。
2. 開啟標準風量產生裝置兩邊的扣鉗，將腔室分離。
3. 於標準流量產生器安裝噴嘴，將噴嘴板定位孔徑對準定位銷，並請小心安裝。
4. 將噴嘴腔室往前輕推，關閉噴嘴前後腔室。
5. 將噴嘴腔室兩側固定扣拑扣上，以固定噴嘴腔室。
6. 確認裝置內無風後，將壓力表歸零。
7. 歸零方式為按下AZ按鍵兩次，直到右上角AZ燈亮起並數字顯示為0。
8. 順時針轉動輔助風機變頻器旋鈕，並觀察且記錄噴嘴前後差壓。
### 五、實驗結果
起始數值為0
""")
image = Image.open('picture/40.jpg')
st.image(image)
st.write("#### 第一次實驗:操作數值為5")
image = Image.open('picture/41.jpg')
st.image(image)
image = Image.open('picture/42.jpg')
st.image(image)
st.write("由左至右文試管刻度為:")
st.write("22、21、20、20、20、20、20、20、22、20")
st.write("#### 第二次實驗:操作數值為10")
image = Image.open('picture/43.jpg')
st.image(image)
image = Image.open('picture/44.jpg')
st.image(image)
st.write("由左至右文試管刻度為:")
st.write("22、21、20、20、20、20、19、18、21、20")
image = Image.open('picture/45.jpg')
st.image(image)
st.write("由左至右文試管刻度為:")
st.write("30、30、31、32、30、30、27、25、24、22")
st.write("#### 第三次實驗:操作數值為20")
image = Image.open('picture/46.jpg')
st.image(image)
image = Image.open('picture/47.jpg')
st.image(image)
st.write("由左至右文試管刻度為:")
st.write("12、10、8、5、4、3、1、0、2、2")
image = Image.open('picture/48.jpg')
st.image(image)
st.write("由左至右文試管刻度為:")
st.write("38、62、65、67、66、60、42、30、21、17")


st.video("picture/1.mp4")