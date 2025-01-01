import streamlit as st
import pandas as pd

st.set_page_config(page_title="熱流力實驗", layout="wide")

# 使用 HTML 進行置中
st.markdown("<h1 style='text-align: center;'>國立虎尾科技大學機械設計工程系</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>113 學年度『機械工程實驗(二)：熱流力實驗』</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>期末報告</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>指導老師：周榮源</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>班級:四設四乙</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>組別:第11組</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>組員:41023229陳濬祺<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;41023238黃嘉偉<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;41023244廖崇軒<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;41023245劉于綸<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;41023245劉昱辰</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>日期：中華民國 114 年 1 月 6 日</p>", unsafe_allow_html=True)

# 顯示表格上方的資訊，並置中
st.markdown("""
<div style="text-align: center;">
    <h3>機械工程實驗(二)：熱流力實驗</h3>
    <p><strong>學期團隊作業/專案設計</strong></p>
    <p>課號：0835 (四設計四乙)</p>
    <p>學年：113學年度第1學期</p>
    <p>題目：熱流力實驗報告</p>
    <p>組別：第11組</p>
    <p>成員：陳濬祺、黃嘉偉、廖崇軒、劉于綸、劉昱辰</p>
</div>
""", unsafe_allow_html=True)

# 創建表格數據
data = {
    "學號": ["41023229", "41023238", "41023244", "41023245", "41023245"],
    "姓名": ["陳濬祺", "黃嘉偉", "廖崇軒", "劉于綸", "劉昱辰"],
    "分工內容": ["協助實驗", "操作實驗", "分析資料", "網站製作", "製作報告"],
    "貢獻度": ["20%", "20%", "20%", "20%", "20%"]
}

# 創建 DataFrame 並重設索引
df = pd.DataFrame(data)
df.index += 1  # 索引從1開始

# 顯示表格
st.table(df)
st.markdown("<p style='text-align: center;'>完成日期：114 年 1 月 6 日</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>聲明</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>本人在此聲明，本設計作業皆由本人與同組成員共同獨立完成，並無其他第三者參與作業之進行，若有抄襲或其他違反正常教學之行為，自願接受該次成績以零分計。</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>同時本人亦同意在上述表格中所記載之作業貢獻度，並以此計算本次個人作業成績。</p>", unsafe_allow_html=True)