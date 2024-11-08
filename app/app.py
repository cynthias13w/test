import streamlit as st

import numpy as np
import pandas as pd

"hello"
st.markdown("""# This is a header
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines to display in df
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)
head_df

st.button("Click me", key='click_me_button')
st.checkbox("I agree")
st.toggle("Enable")

# Caching. E.g., np.random.randn
def generate_data():
    return np.random.randn(3, 3)


@st.cache_data  # 👈 Add the caching decorator
def generate_data_cached():
    return np.random.randn(3, 3)

st.write("No caching")
st.write(generate_data())
st.write("Caching")
st.write(generate_data_cached())
