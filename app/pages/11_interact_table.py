import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

## read csv
# CSVファイルを読み込む
def load_data():
    file_csv = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
    if file_csv is not None:
        df = pd.read_csv(file_csv).to_dict('records')
        return df

# テーブルに関する処理
def process_data(data):
    for data_i in data:
        data_i['datetime'] = datetime.now()
        data_i['result'] = False
    return data

data_list = load_data()
# st.write(data)
if data_list is not None:
    st.write("データフレームの内容:")
    st.table(data_list)
    if st.button("データを処理"):
        data_list_2 = data_list.copy()
        data_list_2 = process_data(data_list_2)
        
        st.write("処理されたデータフレームの内容:")
        st.table(data_list_2)