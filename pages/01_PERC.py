import streamlit as st
from functions import f
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages


st.session_state.update(st.session_state)

f.button_style()
f.hide_anchor_link()
f.hide_footer()
f.hide_hamburger()
f.hide_padding_top()
############################# language choice #################################
if "lang" not in st.session_state:
    st.session_state["lang"] == "Svenska"

if st.session_state["lang"] == "Svenska":
    hide_pages(["X-ray"])
    dct_perc = {
    "Kliniska tecken på DVT": 1,
    "Tidigare LE/DVT diagnos": 1,
    "Hjärtfrekvens >100/min": 1,
    "Hemoptys": 1,
    "Immobiliserad i >3 dagar / Opererad senaste 4 v.": 1,
    "Ålder ≥50": 1,
    "Saturation >94% utan syrgas": 1,
    "Östrogenbehandling": 1
    }
    info_header = "Klicka för info"
    info_txt = "5 av 8 frågor i PERC ingår i Wells' kriterier för Lungemboli.\
    När dessa frågor besvaras i formuläret för Wells' kriterier\
    ges de samma svar i PERC-formuläret nedan"
    perc_pos = "PERC-positiv. Lungemboli kan ej uteslutas.\
          Ta D-dimer för fortsatt utredning."
    perc_neg = "PERC-negativ. Lungemboli kan uteslutas. Överväg annan diagnos."

else:
    hide_pages(["Röntgen"])
    dct_perc = {
    "Clinical signs of DVT": 1,
    "Previous PE/DVT diagnosis": 1,
    "Heart rate >100/min": 1,
    "Hemoptysis": 1,
    "Immobility for >3 days / Surgery in last 4 weeks": 1,
    "Age ≥50": 1,
    "Saturation >94% without oxygen": 1,
    "Estrogen therapy": 1
    }
    info_header = "Show more info"
    info_txt = "5 out of 8 questions in PERC are included\
    in Wells' criteria for Pulmonary Embolism.\
    When these questions are answered in the Wells' criteria form,\
    they receive the same response in the PERC form below."
    perc_pos = "PERC-positive. Pulmonary embolism cannot be ruled out.\
          Perform a D-dimer test for further investigation."
    perc_neg = "PERC-negative. Pulmonary embolism can be ruled out.\
          Consider an alternative diagnosis."


########################### Initialize Variables ##############################

st.session_state["perc_påbörjad"] = True

############################# Local Variables #################################
name_perc = "perc"

############################## Program and UI #################################

st.header("PERC")
with st.expander(info_header):
    st.info(info_txt)

for i, j in enumerate(dct_perc.items()):
    if i < 5:
        st.checkbox(
            j[0],\
            key=f"{name_perc}_{i}")
    else:
        st.checkbox(
            j[0],\
            key=f"{name_perc}_{i}")

if f.calc_score(dct_perc, name_perc) > 0:
    st.error(perc_pos)

    st.markdown("""
    <style>
    .css-ocqkz7 [data-testid=stVerticalBlock]{
        gap: 0.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        knapp_perc_bruten = st.button("Ange D-dimer svar")
        f.perc_display_lottie()
        if knapp_perc_bruten:
            switch_page("D-dimer")
else:
    st.success(perc_neg)
    f.klar()
    # KLAR knapp


############################ Flow Illustration  ###############################
with st.sidebar:
    f.display_flow_v2()