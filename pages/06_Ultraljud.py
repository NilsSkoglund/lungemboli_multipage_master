import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.session_state.update(st.session_state)

st.header("Ultraljud")
st.write("...")

knapp_behandling = st.button("Gå vidare till behandling")
if knapp_behandling:
    switch_page("Behandling")