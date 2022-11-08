import streamlit as st

st.header("Inläggning")

st.write("Om...")

knapp_ultraljud = st.button("Gå vidare till ultraljud")
if knapp_ultraljud:
    switch_page("Ultraljud")