import streamlit as st

# 回数処理
if 'count' not in st.session_state:
    st.session_state["count"] = 0

## interact
if st.button("count++"): # ボタン
    st.session_state["count"] += 1
st.write(st.session_state["count"])
