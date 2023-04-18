import streamlit as st
from st_pages import hide_pages

if "pesi_score" not in st.session_state:
    st.session_state["pesi_score"] = 0

with st.sidebar:
    st.radio(label="Language"
             , options=["Svenska", "English"]
             , key="lang"
             , label_visibility="collapsed"
             , horizontal=True)

if "lang" not in st.session_state:
    st.session_state["lang"] = "Svenska"

if st.session_state["lang"] == "Svenska":
    hide_pages(["X-ray"])
    vård1 = "Vårdnivå 1:"
    vård1_options = ["Hem", "Inläggning"]
    vård2 = "Vårdnivå 2:"
    vård2_options = ["Avdelning", "MIMA", "IVA"]
    tel = "Telemetri:"
    tel_options = ["Ja", "Nej"]
    news = "News:"
    behandling = "Behandling:"

    eko = "Hjärteko"
    eko_options = ["Ja", "Nej"]
    vc = "Vårdcentral"
    vc_options = ["Ja", "Nej"]
    koag = "Koag. mottagn."
    koag_options = ["Ja", "Nej"]


    subh_vård = "Vård"
    subh_remiss = "Remiss"

    header = "Guide efter PESI"

else:
    hide_pages(["Röntgen"])
    vård1 = "Care level 1:"
    vård1_options = ["Home", "Admission"]
    vård2_options = ["Ward", "MIMA", "ICU"]
    vård2 = "Care level 2:"
    tel = "Telemetry:"
    tel_options = ["Yes", "No"]
    news = "News:"
    behandling = "Treatment:"

    eko = "ECG"
    eko_options = ["Yes", "No"]
    vc = "Care center"
    vc_options = ["Yes", "No"]
    koag = "Coag. clinic"
    koag_options = ["Yes", "No"]

    subh_vård = "Care"
    subh_remiss = "Referral"
    header = "Guide after PESI"

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

    st.subheader(subh_vård)

    col1, col2 = st.columns([1,3])

    # Adjust column widths based on custom CSS
    st.markdown(
        f"<style>.css-ocqkz7.e1tzin5v4 > div:nth-child(1) {{ flex: 1 !important; }} .css-ocqkz7.e1tzin5v4 > div:nth-child(2) {{ flex: 2.5 !important; }}</style>",
        unsafe_allow_html=True,
    )

    if x == 1:
        vårdnivå1_index = 0
        vårdnivå2_index = 0
        behandling_index = 1
        telemetri_index = 1
        news_index = 0
        koag_index = 0
        vårdcentral_index = 0
    elif x == 2:
        vårdnivå1_index = 1
        vårdnivå2_index = 0
        behandling_index = 0
        telemetri_index = 1
        news_index = 0
        koag_index = 0
        vårdcentral_index = 1
    elif x == 3:
        vårdnivå1_index = 1
        vårdnivå2_index = 0
        behandling_index = 0
        telemetri_index = 0
        news_index = 1
        koag_index = 0
        vårdcentral_index = 1
    elif x == 4:
        vårdnivå1_index = 1
        vårdnivå2_index = 1
        behandling_index = 0
        telemetri_index = 0
        news_index = 2
        koag_index = 0
        vårdcentral_index = 1
    elif x == 5:
        vårdnivå1_index = 1
        vårdnivå2_index = 2
        behandling_index = 0
        telemetri_index = 0
        news_index = 2
        koag_index = 0
        vårdcentral_index = 1
    with col1:
        st.write(vård1)
        st.write(vård2)
        st.write(tel)
        st.write(news)
        st.write(behandling)

    with col2:
        st.radio("Vårdnivå 1:", options=vård1_options, index=vårdnivå1_index, horizontal=True, label_visibility="collapsed", key=f"radio1_{x}")
        if st.session_state[f"radio1_{x}"] in ["Hem", "Home"]:
            is_hem = True
        else:
            is_hem = False
        st.radio("Vårdnivå 2:", options=vård2_options, index=vårdnivå2_index, horizontal=True, label_visibility="collapsed", disabled=is_hem, key=f"radio2_{x}")
        st.radio("Telemetri:", options=tel_options, index=telemetri_index, horizontal=True, label_visibility="collapsed", disabled=is_hem, key=f"radio3_{x}")
        st.radio("News:", options=["x4", "x6", "x8"], index=news_index, horizontal=True, label_visibility="collapsed", disabled=is_hem, key=f"radio4_{x}")
        st.radio("Behandling:", options=["Fragmin", "Eliquis"], index=behandling_index, horizontal=True, label_visibility="collapsed", key=f"radio5_{x}")
    
    st.subheader(subh_remiss)

    col11, col22 = st.columns([1,3])

    with col11:
        st.write(eko)
        st.write(vc)
        st.write(koag)

    with col22:
        st.radio("Hjärteko:", options=eko_options, index=1, horizontal=True, label_visibility="collapsed", key=f"radio6_{x}")
        st.radio("Vårdcentral:", options=vc_options, index=vårdcentral_index, horizontal=True, label_visibility="collapsed", key=f"radio8_{x}")
        st.radio("Koagulationsmottagning:", options=koag_options, index=koag_index, horizontal=True, label_visibility="collapsed", key=f"radio7_{x}")


st.header(header)

if st.session_state["lang"] == "Svenska":
    st.session_state["most_severe_dtla"] = "lungemboli"
else:
    st.session_state["most_severe_dtla"] = "Pulmonary Embolism"

if "dtla_1" in st.session_state:
    for i in range(1,6):
        x = st.session_state[f"dtla_{i}"]
        if x == True:
            if st.session_state["lang"] == "Svenska":
                if i == 1:
                    st.session_state["most_severe_dtla"] = "perifer lungemboli"
                elif i == 2:
                    st.session_state["most_severe_dtla"] =\
                          "lungemobli på subsegmentell nivå"
                elif i == 3:
                    st.session_state["most_severe_dtla"] =\
                          "lungemboli på segmentell nivå"
                elif i == 4:
                    st.session_state["most_severe_dtla"] =\
                          "lungemobli på lobär nivå"
                elif i == 5:
                    st.session_state["most_severe_dtla"] = "sadelemboli"
            else:
                if i == 1:
                    st.session_state["most_severe_dtla"] =\
                         "Peripheral pulmonary embolism"
                elif i == 2:
                    st.session_state["most_severe_dtla"] =\
                          "Subsegmental pulmonary embolism"
                elif i == 3:
                    st.session_state["most_severe_dtla"] =\
                          "Segmental pulmonary embolism"
                elif i == 4:
                    st.session_state["most_severe_dtla"] =\
                          "Lobar pulmonary embolism"
                elif i == 5:
                    st.session_state["most_severe_dtla"] = "Saddle embolism"

def expand_recommendation(lower_limit, upper_limit):
    return lower_limit < st.session_state["pesi_score"] < upper_limit

with st.expander("PESI Risk 1", expanded=expand_recommendation(0, 66)):
    if st.session_state["lang"] == "Svenska":
        info_msg = f"Patient med bekräftad {st.session_state['most_severe_dtla']}.\
        Riskstratifieras enligt PESI i riskgrupp 1 där den genomsnittliga 30\
        dagars mortaliteten är mellan 0.0-1.6%"
    else:
        info_msg = f"Patient with confirmed\
        {st.session_state['most_severe_dtla']} \
        Risk stratified according to PESI in risk group 1\
        , where the average 30-day mortality rate is between 0.0-1.6%"
    st.info(info_msg)
    display_recommendations(1)

with st.expander("PESI Risk 2", expanded=expand_recommendation(65, 86)):
    if st.session_state["lang"] == "Svenska":
        info_msg = f"Patient med bekräftad {st.session_state['most_severe_dtla']}.\
        Riskstratifieras enligt PESI i riskgrupp 2 där den genomsnittliga 30\
        dagars mortaliteten är mellan 1.7-3.5%"
    else:
        info_msg = f"Patient with confirmed {st.session_state['most_severe_dtla']}.\
        Risk stratified according to PESI in risk group 2, where the average 30-day\
        mortality rate is between 1.7-3.5%"
    st.info(info_msg)
    display_recommendations(2)
    

with st.expander("PESI Risk 3", expanded=expand_recommendation(85, 106)):
    if st.session_state["lang"] == "Svenska":
        info_msg = f"Patient med bekräftad {st.session_state['most_severe_dtla']}.\
        Riskstratifieras enligt PESI i riskgrupp 3 där den genomsnittliga 30\
        dagars mortaliteten är mellan 3.2-7.1%"
    else:
        info_msg = f"Patient with confirmed {st.session_state['most_severe_dtla']}.\
        Risk stratified according to PESI in risk group 3, where the average 30-day\
        mortality rate is between 3.2-7.1%"
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



with st.expander("PESI Risk 4", expanded=expand_recommendation(105, 126)):
    if st.session_state["lang"] == "Svenska":
        info_msg = f"Patient med bekräftad {st.session_state['most_severe_dtla']}.\
        Riskstratifieras enligt PESI i riskgrupp 4 där den genomsnittliga 30\
        dagars mortaliteten är mellan 4.0-11.4%"
    else:
        info_msg = f"Patient with confirmed {st.session_state['most_severe_dtla']}.\
        Risk stratified according to PESI in risk group 4, where the average 30-day\
        mortality rate is between 4.0-11.4%"
    st.info(info_msg)
    display_recommendations(4)

with st.expander("PESI Risk 5", expanded=expand_recommendation(125, 300)):
    if st.session_state["lang"] == "Svenska":
        info_msg = f"Patient med bekräftad {st.session_state['most_severe_dtla']}.\
        Riskstratifieras enligt PESI i riskgrupp 5 där den genomsnittliga 30\
        dagars mortaliteten är mellan 10.0-25.5%"
    else:
        info_msg = f"Patient with confirmed {st.session_state['most_severe_dtla']}.\
        Risk stratified according to PESI in risk group 5, where the average 30-day\
        mortality rate is between 10.0-25.5%"
    st.info(info_msg)
    display_recommendations(5)