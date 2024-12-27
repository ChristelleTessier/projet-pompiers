import streamlit as st
import pandas as pd
import numpy as np

def page4():
    st.write("test p4")
    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        chart_data