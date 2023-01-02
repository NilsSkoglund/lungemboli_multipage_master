import streamlit as st

st.session_state.update(st.session_state)

with st.expander("Behandling 1"):
    st.header("Rukrik")
    st.subheader("Underrubrik")
    st.write("Brödtext...")
    st.checkbox("Visa mer info", key = "mer_info_1")
    if st.session_state["mer_info_1"]: 
        st.header("Rukrik")
        st.subheader("Underrubrik")
        st.write("Brödtext...")

with st.expander("Behandling 2"):
    st.header("Rukrik")
    st.subheader("Underrubrik")
    st.write("Brödtext...")
    st.checkbox("Visa mer info", key = "mer_info_2")
    if st.session_state["mer_info_2"]: 
        st.header("Rukrik")
        st.subheader("Underrubrik")
        st.write("Brödtext...")

with st.expander("Behandling 3"):
    st.header("Rukrik")
    st.subheader("Underrubrik")
    st.write("Brödtext...")
    st.checkbox("Visa mer info", key = "mer_info_3")
    if st.session_state["mer_info_3"]: 
        st.header("Rukrik")
        st.subheader("Underrubrik")
        st.write("Brödtext...")

