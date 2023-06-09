import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

## graph
dataframe = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
st.line_chart(dataframe) # 線グラフ
st.area_chart(dataframe) # チャート
st.bar_chart(dataframe) # 棒グラフ

# 描画領域を用意する
fig = plt.figure()
ax = fig.add_subplot()
# ランダムな値をヒストグラムとしてプロットする
x = np.random.normal(loc=.0, scale=1., size=(100,))
ax.hist(x, bins=20)
# Matplotlib の Figure を指定して可視化する
st.pyplot(fig)