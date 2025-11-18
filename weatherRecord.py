import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 快速測試
d = {}
for i in range(1, 13):
    # 獲取資料夾中的所有檔案
    folder_path = "2024-" + str(i).zfill(2) + "/"
    all_files = os.listdir(folder_path)

    # 過濾出 XML 檔案
    xml_files = [f for f in all_files if f.endswith(".xml")]

    # 逐一處理每個 XML 檔案

    for file_name in xml_files:
        file_path = os.path.join(folder_path, file_name)
        tree = ET.parse(file_path)
        root = tree.getroot()
        description = root.find(".//item/description")
        if description is not None and description.text:
            soup = BeautifulSoup(description.text, "html.parser")
            table = soup.find("table")
            tr0 = table.find_all("tr")[0]
            tempereture = tr0.find_all("td")[1].text[0:2]
            d[file_name] = tempereture
d = dict(sorted(d.items()))
df = pd.DataFrame(list(d.items()), columns=["File Name", "Temperature"])
# 解析檔案名中的時間資訊


def parse_filename(filename):
    # 移除副檔名，例如將 "2024010101.xml" 轉為 "2024010101"
    name_without_ext = filename.replace("-CurrentWeather_uc.xml", "")

    # 提取各個時間成分（假設格式為：年月日時 - 2024010101）
    year = name_without_ext[0:4]  # 2024
    month = name_without_ext[4:6]  # 01
    day = name_without_ext[6:8]  # 01
    hour = name_without_ext[9:11]  # 01

    return year, month, day, hour


# 應用解析函數
df[["Year", "Month", "Day", "Hour"]] = df["File Name"].apply(
    lambda x: pd.Series(parse_filename(x))
)

# 將溫度轉為數值類型
df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")

# 創建完整的日期時間列
df["DateTime"] = pd.to_datetime(df[["Year", "Month", "Day", "Hour"]].astype(int))

# 查看處理後的數據
# 檢查缺失值
print("缺失值統計:")
print(df.isnull().sum())

# 檢查溫度值的基本統計資訊
print("\n溫度統計摘要:")
print(df["Temperature"].describe())

# 移除無效的溫度值（根據香港實際氣候）
df_clean = df[(df["Temperature"] >= 0) & (df["Temperature"] <= 40)].copy()

# 匯出清理後的數據
df_clean.to_csv("hong_kong_temperature_2024.csv", index=False)

# 匯出主要統計結果
summary_stats = {
    "總數據點": len(df_clean),
    "平均溫度": df_clean["Temperature"].mean(),
    "最高溫度": df_clean["Temperature"].max(),
    "最低溫度": df_clean["Temperature"].min(),
    "數據時間範圍": f"{df_clean['DateTime'].min()} 到 {df_clean['DateTime'].max()}",
}

print("分析摘要:")
for key, value in summary_stats.items():
    print(f"{key}: {value}")
# 設定中文字體（如果需要顯示中文）
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]  # 或者使用其他支持中文的字體

# 計算每日平均溫度
# daily_avg = (
#     df_clean.groupby(["Year", "Month", "Day"])
#     .agg({"Temperature": "mean", "DateTime": "first"})
#     .reset_index()
# )

# daily_avg["Date"] = pd.to_datetime(daily_avg[["Year", "Month", "Day"]])

# plt.figure(figsize=(12, 6))
# plt.plot(
#     daily_avg["Date"], daily_avg["Temperature"], marker="o", linewidth=1, markersize=2
# )
# plt.title("2024年香港每日平均溫度變化")
# plt.xlabel("日期")
# plt.ylabel("溫度 (°C)")
# plt.grid(True, alpha=0.3)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# 分析一天中不同時段的溫度模式
# hourly_pattern = (
#     df_clean.groupby("Hour")["Temperature"].agg(["mean", "std"]).reset_index()
# )

# plt.figure(figsize=(10, 6))
# plt.plot(
#     hourly_pattern["Hour"],
#     hourly_pattern["mean"],
#     marker="o",
#     linewidth=2,
#     label="平均溫度",
# )
# plt.fill_between(
#     hourly_pattern["Hour"],
#     hourly_pattern["mean"] - hourly_pattern["std"],
#     hourly_pattern["mean"] + hourly_pattern["std"],
#     alpha=0.2,
#     label="溫度波動範圍",
# )
# plt.title("一天中不同時段的溫度變化模式")
# plt.xlabel("小時")
# plt.ylabel("溫度 (°C)")
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.show()

# 月度統計
# monthly_stats = (
#     df_clean.groupby("Month")
#     .agg({"Temperature": ["mean", "max", "min", "std"]})
#     .round(1)
# )

# monthly_stats.columns = ["月平均", "月最高", "月最低", "月波動"]
# print("月度溫度統計:")
# print(monthly_stats)

# # 繪製月度溫度箱形圖
# plt.figure(figsize=(12, 6))
# df_clean["Month"] = df_clean["Month"].astype(int)
# sns.boxplot(data=df_clean, x="Month", y="Temperature")
# plt.title("2024年各月份溫度分布")
# plt.xlabel("月份")
# plt.ylabel("溫度 (°C)")
# plt.show()
