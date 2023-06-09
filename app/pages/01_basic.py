import streamlit as st
from datetime import date

## text
st.title("title") # タイトル
st.header("header") # ヘッダー
st.write("write") # 表示(内部的に自動変換)

text_markdown="""
# markdonw title
- a
- b
- c
"""
st.markdown(text_markdown) # マークダウンで表示
st.text("text") # テキスト表示

## 温度
st.metric(label="Temperature", value="70 °F", delta="1.2 °F") # 指標

## interact
st.button("button") # ボタン
st.selectbox("selectbox", ("select1", "select2")) # セレクトボックス
st.multiselect("multiselectbox", ("select1", "select2")) # 複数選択可能なセレクトボックス
st.radio("radiobutton", ("radio1", "radio2")) # ラジオボタン
is_check = st.checkbox("check button") # チェックボタン
if is_check:
    st.text("checked")
st.text_input("text input") # 文字入力(1行)
st.text_area("text area") # 文字入力(複数行)
st.slider("slider", 0, 100, 50) # スライダー
st.file_uploader("Choose file") # ファイルアップロード
# 日時
date = st.date_input('Input date', value=date(2000, 1, 1))
time = st.time_input('Input time')
st.write(date, time)