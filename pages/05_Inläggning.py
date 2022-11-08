import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.header("Inläggning")

st.write("Om...")

knapp_ultraljud = st.button("Gå vidare till ultraljud")
if knapp_ultraljud:
    switch_page("Ultraljud")