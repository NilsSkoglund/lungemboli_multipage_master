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
    st.subheader("Rekommendation för riskgrupp 3")

    st.info("**30 dagars mortalitet:** 3.2-7.1%")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**Vårdnivå 1:**")
        st.write("**Vårdnivå 2:**")
    with col2: 
        st.button("Hem")
        st.button("Avdelning")
    with col3:
        st.button("Inläggning")
        st.button("MIMA")
    with col4:
        st.write("")
        st.button("IVA")
    


#     st.write("**Allmän vårdnivå:** Patienten rekommenderas läggas in på en avdelning med telemetri")

#     st.markdown(
#     """
#     **Ytterligare rekommendationer:**
#     - News x4
#     - Beställ Troponin. Om positiv, kontakta kärlkirurg
#     """
# )



with st.expander("Riskgrupp 4", expanded=expand_recommendation(105, 126)):
    st.write("...")

with st.expander("Riskgrupp 5", expanded=expand_recommendation(125, 300)):
    st.write("...")