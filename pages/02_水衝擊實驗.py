import streamlit as st
from PIL import Image
import pandas as pd
st.title("實驗2.水衝擊實驗")

file_paths = {
    "docx": "file/第11組 實驗2.水衝擊實驗.docx",
    "pdf": "file/第11組 實驗2.水衝擊實驗.pdf",
    "xls": "file/第11組 實驗2.水衝擊實驗.xls"
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

create_download_button(file_paths["docx"], "第11組 實驗2.水衝擊實驗.docx", "application/msword")  # doc 檔案
create_download_button(file_paths["pdf"], "第11組 實驗2.水衝擊實驗.pdf", "application/pdf")   # pdf 檔案
create_download_button(file_paths["xls"], "第11組 實驗2.水衝擊實驗.xls", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")  # xlsx 檔案

st.markdown("""
### 一、實驗目的 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;瞭解流體流動時，其動量變化與其承受力量間之關係，以驗証動量方程式。 
### 二、儀器與設備
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;水衝擊實驗係由一水循環泵、驅動馬達、儲水槽、實驗台架、柏登壓力錶、流量控制閥、水衝擊台一套(包括有透明壓克力套筒、噴嘴、各種形式之衝擊檔板、動量平衡器)、以及三角形堰(流量計)、和稱重器等構成整套儀器，詳細構造如圖一所示。 
""")
image = Image.open('picture/49.jpg')
st.image(image, caption='圖1.水衝擊外觀及構造圖 ')
data = {
    "設備名稱": [
        "出口水壓計", "測量流速用水箱", "水量刻度表", "測量流速水箱之洩放閥", "儲水槽", "輪子", "離心泵及馬達",
        "進口閥", "進口水壓計", "機架底座", "浮沉式流量計", "馬達開關", "馬達速度控制錶", "流量控制閥", 
        "水衝擊器", "重量平衡器(秤重)", "平衡指標"
    ]
}
df = pd.DataFrame(data)
df.index += 1  # 索引從1開始
st.table(df)
st.write("[實驗儀器規格與尺寸] ")
data = {
    "項目": ["驅動馬達規格", "水循環泵規格", "測試元件"],
    "規格": [
        "電壓:110 伏特  頻率:60HZ  功率:0.12 仟瓦",
        "型式:離心式  揚程:3.0-13.7m  流量:11.4-54.5l/min(or 150-720 G.P.H)",
        "噴嘴:直徑 5mm 1 個 8mm 1 個  衝擊擋板:平板、45°錐形硯板、半球形硯板各1個"
    ]
}
df = pd.DataFrame(data)
df.index += 1  # 索引從1開始
st.table(df)
st.markdown("### 三、實驗原理")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;衝擊試驗之主要目的在驗証動量方程式。吾人知道動量方程式屬於流體力學四大方程式之一，其應用頗為廣泛，如衝動式水輪機之分析、各型彎管、噴嘴之受力分析等均有賴動量方程式的計算。至於各式離心泵、衝動式水輪機等亦需藉重經由動量方式推導出之動量矩方程式來分析，故吾人希望藉重此一實驗來加深讀者對動量方程式應用在流體力學的控制體積時，一般可表為下列之形式")
image = Image.open('picture/50.jpg')
st.image(image)
st.markdown("""
### 四、實驗步驟 
1. 將 110V 之電源連接妥當。 
2. 儲水槽加入之水量約九分滿。  
3. 將噴嘴及硯板裝入水衝擊器內。 
4. 將動量平衡器先預加上荷重約 350～450gms，使其壓縮彈簧約 80%之壓縮量(勿將彈簧完全壓縮，否則會產生很大的誤差〉，並將平衡指標切口對準與平板同高，此時需將試重之實際重量［包括容器、即杯子 ］計錄下來，此即為預負荷。 
5. 按下啟動馬達開關，並逐漸打開流量控制閥至某一特定流量。  
6. 同時衝擊水流對硯板產生衝擊，而將硯板上推至最高點。此時開始加入荷重，至平板回到原來之平衡位置為止，取下容杯重新稱重，即得總負荷。總負荷減去預負荷，所得之重量即為水對硯板之衝擊力。  
7. 逐漸打開流量控制閥（出口閥），以改變流量，重覆上述步驟，流量由小至大，至少取五種，並詳細記錄各值。  
8. 關閉電源，並將出口閥關閉。  
9. 依序更換噴嘴或硯扳，重覆 3～8 之步驟完成同樣之量測。  
10. 實驗結束，關閉電源，並將流量測量槽內之水排放至儲水槽。 
### 五、實驗結果與討論 
1. 討論硯板與噴嘴間之距離對硯板受力大小之影響。  
2. 討論在同流量之情況下，噴嘴直徑與硯板受力之關係。  
3. 繪製流速與硯板受力之關係圖，比較三種硯板之受力情形。  
4. 討論誤差大小與噴嘴直徑、硯板形狀間之關係。  
### 六、測驗題  
1. 水衝擊實驗在驗証 <u>動量</u> 方程式。  
2. 本實驗有幾種硯板可供實驗：<u>3</u>  
3. 本實驗有那幾種規格之噴嘴：<u>8mm</u> 、 <u>5mm</u> 。  
4. 在流量固定之下，使用同一硯板，配合那一個噴嘴衝擊力較大 <u>8mm</u> ，為什麼：<u>衝量大</u> 。  
5. 在同一流量和噴嘴，那一種硯板衝擊力最大 <u>半圓形</u> ， <u>45°圓錐形硯板</u> 硯板衝擊力最小，最大約為最小的 <u>3.125</u> 倍。  
6. 在流量固定下何種噴嘴與硯板之組合衝擊力最大：<u>8mm 半圓形</u> ，何種組合衝擊力最小：<u>5mm</u> ， <u>45°圓錐形硯板</u> 。前者約為後者的 <u>3.125</u> 倍。  
7. 1Kgw=<u>9.8</u> N。  
8. 推導ρQV所得到之單位：<u>N</u> 。〈取ρ為kg/m³, Q為m³/s, V為m/s〉  
9. 預負荷300gw，總負荷2800gw，Q=30l/min，噴嘴5mm作用在半圓形硯板，則實際負荷為 <u>2500</u> N ，理論衝擊力 <u>1270</u> N ， <u>49.2</u> ％。  
""", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/51.jpg')
    st.image(image)
with col2:
    image = Image.open('picture/52.jpg')
    st.image(image)
image = Image.open('picture/53.jpg')
st.image(image)
image = Image.open('picture/54.jpg')
st.image(image)