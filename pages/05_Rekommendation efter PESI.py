import streamlit as st

st.header("Rekommendation efter PESI")

st.write("Pesi score:", st.session_state["pesi_score"])

def expand_recommendation(lower_limit, upper_limit):

    return lower_limit < st.session_state["pesi_score"] < upper_limit

st.write("Hej")


with st.expander("Riskgrupp 1", expanded=expand_recommendation(0, 66)):
    st.write("...")

with st.expander("Riskgrupp 2", expanded=expand_recommendation(65, 86)):
    st.write("...")

with st.expander("Riskgrupp 3", expanded=expand_recommendation(85, 106)):
    st.write("...")

with st.expander("Riskgrupp 4", expanded=expand_recommendation(105, 126)):
    st.write("...")

with st.expander("Riskgrupp 5", expanded=expand_recommendation(125, 300)):
    st.write("...")