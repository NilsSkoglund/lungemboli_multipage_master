import streamlit as st

st.session_state.update(st.session_state)

with st.expander("Behandling 1"):
    st.header("Rukrik")
    st.subheader("Underrubrik")
    st.write("Brödtext...")

with st.expander("Behandling 2"):
    st.write("...")

with st.expander("Behandling 3"):
    st.write("...")

