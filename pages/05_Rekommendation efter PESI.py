import streamlit as st

st.header("Rekommendation efter PESI")

st.write("Pesi score:", st.session_state["pesi_score"])

def expand_recommendation(lower_limit, upper_limit):

    return lower_limit < st.session_state["pesi_score"] < upper_limit

st.write("Hej")


with st.expander("Riskgrupp 1", expanded=expand_recommendation(0, 66)):
    st.write("...")

with st.expander("Riskgrupp 2", expanded=expand_recommendation(65, 86)):
    st.info("PESI riskgrupp 2 med 30 dagars mortalitet mellan 1.7-3.5%")
    # Define custom CSS
    custom_css = """
    <style>
    /* Custom CSS for Streamlit columns */

    .css-ocqkz7.e1tzin5v4 {
    display: flex !important;
    flex-wrap: nowrap !important;
    }

    .css-ocqkz7.e1tzin5v4 > div {
    flex: 1 !important;
    min-width: 0 !important;
    }
    </style>
    """

    # Add custom CSS to the application
    st.markdown(custom_css, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Vårdnivå 1:")
        st.write("Vårdnivå 2:")
    with col2:
        st.radio("Vårdnivå 1:", options=["Hem", "Inläggning"], index=1, horizontal=True, label_visibility="collapsed")
        st.radio("Vårdnivå 2:", options=["Avdelning", "MIMA", "IVA"], index=0, horizontal=True)
    
    st.radio("Telemetrik:", options=["JA", "NEJ"], index=0, horizontal=True)
    st.radio("News:", options=["x4", "x6", "x8"], index=1, horizontal=True)
    st.radio("Behandling:", options=["Fragmin", "Eliquis"], index=0, horizontal=True)
    st.multiselect("Remiss:", options=["Hjärteko", "Koagulationsmottagning", "Vårdcentral"])
    


with st.expander("Riskgrupp 3", expanded=expand_recommendation(85, 106)):
    st.subheader("Rekommendation för riskgrupp 3")

    st.info("**30 dagars mortalitet:** 3.2-7.1%")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**Vårdnivå 1:**")
        st.write("**Vårdnivå 2:**")
        st.write("**News:**")
    with col2: 
        st.button("Hem")
        st.button("Avdelning")
        st.button("x4")
    with col3:
        st.button("Inläggning")
        st.button("MIMA")
        st.button("x6")
    with col4:
        st.button("N/A", disabled=True)
        st.button("IVA")
        st.button("x8")
    


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