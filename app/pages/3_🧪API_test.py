import streamlit as st
import requests
import numpy as np

st.set_page_config(page_title="Find Your Gif", page_icon='🔎')
st.title('🎁 Request a Gif')
query = st.text_input('Enter search query')
url = 'https://api.giphy.com/v1/gifs/search'
params = {"api_key": st.secrets['api_key'],
          "q": query,
          "limit":10}

if query:
    response = requests.get(url=url, params=params).json()
    result = response['data'][np.random.randint(5)]['embed_url']

    # URL
    st.write(f'🔗 Requested URL ➡️ {result}')

    # Render gif
    st.title('Your Gif')
    st.write(f'<iframe src="{result}" width="480" height="240">',
            unsafe_allow_html=True)
