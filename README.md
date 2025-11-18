# WeatherReport
香港氣象數據分析 - 使用 Python 爬取並分析香港天文台 XML 數據。包含數據清理、趨勢分析和可視化，展示 Pandas 與 Matplotlib 的實戰應用。


# 香港天氣數據分析 2024

## 專案概述
本專案從香港天文台爬取 2024 年每小時天氣數據，進行完整的數據清理、轉換與分析，探索溫度變化模式與季節趨勢。

📈 主要發現<img width="1194" height="591" alt="Screenshot 2025-11-18 at 3 17 48 PM" src="https://github.com/user-attachments/assets/3b8c8331-9614-4efd-93af-21bdc066acbd" />
<img width="990" height="587" alt="Screenshot 2025-11-18 at 3 26 48 PM" src="https://github.com/user-attachments/assets/b51311a3-313c-4772-a81c-a2638dcbbab2" />
<img width="1171" height="568" alt="Screenshot 2025-11-18 at 3 27 16 PM" src="https://github.com/user-attachments/assets/36b95cae-c0c6-45e2-9909-2ad91feb29a4" />

2024 年最高溫：35°C 出現在 8月
最低溫度：6°C 出現在1月
全年平均氣溫24.79°C 

每日溫度峰值通常出現在下午 X 點
## 🛠 技術棧
- **語言**: Python 3
- **主要套件**: Pandas, Matplotlib, BeautifulSoup, xml.etree
- **數據源**: 香港天文台開放數據

## 📊 專案亮點
- 從原始 XML 檔案解析並提取天氣數據
- 處理時間序列數據與異常值清理
- 生成多種可視化圖表：
  - 每日溫度趨勢圖
  - 每小時溫度模式分析
  - 月度溫度分布箱形圖


## 🚀 快速開始
```bash
# 克隆專案
git clone https://github.com/yourusername/hk-weather-analysis.git

# 安裝依賴
pip install pandas matplotlib beautifulsoup4

# 運行分析
python weather_analysis.py 
