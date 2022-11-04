import streamlit as st

st.session_state.update(st.session_state)

st.header("Röntgen")

options = st.multiselect(
    'Röntgensvar',
    ['Alternativ 1', 'Alternativ 2', 'Alternativ 3'])

st.write('You selected:', options)

st.info("visa bilder här istället!")