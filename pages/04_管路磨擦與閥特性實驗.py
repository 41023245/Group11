import streamlit as st
from PIL import Image

st.title("實驗4.管路磨擦與閥特性實驗")

file_paths = {
    "doc": "file/第11組 實驗4.管路磨擦與閥特性實驗.doc",
    "pdf": "file/第11組 實驗4.管路磨擦與閥特性實驗.pdf",
    "xlsx": "file/第11組 實驗4.管路磨擦與閥特性實驗.xlsx"
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

create_download_button(file_paths["doc"], "第11組 實驗4.管路磨擦與閥特性實驗.doc", "application/msword")  # doc 檔案
create_download_button(file_paths["pdf"], "第11組 實驗4.管路磨擦與閥特性實驗.pdf", "application/pdf")   # pdf 檔案
create_download_button(file_paths["xlsx"], "第11組 實驗4.管路磨擦與閥特性實驗.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")  # xlsx 檔案
st.markdown("""
### 一、	實驗目的
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本實驗目的就在於測量液體的黏滯係數,並觀察黏滯係數與溫度變化的關係。
#### 儀器與設備
1. 測黏滯定儀
2. 燒杯
3. 測量電壓機
4. 恆溫箱
""")
col1, col2, col3 = st.columns(3)
with col1:
    image = Image.open('picture/19.jpg')
    st.image(image, caption='圖1. 測黏滯定儀')
with col2:
    image = Image.open('picture/20.jpg')
    st.image(image, caption='圖2.燒杯')
with col3:
    image = Image.open('picture/21.jpg')
    st.image(image, caption='圖3.測量電壓機')
st.markdown("""
### 二、	實驗原理
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;黏滯性是流體的性質之一,產生黏滯的原因在於分子的內聚力及附著力。 物體在液體中移動時,因為表面有附著力以及摩擦力而形成阻力,而不同的液體有不同的阻力,經由計算可以了解每一種液體的黏滯係數。黏滯力 f 和施力 F 方向相反，黏滯力 f 的 大小和平行板的面積 A 以及平行板的相對速度 dv 成正比，和平 板間的距離 dr 成反比。)
""")
image = Image.open('picture/22.jpg')
st.image(image)
st.markdown("""
### 四、實驗步驟
#### 準備階段:
1. 安裝黏度計:將黏度計安裝在穩固的平台上，調整水平，使氣泡位於水準儀的黑圈中。打開黏度計電源，確保設備正常運作。
2. 準備樣品與恆溫箱:樣品注入恆溫箱，啟動電源與冷凍開關，將恆溫箱的溫度設置為20℃，等待溫度穩定。
3. 準備一個600ml標準燒杯，將樣品加入至指定高度，確保液體足以覆蓋轉針的測量範圍。完成黏度計的參數設置，並安裝護架。
#### 測量階段:
4. 安裝轉針:轉針小心地裝入黏度計中，確保轉針垂直並完全浸入樣品液體中。
設定轉針參數與測量條件。設定適當的轉針號碼和轉速組合，確保扭矩百分比讀數在10-100%範圍內。
""")
image = Image.open('picture/23.jpg')
st.image(image)
image = Image.open('picture/24.jpg')
st.image(image)
st.markdown("### 五、實驗結果")
st.markdown("#### 實驗數據:")
image = Image.open('picture/25.jpg')
st.image(image)
st.markdown("#### 實驗:")
image = Image.open('picture/26.jpg')
st.image(image)