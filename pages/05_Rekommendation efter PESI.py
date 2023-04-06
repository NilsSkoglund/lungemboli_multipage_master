import streamlit as st

def display_recommendations(x):
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

    st.subheader("Vård")

    col1, col2 = st.columns([1,3])

    # Adjust column widths based on custom CSS
    st.markdown(
        f"<style>.css-ocqkz7.e1tzin5v4 > div:nth-child(1) {{ flex: 1 !important; }} .css-ocqkz7.e1tzin5v4 > div:nth-child(2) {{ flex: 2 !important; }}</style>",
        unsafe_allow_html=True,
    )

    if x == 1:
        vårdnivå1_index = 0
        behandling_index = 1
        telemetri_index = 1
        news_index = 0
        koag_index = 0
        vårdcentral_index = 0
    elif x == 2:
        vårdnivå1_index = 1
        behandling_index = 0
        telemetri_index = 1
        news_index = 0
        koag_index = 0
        vårdcentral_index = 1
    elif x == 3:
        vårdnivå1_index = 1
        behandling_index = 0
        telemetri_index = 0
        news_index = 1
        koag_index = 0
        vårdcentral_index = 1
    with col1:
        st.write("Vårdnivå 1:")
        st.write("Vårdnivå 2:")
        st.write("Telemetri:")
        st.write("News:")
        st.write("Behandling:")

    with col2:
        st.radio("Vårdnivå 1:", options=["Hem", "Inläggning"], index=vårdnivå1_index, horizontal=True, label_visibility="collapsed", key=f"radio1_{x}")
        if st.session_state[f"radio1_{x}"] == "Hem":
            is_hem = True
        else:
            is_hem = False
        st.radio("Vårdnivå 2:", options=["Avdelning", "MIMA", "IVA"], index=0, horizontal=True, label_visibility="collapsed", disabled=is_hem, key=f"radio2_{x}")
        st.radio("Telemetri:", options=["Ja", "Nej"], index=telemetri_index, horizontal=True, label_visibility="collapsed", disabled=is_hem, key=f"radio3_{x}")
        st.radio("News:", options=["x4", "x6", "x8"], index=news_index, horizontal=True, label_visibility="collapsed", disabled=is_hem, key=f"radio4_{x}")
        st.radio("Behandling:", options=["Fragmin", "Eliquis"], index=behandling_index, horizontal=True, label_visibility="collapsed", key=f"radio5_{x}")
    
    st.subheader("Remiss")

    col11, col22 = st.columns([1,3])

    with col11:
        st.write("Hjärteko")
        st.write("Koag. mottagn.")
        st.write("Vårdcentral")

    with col22:
        st.radio("Hjärteko:", options=["Ja", "Nej"], index=1, horizontal=True, label_visibility="collapsed", key=f"radio6_{x}")
        st.radio("Koagulationsmottagning:", options=["Ja", "Nej"], index=koag_index, horizontal=True, label_visibility="collapsed", key=f"radio7_{x}")
        st.radio("Vårdcentral:", options=["Ja", "Nej"], index=vårdcentral_index, horizontal=True, label_visibility="collapsed", key=f"radio8_{x}")


st.header("Rekommendation efter PESI")

st.session_state["most_severe_dtla"] = "lungemboli"
if "dtla_1" in st.session_state:
    for i in range(1,6):
        x = st.session_state[f"dtla_{i}"]
        if x == True:
            if i == 1:
                st.session_state["most_severe_dtla"] = "perifer lungemboli"
            elif i == 2:
                st.session_state["most_severe_dtla"] = "lungemobli på subsegmentell nivå"
            elif i == 3:
                st.session_state["most_severe_dtla"] = "lungemboli på segmentell nivå"
            elif i == 4:
                st.session_state["most_severe_dtla"] = "lungemobli på lobär nivå"
            elif i == 5:
                st.session_state["most_severe_dtla"] = "sadelemboli"

if "pesi_score" not in st.session_state:
    st.session_state["pesi_score"] = 70

st.write("Pesi score:", st.session_state["pesi_score"])

def expand_recommendation(lower_limit, upper_limit):
    return lower_limit < st.session_state["pesi_score"] < upper_limit

with st.expander("Riskgrupp 1", expanded=expand_recommendation(0, 66)):
    info_msg = f"Patient med bekräftad {st.session_state['most_severe_dtla']}.\
    Riskstratifieras enligt PESI i riskgrupp 1 där den genomsnittliga 30\
    dagars mortaliteten är mellan 0.0-1.6%"
    st.info(info_msg)
    display_recommendations(1)

with st.expander("Riskgrupp 2", expanded=expand_recommendation(65, 86)):
    info_msg = f"Patient med bekräftad {st.session_state['most_severe_dtla']}.\
        Riskstratifieras enligt PESI i riskgrupp 2 där den genomsnittliga 30\
        dagars mortaliteten är mellan 1.7-3.5%"
    st.info(info_msg)
    display_recommendations(2)
    

with st.expander("Riskgrupp 3", expanded=expand_recommendation(85, 106)):
    info_msg = f"Patient med bekräftad {st.session_state['most_severe_dtla']}.\
        Riskstratifieras enligt PESI i riskgrupp 3 där den genomsnittliga 30\
        dagars mortaliteten är mellan 3.2-7.1%"
    st.info(info_msg)
    display_recommendations(3)
    


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