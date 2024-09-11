import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import time
from sklearn.linear_model import LinearRegression

# データ生成（仮データ）
def generate_mock_data():
    dates = pd.date_range(start="2023-01-01", periods=10)
    progress_data = np.random.randint(50, 100, size=(10,))
    submission_rates = np.random.randint(80, 100, size=(10,))
    study_hours = np.random.randint(1, 4, size=(10,))
    return pd.DataFrame({"Date": dates, "Progress": progress_data, "Submission Rate": submission_rates, "Study Hours": study_hours})

data = generate_mock_data()

# ヘッダー
st.title("学習管理アプリ")
st.header("進捗状況と成績の管理")

# グラフ描画
st.subheader("学習進捗のグラフ")
fig, ax = plt.subplots()
ax.plot(data["Date"], data["Progress"], label="進捗状況 (%)")
ax.set_xlabel("日付")
ax.set_ylabel("進捗 (%)")
ax.legend()
st.pyplot(fig)

# 課題提出率の表示
st.subheader("課題提出率")
st.bar_chart(data.set_index("Date")["Submission Rate"])

# 学習時間記録
st.subheader("学習時間の記録")
st.line_chart(data.set_index("Date")["Study Hours"])

# ランダム通知（簡易版）
st.subheader("ランダム通知")
if st.button("ランダムに問題を出す"):
    random_notification = random.choice(["問題を解いてみましょう！", "次の課題に挑戦！", "小テストの時間です！"])
    st.write(random_notification)

# 成績のAI分析（簡易版）
st.subheader("AIによる成績分析")
X = np.array(data.index).reshape(-1, 1)  # 仮データ
y = data["Progress"]

# 線形回帰モデルの訓練
model = LinearRegression()
model.fit(X, y)

predicted_progress = model.predict(np.array([[len(data)]]))  # 次の日の進捗予測

st.write(f"AIの予測によると、明日の進捗は {predicted_progress[0]:.2f}% です。")
