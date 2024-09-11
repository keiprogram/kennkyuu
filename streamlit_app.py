import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# タイトルと説明
st.title('学習進捗管理アプリ')
st.write('学習の進捗状況や成績をリアルタイムで管理・視覚化するアプリです。')

# データを保存するための初期化（デモ用）
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=['Date', 'Study Hours', 'Score'])

# 学習データ入力フォーム
with st.form(key='study_form'):
    date = st.date_input('学習日', value=datetime.now())
    study_hours = st.number_input('学習時間（時間）', min_value=0.0, step=0.5)
    score = st.number_input('テストのスコア', min_value=0, max_value=100, step=1)
    
    submit_button = st.form_submit_button(label='データを保存')

# データの保存処理
if submit_button:
    new_data = pd.DataFrame({'Date': [date], 'Study Hours': [study_hours], 'Score': [score]})
    st.session_state['data'] = pd.concat([st.session_state['data'], new_data], ignore_index=True)
    st.success('データが保存されました！')

# 保存されたデータの表示
st.write('### 現在の学習データ')
st.dataframe(st.session_state['data'])

# グラフ描画のオプション
st.write('### グラフ表示')
plot_type = st.selectbox('表示するグラフを選択してください', ['学習時間', 'スコア'])

# グラフ描画
if not st.session_state['data'].empty:
    fig, ax = plt.subplots()

    if plot_type == '学習時間':
        ax.plot(st.session_state['data']['Date'], st.session_state['data']['Study Hours'], marker='o')
        ax.set_title('日別学習時間の推移')
        ax.set_xlabel('日付')
        ax.set_ylabel('学習時間（時間）')

    elif plot_type == 'スコア':
        ax.plot(st.session_state['data']['Date'], st.session_state['data']['Score'], marker='o', color='orange')
        ax.set_title('日別スコアの推移')
        ax.set_xlabel('日付')
        ax.set_ylabel('スコア')

    st.pyplot(fig)
else:
    st.write('データがまだ入力されていません。')
