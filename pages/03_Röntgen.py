import streamlit as st

st.subheader("Röntgen")

options = st.multiselect(
    'Röntgensvar',
    ['Alternativ 1', 'Alternativ 2', 'Alternativ 3'])

st.write('You selected:', options)