import streamlit as st
import pandas as pd
import numpy as np

## table
dataframe = pd.DataFrame(np.random.randn(5,20))

## show
st.dataframe(dataframe) # pandasのデータフレーム
st.table(dataframe) # 静的な表
