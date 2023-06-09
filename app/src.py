import os
from pydantic import BaseModel

import streamlit as st
import pandas as pd
import numpy as np



css = """
  <style>
  #MainMenu {visibility: hidden;}
  </style>
  """
st.markdown(css, unsafe_allow_html=True)

st.write("Hello, World!")
