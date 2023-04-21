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
    dct_radiology_report={
        "Ingen lungemboli": 0,
        "Perifer lungemboli": 1,
        "Lungemboli på subsegmentell nivå": 2,
        "Lungemboli på segmentell nivå": 3,
        "Lungemboli på lobär nivå": 4,
        "Sadelemboli": 5
        }
    header = "Röntgen"
    uteslutas = "Lungemboli kan uteslutas. Överväg annan diagnos."
    verifierad = "Patienten har en verifierad lungemboli.\
          Bedöm vårdnivå med hjälp av PESI."
    pesi_txt = "Riskstratifiera enligt PESI"
    konflikterande_info = "Konflikterande information."

else:
    hide_pages(["Röntgen"])
    dct_radiology_report = {
        "No pulmonary embolism": 0,
        "Peripheral pulmonary embolism": 1,
        "Subsegmental pulmonary embolism": 2,
        "Segmental pulmonary embolism": 3,
        "Lobar pulmonary embolism": 4,
        "Saddle embolism": 5
        }
    header = "X-ray"
    uteslutas = "Pulmonary embolism can be ruled out.\
          Consider an alternative diagnosis."
    verifierad = "The patient has a confirmed pulmonary embolism.\
          Assess the level of care using PESI."
    pesi_txt = "Risk stratify according to PESI"
    konflikterande_info = "Conflicting information."

# Initialize variables for radiology_report
	# dct with report_answer:score
	# name for key

name_rad = "dtla"

st.header(header)
    
for i, j in enumerate(dct_radiology_report.items()):
    st.checkbox(
        j[0]\
        , key=f"{name_rad}_{i}"
    )

#st.warning("visa bilder här baserat på svar")

if "verifierad_lungemboli" not in st.session_state:
    st.session_state["verifierad_lungemboli"] = False

for i in range(1,6):
    if st.session_state[f"dtla_{i}"]:
        st.session_state["verifierad_lungemboli"] = True
        break
    else:
        st.session_state["verifierad_lungemboli"] = False

if st.session_state["dtla_0"] and st.session_state["verifierad_lungemboli"]:
    st.session_state["verifierad_lungemboli"] = False
    st.warning(konflikterande_info)
elif st.session_state["dtla_0"]:
    st.session_state["verifierad_lungemboli"] = False
    st.success(uteslutas)
    if st.session_state["lang"] == "English":
        f.klar_eng()
    else:
        f.klar()
elif st.session_state["verifierad_lungemboli"]:
    st.error(verifierad)

    col1, col2 = st.columns([1, 1])
    f.col_control_rem()
    with col1:
        knapp_pesi = st.button(pesi_txt)
        if st.session_state["lang"] == "English":
            f.dtla_display_lottie_eng()
        else:
            f.dtla_display_lottie()
        if knapp_pesi:
            switch_page("PESI")

############################ Flow Illustration  ###############################
with st.sidebar:
    if st.session_state["lang"] == "English":
        f.display_flow_v2_eng()
    else:
        f.display_flow_v2()