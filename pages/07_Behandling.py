import streamlit as st

st.session_state.update(st.session_state)

with st.expander("Fragmin(dalteparin)", expanded=True):
    st.header("Fragmin(dalteparin)")
    st.write("Dos: 200 E/kg/dygn")
    st.markdown(
"""
Absoluta kontraindikationer:
- Ti överkänslighet för Fragmin
"""
)
    st.empty()
    st.checkbox("Visa mer info", key = "mer_info_1")
    if st.session_state["mer_info_1"]: 
        st.markdown(
"""
Relativa ki:
- Pågående blödning
- Tidigare HIT typ II
- Svår koagulationsrubbning
"""
)

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

