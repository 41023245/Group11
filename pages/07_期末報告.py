import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(page_title="熱流力實驗", layout="wide")

st.markdown("<h1 style='text-align: center;'>國立虎尾科技大學機械設計工程系</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>113 學年度『機械工程實驗(二)：熱流力實驗』</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>期末報告</h2>", unsafe_allow_html=True)
st.markdown(
    "<h2 style='text-align: center; color: red;'>一、創新夾持裝置機械設計</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<h2 style='text-align: center; color: red;'>二、環境量測與控制裝置機械設計</h2>",
    unsafe_allow_html=True
)
st.markdown("<p style='text-align: center;'>指導老師：周榮源</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>班級:四設四乙</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>組別:第11組</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>組員:41023229陳濬祺<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;41023238黃嘉偉<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;41023244廖崇軒<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;41023245劉于綸<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;41023246劉昱辰</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>日期：中華民國 114 年 1 月 6 日</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

st.title("一、概論 (問題描述與產業應用分析、文獻回顧、資料與專利蒐集與分析)")
st.markdown("""
## 主題一、創新夾持裝置機械設計
### 1. 各式（家）真空產生器的特點
#### 1.1 機械式真空幫浦（Piston Type Vacuum Pump）
**原理**：透過活塞的往復運動來產生真空。
- 適用於中等範圍的真空抽取。
- 效率較高，工作穩定。
- 容易維護。
- 工作時噪音較大。
#### 1.2 膜片式真空幫浦（Diaphragm Vacuum Pump）
**原理**：透過膜片的彎曲和回彈動作產生真空。
- 無油運轉，避免油污染。
- 體積較小，適合桌上型設備。
- 噪音較低。
- 可抽取較乾淨的氣體，但抽氣量相對較低。
#### 1.3 旋片式真空幫浦（Rotary Vane Vacuum Pump）
**原理**：透過旋轉的葉片在泵體內壓縮氣體來實現真空。
- 性能穩定，適合高真空環境。
- 工作噪音低，效率高。
- 需要潤滑油進行運作。
#### 1.4 分子泵（Molecular Pump）
**原理**：利用分子運動原理，透過渦輪轉動或氣體碰撞吸引分子以排除氣體。
- 適合抽取極高真空。
- 沒有油污染問題，抽氣極為乾淨。
- 能耗較高，價格昂貴。
### 2. 各式（家）真空產生器的產品與功能介紹
#### 2.1 威卡（VACUUBRAND）
**產品系列**：VACUUBRAND 提供各種類型的真空泵，包括旋片泵、膜片泵、渦輪分子泵等。
- 高效率的真空產生，適用於實驗室和工業用途。
- 無油設計，減少污染。
- 靜音運行，適合敏感環境。
- 高精度控制，可精確調整真空程度。
#### 2.2 貝爾（Busch）
**產品系列**：Busch 提供多種類型的真空泵，如旋片泵、液環泵、分子泵等。
- 高性能真空泵，適合高真空需求。
- 特別適用於需要持久穩定的應用。
- 具有高度可靠性和低維護成本。
- 強大的抽氣能力，滿足大型工業需求。
#### 2.3 西門子（Siemens）
**產品系列**：西門子提供多種真空泵，如螺桿泵、迴轉泵、液環泵等。
- 高效節能，減少能耗。
- 提供多樣的真空控制選項，方便精確操作。
- 強大的耐用性，適用於極端環境。
#### 2.4 阿爾法（Alcatel）
**產品系列**：提供從低到高真空的多種真空產生器，包括旋片幫浦、分子幫浦、油封幫浦等。
- 精確的真空控制，適合微米等級的操作。
- 快速啟動與操作，方便應用場景中的即時使用。
- 無污染操作，適用於潔淨環境。
## 主題二、環境量測與控制裝置機械設計
### 1.各式（家）散熱器元件或模組的特點
#### 1.1 空氣散熱器（Air Coolers）
原理: 利用風扇通過散熱片，將熱量傳導至空氣中，降低元件溫度。
- 成本低，安裝簡單。
- 需要較大空間安裝。
- 散熱效能受環境溫度影響較大。
- 適用於低至中等功率的設備。
#### 1.2 液冷散熱器（Liquid Coolers）
原理: 使用液體（通常是水或專用冷卻液）將熱量帶走，然後通過散熱器將熱量散發至空氣。
- 散熱效能高，能在較小體積內處理更多的熱量。
- 較為安靜。
- 涉及液體管路和泵系統，安裝較為複雜。
- 成本較高。
#### 1.3 熱管散熱器（Heat Pipe Coolers）
原理: 通過熱管內部的液體蒸發和冷凝過程，將熱量快速傳遞至散熱片。
- 高效能，能快速傳遞熱量。
- 具有較小的體積和重量。
- 不依賴機械運動部件，運行安靜。
- 需要較高的散熱片密度。
#### 1.4 散熱片（Heat Sinks）
原理: 將熱量從熱源傳遞到散熱片的表面，並通過與空氣的接觸進行散熱。
- 結構簡單，成本低。
- 無需外部動力，只依賴自然對流。
- 效能受周圍環境影響較大。
- 不適用於高功率設備。
### 2.各式（家）散熱器元件或模組的產品與功能介紹
#### 2.1 Noctua
產品系列: 各種高效能的空氣散熱器和風扇。
- 高效能散熱，優異的空氣流通設計。
- 適合高性能處理器及顯示卡的散熱。
- 低噪音設計，運行安靜。
- 長效耐用的高品質風扇。
應用領域: 高效能電腦、伺服器、工作站等
#### 2.2 Corsair
產品系列: Corsair 提供液冷散熱器和風扇模組。
- 提供強大的散熱效能，適合超頻處理器和顯示卡。
- 支援即插即用的安裝設計，便於使用者安裝。
- 配備 RGB 燈效和高效能冷卻液。
- 無需額外的維護，簡化操作。
應用領域: 高效能電腦、大型遊戲機、伺服器等
#### 2.3 Thermaltake
產品系列: 提供液冷模組、散熱片和風扇產品。
- 支援高效能冷卻技術，保持設備長時間穩定運行。
- 優化的散熱片設計，提升散熱效果。
- 支援RGB燈效及智能風扇控制。
- 易於安裝，適合DIY 電腦。
應用領域: DIY 電腦、伺服器、工業設備等
#### 2.4 DeepCool
產品系列: 提供各類液冷和熱管散熱器。
- 提供穩定的散熱效果，適合中高端設備。
- 靜音設計，運行安靜。
- 簡單的安裝過程，方便使用。
- 高效的冷卻技術，支持長時間負載運行。
應用領域: 個人電腦、伺服器、工業設備等
""")

st.markdown("<hr>", unsafe_allow_html=True)
st.title("二、原理與設計方法 (機械設計與繪圖)")
st.markdown("""
## 主題一、創新夾持裝置機械設計
### 1. 真空產生器設計與要求規範
#### 1.1 抽氣能力
- **真空度範圍**：根據應用需求設計真空度範圍。常見的真空度範圍為粗真空（10^-3至10^-1 Torr）、中等真空（10^-5至10^-3 Torr）、高真空（低於10^-7 Torr）。
- **抽氣速率**：真空泵的抽氣速率（通常以L/min或m³/h表示）需要根據系統的需求來確定，確保在一定時間內能夠達到目標真空度。
#### 1.2 效率與能耗
- **能源效率**：要求設計的真空產生器具有較高的能源利用效率，降低運行成本。
- **低能耗設計**：在設計中應選擇低能耗的馬達或泵浦來降低運行過程中的能量損失。
#### 1.3 噪音控制
- **低噪音運行**：真空泵在運行過程中可能會產生較高的噪音。設計時應考慮低噪音要求，採用隔音材料、特殊設計的風扇葉片和低噪音的動力系統。
#### 1.4 運行穩定性
- **長期運行穩定**：設計應確保真空產生器能夠長時間穩定運行，不容易出現故障或過熱。
- **耐用性**：泵浦的結構設計需要有足夠的強度來承受長時間運行帶來的機械應力。
#### 1.5 油污染與維護
- **無油運行**：設計時應盡量選擇無油泵浦，以避免油污染。油封和無油泵系統對於環境的清潔要求較高，尤其是對醫療和半導體行業。
- **簡單維護**：應考慮到設備的日常維護，設計應便於檢修、更換零件和清潔。
#### 1.6 尺寸與重量
- **結構小巧**：根據使用環境，設計的真空產生器應該盡量小型化，便於安裝。
- **便於移動**：尤其是在需要多點使用的場合，便於搬動和安裝的設計會更具吸引力。
#### 1.7 可靠性與安全性
- **耐高溫運行**：真空產生器需要在高溫或高壓環境下穩定工作，因此選材和密封設計非常重要。
- **故障保護機制**：設計應包含過熱保護、過壓保護等機制，避免在異常情況下損壞設備。
#### 1.8 成本控制
- **製造成本**：在確保性能和可靠性的基礎上，設計需要平衡成本，特別是對於大規模應用的設備。
### 2. 真空產生器設計方法
#### 2.1 理論與實驗分析
- **計算和模擬**：利用數學模型和計算流體動力學（CFD）模擬真空泵的運行，分析流體流動、熱傳遞、以及壓力變化等關鍵參數。這樣能夠幫助預測真空泵在實際應用中的性能，優化設計。
- **試驗測試**：在理論分析的基礎上進行物理試驗，驗證模擬結果。這有助於確保真空泵設計符合實際使用條件。
#### 2.2 真空泵選型
- **泵浦類型選擇**：根據應用需求，選擇合適的泵浦類型（如旋片泵、膜片泵、分子泵等），每種類型的泵浦都有其特定的應用場景和性能特點。
- **多階段真空系統設計**：對於需要極高真空度的應用，可能需要多階段泵系統來達成目標真空度，例如先用粗真空泵再接分子泵來達成高真空。
#### 2.3 機械結構設計
- **密封設計**：良好的密封系統對於保持真空是非常關鍵的，需根據工作環境選擇適當的密封材料。
- **材料選擇**：真空泵的材料需要具有良好的耐腐蝕性、耐高溫性和機械強度，常用材料有鋁合金、不鏽鋼等。
#### 2.4 系統集成設計
- **自動化控制**：設計應該包含精確的真空度控制系統，能根據需要自動調節真空程度。
- **監控系統**：設計應包括壓力傳感器、溫度傳感器等監控裝置，能夠及時反映真空產生器的運行狀態。
#### 2.5 減少能源消耗與提高效率
- **高效能設計**：選擇高效的馬達和泵體設計，減少能量損失。可以使用變頻驅動（VFD）來根據負荷情況調節泵速，從而降低能耗。
- **熱回收系統**：設計中可以加入熱回收系統，將真空泵運行中產生的熱能回收再利用，提高整體能源利用率。
#### 2.6 降低噪音與震動
- **隔音設計**：在真空泵的設計中應該考慮隔音材料的使用，並設計合理的機械結構來減少運行時的噪音。
- **振動減少**：合理的結構設計可以有效減少泵運行中的振動，進而降低噪音和延長設備壽命。
#### 2.7 測試與驗證
- **可靠性測試**：設計完成後，進行長時間運行測試以確認真空產生器在不同工作條件下的穩定性和可靠性。
- **性能測試**：進行抽氣速率、真空度、能效等性能測試，確保設備達到設計要求。
### 3.依據原理與工件大小之零組件設計圖
""")
image = Image.open('picture/62.jpg')
st.image(image)
st.markdown("""
## 主題二、環境量測與控制裝置機械設計
### 1. 散熱器設計與要求規範
#### 1.1 散熱效能
- **散熱範圍**：根據應用需求，設計應該能夠處理所需的熱量並將其有效散發至周圍環境。
- **熱傳遞效率**：散熱器應具備良好的熱傳遞性能，以實現快速散熱，並保持設備的穩定運行。
#### 1.2 安裝要求
- **尺寸與佈局**：根據設備的空間限制設計，確保散熱器能夠適配各種尺寸要求，並具有靈活的安裝方式。
- **結構穩定性**：散熱器的結構應具有足夠的強度，承受長期使用過程中的機械負荷。
#### 1.3 能效與能耗
- **低能耗設計**：選擇能效高的材料和設計方案，減少能源消耗，降低運行成本。
- **有效利用環境**：充分利用周圍環境條件（如風速、溫度等），提升散熱效能並減少能量損耗。
#### 1.4 噪音控制
- **低噪音運行**：在設計中應考慮散熱器運行時的噪音控制，特別是在需要安靜操作的環境下。
#### 1.5 效率與維護
- **長效運行**：散熱器應具有長期穩定運行的能力，耐高溫、耐腐蝕，並且能夠抵抗外部環境的影響。
- **簡單維護**：設計應考慮日常維護需求，散熱器的清潔、保養、修理應簡單便捷。
#### 1.6 可靠性與安全性
- **耐高溫運行**：散熱器應能夠在高溫環境下穩定運行，防止過熱對設備造成損壞。
- **故障預防**：設計中應包含熱過載保護、異常情況自動關閉等安全機制，避免設備因散熱不足而損壞。
#### 1.7 成本控制
- **製造成本**：在確保散熱效能和可靠性的基礎上，設計需要平衡成本，尤其是在大規模應用中，降低整體成本至關重要。
### 2. 散熱器設計方法
#### 2.1 熱設計分析
- **熱流分析**：根據設備的熱負荷，進行熱流分析，計算並選擇合適的散熱器尺寸和形狀。
- **熱傳遞模擬**：使用計算流體動力學（CFD）模擬熱傳遞過程，分析散熱器表面和周圍環境的熱交換效率。
#### 2.2 散熱器選型
- **散熱器類型選擇**：根據應用需求選擇合適的散熱器類型（如空氣散熱器、液冷散熱器、熱管散熱器等）。每種類型的散熱器有其特定的優勢和適用範圍。
- **多階段散熱系統**：對於高熱負荷的設備，可能需要多層次散熱系統，如在液冷系統中配合熱管或散熱片來加強散熱效能。
#### 2.3 材料選擇
- **高導熱材料**：選擇具有良好導熱性的材料，如鋁合金、銅等，來提高散熱效率。
- **耐腐蝕性材料**：在某些應用中，選擇耐腐蝕材料以確保散熱器的長期穩定性。
#### 2.4 結構設計
- **散熱片設計**：根據熱流情況，設計適當間隔和形狀的散熱片，以最大化表面積，提高散熱效果。
- **散熱片排列與配置**：設計合理的散熱片排列，使氣流能夠順暢地通過散熱片，增加對流散熱效率。
#### 2.5 散熱系統集成
- **風冷與液冷技術**：選擇風冷或液冷散熱系統，並根據散熱需求選擇合適的風扇、泵浦等輔助裝置來提高散熱效能。
- **自動化控制系統**：設計散熱系統中的溫度控制和風扇調速系統，根據工作狀況自動調節散熱器的運行。
#### 2.6 降低能耗與提高效率
- **高效能設計**：選擇高效能的散熱材料和設計，減少能量損失，提高整體運行效率。
- **能效監控系統**：設計中可以加入智能監控系統，實時檢測散熱器的工作狀態，優化能效表現。
#### 2.7 降低噪音與震動
- **風扇設計**：選擇低噪音風扇，並使用振動減少技術來降低散熱器運行過程中的噪音和震動。
- **聲學設計**：考慮聲學設計，選擇隔音材料或特殊結構來減少散熱器工作時產生的噪音。
#### 2.8 測試與驗證
- **性能測試**：對設計完成的散熱器進行性能測試，驗證其散熱效能、運行穩定性及能效。
- **壽命測試**：進行長期運行測試，確保散熱器在不同環境下能夠穩定運行，達到預期效果。
### 3.依據原理與工件大小之零組件設計圖
""")
col1, col2, col3, col4 = st.columns(4)
with col1:
    image = Image.open('picture/4.jpg')
    st.image(image, caption='散熱結構1')
with col2:
    image = Image.open('picture/5.jpg')
    st.image(image, caption='散熱結構2')
with col3:
    image = Image.open('picture/6.jpg')
    st.image(image, caption='散熱結構3')
with col4:
    image = Image.open('picture/7.jpg')
    st.image(image, caption='散熱結構4')


st.markdown("<hr>", unsafe_allow_html=True)
st.title("三、實驗量測與數據分析")
st.markdown("## 主題一、創新夾持裝置機械設計")
st.markdown("### 1.依照 Excel 檔進行設計參數計算")
st.markdown("### 2.詳細列出軟體分析之過程(CAD 模型、條件、材料常數、計算方法、其他)")
col1, col2, col3 = st.columns(3)
with col1:
    image = Image.open('picture/68.jpg')
    st.image(image)
with col2:
    image = Image.open('picture/69.jpg')
    st.image(image)
with col3:
    image = Image.open('picture/70.jpg')
    st.image(image)
st.write("#### Water 2D(Venturi_Example)")
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/71.jpg')
    st.image(image, caption='V=10 速度圖')
with col2:
    image = Image.open('picture/72.jpg')
    st.image(image, caption='V=10 壓力圖')
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/75.jpg')
    st.image(image, caption='V=15 速度圖')
with col2:
    image = Image.open('picture/76.jpg')
    st.image(image, caption='V=15 壓力圖')
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/73.jpg')
    st.image(image, caption='V=20 速度圖')
with col2:
    image = Image.open('picture/74.jpg')
    st.image(image, caption='V=20 壓力圖')
st.write("#### Air 2D_Asym(Venturi Exp)")
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/77.jpg')
    st.image(image, caption='V=6 速度圖')
with col2:
    image = Image.open('picture/78.jpg')
    st.image(image, caption='V=6 壓力圖')
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/79.jpg')
    st.image(image, caption='V=9.7 速度圖')
with col2:
    image = Image.open('picture/80.jpg')
    st.image(image, caption='V=9.7 壓力圖')
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/81.jpg')
    st.image(image, caption='V=13.33 速度圖')
with col2:
    image = Image.open('picture/82.jpg')
    st.image(image, caption='V=13.33 壓力圖')
st.write("#### Air 3D(Venturi Exp)")
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/84.jpg')
    st.image(image, caption='V=6 速度圖')
with col2:
    image = Image.open('picture/83.jpg')
    st.image(image, caption='V=6 壓力圖')
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/86.jpg')
    st.image(image, caption='V=9.7 速度圖')
with col2:
    image = Image.open('picture/85.jpg')
    st.image(image, caption='V=9.7 壓力圖')
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/88.jpg')
    st.image(image, caption='V=13.33 速度圖')
with col2:
    image = Image.open('picture/87.jpg')
    st.image(image, caption='V=13.33 壓力圖')
st.write("#### Air 3D(Generator)")
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/89.jpg')
    st.image(image, caption='V=1 速度圖')
with col2:
    image = Image.open('picture/90.jpg')
    st.image(image, caption='V=1 壓力圖')
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/91.jpg')
    st.image(image, caption='V=5 速度圖')
with col2:
    image = Image.open('picture/92.jpg')
    st.image(image, caption='V=5 壓力圖')
col1, col2 = st.columns(2)
with col1:
    image = Image.open('picture/93.jpg')
    st.image(image, caption='V=10 速度圖')
with col2:
    image = Image.open('picture/94.jpg')
    st.image(image, caption='V=10 壓力圖')
image = Image.open('picture/95.jpg')
st.image(image)
st.markdown("## 主題二、環境量測與控制裝置機械設計")
st.markdown("### 1.依照 Excel 檔進行設計參數計算")
st.markdown("""
### 2.詳細列出軟體分析之過程(CAD 模型、條件、材料常數、計算方法、其他)")
材料:
- A16061/A17075
- ADC12
- Cu
- Base = 52x52x9.5mm
- Height = 40mm
""")
image = Image.open('picture/66.jpg')
st.image(image)
image = Image.open('picture/67.jpg')
st.image(image)
st.markdown("""
## 主題三、bladeless wind turbine 結構設計(僅 Fluent 模擬)
### 1.詳細列出軟體分析之過程(CAD 模型、條件、材料常數、計算方法、其他)
幾何條件:
- D =0.01 m
- V = 1 m/s
- air,rho = 1.184 kg/m^3 (25℃, 一大氣壓)
- air,mu = kg/(m*s) (25℃, 一大氣壓)
流場條件:
- Re = 640
""")
image = Image.open('picture/63.jpg')
st.image(image, caption='V=0.1')
image = Image.open('picture/64.jpg')
st.image(image, caption='V=1')
image = Image.open('picture/65.jpg')
st.image(image, caption='分析結果')

st.markdown("<hr>", unsafe_allow_html=True)
st.title("四、結果與討論")
st.markdown("## 主題一、創新夾持裝置機械設計")
st.markdown("### 1.依照 Excel 檔建立真空產生器與周邊 3D 設計圖(零件、組合、爆炸)")
image = Image.open('picture/60.jpg')
st.image(image)
st.markdown("### 2.依照 Excel 檔建立真空產生器計算書(公式法)")
st.markdown("### 3.繪圖並討論數值模擬結果及計算書結果與數值模擬(CAE 法)之誤差?")
image = Image.open('picture/13.jpg')
st.image(image)
st.markdown("""
#### (1)進口壓力誤差
- **實驗數據：** 空壓機進口壓力為 6 kPa。  
- **Fluent 模擬結果：** 進口壓力為 4.76 kPa。  
- **誤差計算：**  
 誤差 (%) = │實驗值 - 模擬值│ ÷ 實驗值 × 100% = │6 - 4.76│ ÷ 6 × 100% = 26%  
#### (2)吸口壓力誤差
- **實驗數據：**  
  - 固體吸取測試的吸口壓力為 -57.8 kPa。  
  - 帶體吸取為 -59.1 kPa。  
  - 不規則吸取為 -59.9 kPa。  
  - 大荷重吸取為 -62.3 kPa。  
- **Fluent 模擬結果：** 喉部壓力（吸口壓力）為 -20.372 kPa。  
- **誤差計算（以固體吸取測試為例）：**  
誤差 (%) = │實驗值 - 模擬值│ ÷ 實驗值 × 100% = │(-57.8) - (-20.372)│ ÷ 6 × 100% = 188%  
### 4.繪圖並討論實驗測試結果及可能誤差大小與原因?)
#### (1)進口壓力測試結果
可能誤差原因：
- 模擬邊界條件設定可能不夠精確，尤其是進口邊界的紊流強度未正確考慮。
- 模擬中可能未充分考慮流場壓縮性效應或設備的微小泄露現象。
#### (2)吸口壓力測試結果
可能誤差原因：
- 模擬模型對喉部的流場特性可能估算不足，未能正確捕捉紊流效應或吸口壓力波動特性。
- 喉部幾何結構在模擬中可能簡化過度，導致與實際設備不符。
- 實驗測量中可能存在微小的壓力波動，影響數據穩定性。
""")
st.markdown("## 主題二、環境量測與控制裝置機械設計")
st.markdown("### 1.依照 Excel 檔建立散熱器與周邊 3D 設計圖(零件、組合、爆炸)")
image = Image.open('picture/61.jpg')
st.image(image)
st.markdown("### 2.依照 Excel 檔建立散熱器器計算書(公式法)")
st.markdown("### 3.繪圖並討論數值模擬結果及計算書結果與數值模擬(CAE 法)之誤差?")
image = Image.open('picture/14.jpg')
st.image(image)
st.markdown("""
#### (1)實際實驗數據：
- 輸出功率：4.914 W
- 室內溫度：22.5°C
- 室內相對濕度：57 RH%
- 散熱片頂部溫度：31.1°C
- 散熱片底部溫度：33.1°C
- 散熱面積：2958.34 mm²
#### (2)模擬結果:
- 散熱片頂部溫度：23.17°C
- 散熱片底部溫度：26.342°C
#### (3)誤差計算:
- 頂部溫度誤差:誤差 (%) = │實驗值 - 模擬值│ ÷ 實驗值 × 100% = │31.1 - 23.17│ ÷ 6 × 100% = 34.2%  
- 底部溫度誤差:誤差 (%) = │實驗值 - 模擬值│ ÷ 實驗值 × 100% = │33.1 - 26.342│ ÷ 6 × 100% = 25.6%  
""")
st.markdown("""
### 4.繪圖並討論實驗測試結果及可能誤差大小與原因?
可能的誤差原因:
- 模擬邊界條件設置
在數值模擬過程中，邊界條件的設定對結果的準確性至關重要。實際實驗可能無法完全模擬模擬中的理想條件。比如，散熱片的邊緣效應、環境溫度的波動等因素可能在模擬中被忽略或簡化。這可能導致模擬結果與實際測試之間的差異。
- 熱對流與熱傳導的影響
實際環境中，空氣流動（自然對流或強制對流）對熱傳遞的影響往往難以在模擬中精確捕捉。即使模擬中考慮了對流效應，也可能無法完全覆蓋實際實驗中遇到的變數，例如空氣流動模式和濕度影響等。
- 測量誤差
在實際測量中，使用的溫度計和傳感器可能會存在校準誤差或讀取誤差。此外，散熱片的不同部分在測量過程中可能會受到不同的環境影響，如接觸不良、環境輻射等，也可能會對測量結果產生影響。
- 模擬模型簡化
在使用CFD (計算流體力學) 模擬時，常常需要進行許多簡化處理，例如對流係數的估算、網格設置、物理模型的選擇等。如果這些簡化過程不夠精確，則模擬結果可能會與實際測量存在偏差。
- 物理模型的假設
數值模擬中可能對某些物理現象進行了假設和近似處理，例如忽略了散熱過程中的湍流效應或流場的非均勻性。這些假設可能對結果產生顯著影響，尤其是在高精度要求的情況下。
""")

st.markdown("<hr>", unsafe_allow_html=True)
st.title("結論")
st.markdown("""
## 主題一、創新夾持裝置機械設計
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;模擬結果與實際操作中的進口壓力誤差為 26%，而溪口壓力的誤差達到 188%。這表明模擬模型在壓力分布的預測上存在顯著偏差，尤其是在溪口壓力的計算上與實際情況不符。未來需針對模擬參數設定與模型邊界條件進行深入校正，以縮小模擬與實驗結果之間的差距，提升模型的準確性。
## 主題二、環境量測與控制裝置機械設計
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;模擬與實際操作中的頂部溫度誤差為 34.2%，底部溫度誤差為 25.6%。這說明裝置在模擬熱傳導過程與實際操作的溫度分布方面仍有不一致之處，特別是在熱流動與邊界影響的考量上存在偏差。未來應改進模擬熱模型的細節設定，並加強對環境邊界條件的控制，以提高模擬結果的準確性與可信度。
""")


st.markdown("<hr>", unsafe_allow_html=True)

image = Image.open('picture/1.jpg')
st.image(image, caption='期末上機測驗評分表', width=600)
st.markdown("<hr>", unsafe_allow_html=True)
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

data = {
    "學號": ["41023229", "41023238", "41023244", "41023245", "41023246"],
    "姓名": ["陳濬祺", "黃嘉偉", "廖崇軒", "劉于綸", "劉昱辰"],
    "分工內容": ["協助實驗", "操作實驗", "分析資料", "網站製作", "製作報告"],
    "貢獻度": ["20%", "20%", "20%", "20%", "20%"]
}

df = pd.DataFrame(data)
df.index += 1  # 索引從1開始

st.table(df)
st.markdown("<p style='text-align: center;'>完成日期：114 年 1 月 6 日</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>聲明</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>本人在此聲明，本設計作業皆由本人與同組成員共同獨立完成，並無其他第三者參與作業之進行，若有抄襲或其他違反正常教學之行為，自願接受該次成績以零分計。</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>同時本人亦同意在上述表格中所記載之作業貢獻度，並以此計算本次個人作業成績。</p>", unsafe_allow_html=True)
col1, col2, col5, col3, col4 = st.columns(5)
with col1:
    image = Image.open('picture/8.jpg')
    st.image(image)
with col2:
    image = Image.open('picture/9.jpg')
    st.image(image)
with col3:
    image = Image.open('picture/10.jpg')
    st.image(image)
with col4:
    image = Image.open('picture/11.jpg')
    st.image(image)
with col5:
    image = Image.open('picture/12.jpg')
    st.image(image)