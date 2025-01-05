import streamlit as st
from PIL import Image
st.title("實驗5.溫度與散熱實驗")

file_paths = {
    "doc": "file/第11組 實驗5.溫度與散熱實驗.doc",
    "pdf": "file/第11組 實驗5.溫度與散熱實驗.pdf",
    "xls": "file/第11組 實驗5.溫度與散熱實驗.xls"
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

create_download_button(file_paths["doc"], "第11組 實驗5.溫度與散熱實驗.doc", "application/msword")  # doc 檔案
create_download_button(file_paths["pdf"], "第11組 實驗5.溫度與散熱實驗.pdf", "application/pdf")   # pdf 檔案
create_download_button(file_paths["xls"], "第11組 實驗5.溫度與散熱實驗.xls", "application/vnd.ms-excel")  # xls 檔案

st.markdown("""
### 一、實驗目的
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;透過不同電壓(V)獲取不同功率(W)，觀察光對於溫度的變化，所得到照度的數據在填入表中，以得出結果。
### 二、儀器與設備
1. T-type熱電偶線數條
2. 水銀溫度計乙支
3. 加熱片乙片
4. 鋁合金散熱片乙個
5. 導熱膏乙罐(共用)
6. 多功能電表(FLUKE 87-5)乙台
7. 多功能電表(FLUKE 287)乙台
8. 直流電源供應器(Agilent U8002A)兩台
9. 三孔延長線乙條
10. 銲槍乙支(含銲錫及耗材、電線等)
11. 照度計乙台
""")
col1, col2, col3 = st.columns(3)
with col1:
    image = Image.open('picture/27.jpg')
    st.image(image, caption='圖1.電壓表')
with col2:
    image = Image.open('picture/28.jpg')
    st.image(image, caption='圖2.量測照度光量子計')
with col3:
    image = Image.open('picture/29.jpg')
    st.image(image, caption='圖3.功率計')
st.markdown("### 三、實驗原理")
image = Image.open('picture/30.jpg')
st.image(image)
st.markdown("""
### 四、實驗步驟
####加熱片與溫度量測:
1. 通10W電源，以TC量測溫度值並記錄於表上
#### 散熱片量測與熱阻計算:
1. 將散熱片塗抹導熱膏後貼附於加熱片上
2. 打開電源供應器之電源開關，依照實驗表格之數值設定電流I之大小，並以兩台多功能電表(FLUKE 87-5)K-type熱電偶線，同時量測散熱片上鰭片與底座之溫度，等到溫度穩定後將所得數據記錄於表格中。
#### LED照明散熱：LED熱逸散因子實驗量測:
1. 利用焊槍將LED正負(+/-)兩端接腳分別連接一條電線。
2. 將LED正(+)接腳一端接電源供應器之正極，另一端負(-)接腳接電源供應器之負極。
3. 打開電源供應器之電源開關，依照實驗表格之數值設定電流I之大小，並以兩台多功能電表(FLUKE 87-5)K-type熱電偶線，同時量測LED上下兩面之溫度，等到溫度穩定後將所得數據記錄於表格中。
4. 在量測溫度之同時，以照度計量測照度值，並記錄於表格中。
5. 依照表格中之公式計算其餘項目之數值，完成整份表格。
6. 將LED貼緊於HS之平面端，注意K-type熱電偶線之結球必須剛好保持在上下兩面之間微微接觸，以量測得此位置之溫度值。
7. 重覆步驟(3)-(5)，完成所有電流I設定值之實驗量測，將數據記錄於表格中。
### 五、實驗結果
實驗數據:
""")
image = Image.open('picture/31.jpg')
st.image(image)
st.write("第一次實驗:")
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/32.jpg')
    st.image(image)
with col2:
    image = Image.open('picture/33.jpg')
    st.image(image)
st.write("第二次實驗:")
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/34.jpg')
    st.image(image)
with col2:
    image = Image.open('picture/35.jpg')
    st.image(image)
st.write("第三次實驗:")
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/36.jpg')
    st.image(image)
with col2:
    image = Image.open('picture/37.jpg')
    st.image(image)
st.video("picture/2.mp4")
st.video("picture/3.mp4")