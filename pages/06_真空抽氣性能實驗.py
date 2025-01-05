import streamlit as st
from PIL import Image

st.title("實驗6.真空抽氣性能實驗")

file_paths = {
    "docx": "file/第11組 實驗6.真空抽氣性能實驗.docx",
    "pdf": "file/第11組 實驗6.真空抽氣性能實驗.pdf"
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

create_download_button(file_paths["docx"], "第11組 實驗6.真空抽氣性能實驗.docx", "application/msword")  # doc 檔案
create_download_button(file_paths["pdf"], "第11組 實驗6.真空抽氣性能實驗.pdf", "application/pdf")   # pdf 檔案

st.markdown("""
### 一、	實驗目的
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;真空抽氣性能實驗的主要目的是評估真空系統的性能和效率，並確保其能達到特定應用所需的真空度。此實驗的結果能幫助改善真空系統的設計，優化其運行參數，並確保其能在實際應用中可靠地達到要求的真空度和抽氣速度。
### 二、	儀器與設備
1.	自製真空系統乙套
2.	水氣Trap乙個
3.	計時器乙個
4.	水盤乙個
5.	吸水紙數張
6.	精密天平乙台
""")
col1, col2, col3 = st.columns(3)
with col1:
    image = Image.open('picture/15.jpg')
    st.image(image, caption='圖1.真空腔體')
with col2:
    image = Image.open('picture/16.jpg')
    st.image(image, caption='圖2.機械幫浦')
with col3:
    image = Image.open('picture/17.jpg')
    st.image(image, caption='圖3.真空計')
st.markdown("""
### 三、實驗原理
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;真空幫浦之功能是將一特定空間之氣體抽除，使氣體密度降低，達到某一壓力狀態。但是，氣體在真空系統中之流動特性隨壓力之不同而有很大差異。因此，對不同壓力範圍必須依相對應之抽氣原理來設計不同型態幫浦。同時，針對特定抽氣要求，需組合搭配不同性能與型態之真空幫浦來使用，才能達到有效又經濟之真空抽氣目的。
""")
image = Image.open('picture/18.jpg')
st.image(image, caption='圖4.實驗器材配置')
st.markdown("""
### 四、實驗步驟
1.旋轉閥門(約16圈)。
2.將真空腔體蓋子蓋上，管路末端出口關上，開啟幫浦開始抽真空  (開啟蓋子打不開表示實驗正確)。
3.觀察測量器上的數值，待數值穩定後，將閥門轉10圈至半開，重複1、2步驟。
4.查看數據並記錄。
### 五、實驗結果與討論
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由此實驗可知，真空度越大表示越接近大氣壓力，真空度月小理論上越接近真空狀態。以下是詳細解釋：
1.	真空等級的理解 
高壓（低真空）:當壓力值較大（例如 760 Torr,101.3 kPa)時，表示系統內的氣體較多，真空度較低,抽氣效果較弱。
低壓（高真空）： 當壓力值較小（例如 10⁻³ Torr,1 mPa)時,表示系統內的氣體較少，真空度較高，接近理想真空。
2.	真空技術中的壓力單位 
Torr（托）： 真空技術中常用單位
一. 1 Torr ≈ 133.3 帕斯卡(Pa)。
二.帕斯卡(Pa): 國際單位制壓力單位，真空工程中也常用。
三.Micron(微米汞柱): 1 微米汞柱 = 0.001 Torr,用於非常細微的真空測量。
""")