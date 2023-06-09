import streamlit as st

# テーブルに関する処理
def process_text(text):
    return f'a {text} b'

text = st.text_input("text input") # テキスト表示

## interact
if st.button("テキストを処理"): # ボタン
    text2 = process_text(text)
    st.write(text2)
