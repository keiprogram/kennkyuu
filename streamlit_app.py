import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 仮データの生成
def generate_progress_data():
    # 10日間の仮データ
    dates = pd.date_range(start="2023-01-01", periods=10)
    progress = [55, 60, 65, 70, 75, 80, 82, 85, 88, 90]  # 進捗率 (%)
    scores = [70, 72, 75, 78, 80, 85, 87, 88, 90, 92]    # 成績 (%)
    return pd.DataFrame({"Date": dates, "Progress": progress, "Score": scores})

# データの読み込み
data = generate_progress_data()

# アプリのタイトル
st.title("学習進捗管理アプリ")
st.header("リアルタイムで学習進捗と成績を把握")

# 進捗状況のグラフ
st.subheader("学習進捗の視覚化")
fig, ax = plt.subplots()
ax.plot(data["Date"], data["Progress"], marker="o", label="進捗率 (%)")
ax.plot(data["Date"], data["Score"], marker="x", label="成績 (%)", linestyle="--")
ax.set_xlabel("日付")
ax.set_ylabel("進捗/成績 (%)")
ax.set_title("学習進捗と成績の推移")
ax.legend()

st.pyplot(fig)

# データの表示
st.subheader("データの確認")
st.write(data)

# 進捗と成績のリアルタイム入力
st.subheader("進捗状況を更新")
new_progress = st.slider("今日の進捗率 (%)", 0, 100, 50)
new_score = st.slider("今日の成績 (%)", 0, 100, 50)

if st.button("更新"):
    # 新しいデータを追加
    new_data = pd.DataFrame({
        "Date": [pd.to_datetime("today")],
        "Progress": [new_progress],
        "Score": [new_score]
    })
    data = pd.concat([data, new_data], ignore_index=True)
    
    st.success(f"進捗率: {new_progress}%, 成績: {new_score}% を追加しました")

# 更新後のグラフ再描画
st.subheader("更新後の学習進捗の視覚化")
fig2, ax2 = plt.subplots()
ax2.plot(data["Date"], data["Progress"], marker="o", label="進捗率 (%)")
ax2.plot(data["Date"], data["Score"], marker="x", label="成績 (%)", linestyle="--")
ax2.set_xlabel("日付")
ax2.set_ylabel("進捗/成績 (%)")
ax2.set_title("更新後の学習進捗と成績の推移")
ax2.legend()

st.pyplot(fig2)

# 更新後のデータ表示
st.subheader("更新後のデータ")
st.write(data)
