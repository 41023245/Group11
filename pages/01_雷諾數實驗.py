import streamlit as st
from PIL import Image
import pandas as pd
st.title("實驗1.雷諾數實驗")

file_paths = {
    "docx": "file/第11組 實驗1.雷諾數實驗.docx",
    "pdf": "file/第11組 實驗1.雷諾數實驗.pdf",
    "xls": "file/第11組 實驗1.雷諾數實驗.xls"
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

create_download_button(file_paths["docx"], "第11組 實驗1.雷諾數實驗.docx", "application/msword")  # doc 檔案
create_download_button(file_paths["pdf"], "第11組 實驗1.雷諾數實驗.pdf", "application/pdf")   # pdf 檔案
create_download_button(file_paths["xls"], "第11組 實驗1.雷諾數實驗.xls", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")  # xlsx 檔案
st.write("### 一、實驗目的")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;以墨汁流入透明之壓克力管流中，觀察流體在管路中流動的情形，並配合計算出")
st.write("### 二、儀器與設備 ")
image = Image.open('picture/55.jpg')
st.image(image, caption='圖1.雷諾數儀器構造')
data = {
    "名稱": ["套管式測試管", "點滴液瓶", "機架", "節流閥", "內管"],
    "材質規格": ["壓克力", "玻璃 500℃", "SS41L型銅銲接", "透明壓克力", "透明壓克力"],
    "數量": [1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)
df.index += 1  
st.table(df)
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本套儀器是由一透明之壓克力製內外雙套管、機架台座、點滴液瓶、進出口閥、洩水閥及溢水管等和管路連接而成，詳細構造如圖一所示。")
data = {
    "名稱": ["外套管直徑", "內套管直徑"],
    "尺寸": ["150mm", "25mm"]
}
df = pd.DataFrame(data)
df.index += 1  
st.table(df)
st.write("### 三、實驗原理") 
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在研究流體力學的過程中，我們會遇到為數不少的無因次參數，如 Re、Fr、Ma 等，但其中最為大家所熟知的則為 Re，即雷諾數。")
image = Image.open('picture/56.jpg')
st.image(image)
st.markdown("""
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;層流、擾流及過渡區之流線圖現若再度加快流速，可發現整個流場呈擾動現象(圖 2c)，此即所謂的擾流。一般而言，當 Re<2300 時，流場為層流，Re>4000 時為擾流，2300<Re<4000 時則為轉換區。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本實驗旨在使同學由實驗中觀察層流、擾流、轉換區流場之不同，且驗証雷諾數與流場間之關係。在雷諾數之計算上，只要測得流量 Q 及管徑 D，則由 V = Q/A ，及已知之流體性質 及 即可求得所需的 Re。
### 四、實驗步驟 
1. 墨水加水稀釋（約1：5）後裝入點滴液瓶內並裝置在儀器上端。  
2. 打開進水口閥及內管出水口閥，並將進出口流量控制在穩定流動狀 態(即外管水位維持在某一固定位置不變)。 
3. 將墨水之控制閥打開讓墨水穩定的滴入套筒中。 
4. 觀察墨水於管路中流動的情形(層流、紊流或於臨界區域)同時用 量杯(或水筒)量取流量並用碼錶確實測量時間(秒)將此等資料數據(流動情形、流量、測量時間)詳細計錄。 
5. 改變流量(由小到大)至少取五種不同的流量，以確實觀察由層流變化到完全紊流的情形。 
6. 實驗結束，將墨水關閉，且洗淨針頭後置淸水桶內，以免墨汁乾化，堵塞針孔，同時開大進水閥(出口閥維持略開)讓淸水充滿套筒內 部(此時會有多餘的水從溢水口流出)讓其自然循環數分鐘將墨汁 淸洗掉。 
7. 最後再將進水閥關閉，並打開出口閥和洩水閥將水排乾。 
8. 擦淨儀器本身及四周地板。 
### 五、實驗結果與討論 
1. 依實驗之觀察和計算結果，試判斷層流和紊流的臨界區域値在何種範圍。 
2. 爲何在靠近管路之進出口端點處，流動均呈不穩定現象。  
3. 試繪出層流和紊流之流動情形？並說明層流和紊流時水分子的流動情形。 
4. 依據實驗數據及觀察結果，本實驗和一般衆多書籍所敍述之數據是否符合？若不符合，你認爲原因出在那裡，應如何改善。 
""")
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/57.jpg')
    st.image(image)
with col2:
    image = Image.open('picture/58.jpg')
    st.image(image)
st.markdown("""
雷諾數實驗報告
- 水溫:26℃
- 密度(ρ):1000kg/m3
- 黏度係數 :0.001N-s/m2
- 內管直徑(D)25mm
- 截面積(A):0.0005 m2 
""")
image = Image.open('picture/59.jpg')
st.image(image)
st.markdown("""
1. 雷諾數公式<u>(ρ×V×D)/μ3</u>   
2. Re之物理意義<u>慣性力與黏性力之比值。</u>  
3. 一般而言，Re大於<u>4000</u> 爲擾流，小於<u>2300層流</u> 。 
4. 推導Re之單位：<u>((kg×m)/S^2)/N</u> 
5. 以實驗室之 D=2.5cm 而言，水之 μ 1×10-3N-s/m2，則在層流之狀況，其 V 應小於<u>0.092</u> 
6. 同上，在擾流之情況，V應大於<u>0.16</u> 
7.  若管徑2cm，Q＝10l/min，請問此時之Re＝<u>10600</u> ，其流場應爲<u>擾流</u> 
8. Re數之功用<u>是用來判斷流體流動的型態</u> 。 
""", unsafe_allow_html=True)