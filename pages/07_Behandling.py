import streamlit as st

st.session_state.update(st.session_state)

with st.expander("Behandling 1"):
    st.header("Rukrik")
    st.subheader("Underrubrik")
    st.write("Brödtext...")
    mer_info_1 = st.checkbox("Visa mer info")
    if mer_info_1: 
        st.header("Rukrik")
        st.subheader("Underrubrik")
        st.write("Brödtext...")

with st.expander("Behandling 2"):
    st.header("Rukrik")
    st.subheader("Underrubrik")
    st.write("Brödtext...")
    mer_info_2 = st.checkbox("Visa mer info")
    if mer_info_2: 
        st.header("Rukrik")
        st.subheader("Underrubrik")
        st.write("Brödtext...")

with st.expander("Behandling 3"):
    st.header("Rukrik")
    st.subheader("Underrubrik")
    st.write("Brödtext...")
    mer_info_3 = st.checkbox("Visa mer info")
    if mer_info_3: 
        st.header("Rukrik")
        st.subheader("Underrubrik")
        st.write("Brödtext...")

