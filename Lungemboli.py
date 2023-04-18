import streamlit as st
from functions import f
from st_pages import Page, show_pages, hide_pages
st.session_state.update(st.session_state)

############################# language choice #################################
with st.sidebar:
    st.radio(label="Language"
             , options=["Svenska", "English"]
             , key="lang"
             , label_visibility="collapsed"
             , horizontal=True)

show_pages(
[
    Page("Lungemboli.py", "Wells'"),
    Page("pages/01_PERC.py", "PERC"),
    Page("pages/02_D-dimer.py", "D-dimer"),
    Page("pages/03_Röntgen.py", "Röntgen"),
    Page("pages/03_xray.py", "X-ray"),

]
)
if st.session_state["lang"] == "Svenska":
    hide_pages(["X-ray"])
    dct_lungemboli = {
        "Kliniska tecken på DVT": 3,
        "Tidigare LE/DVT diagnos": 1.5,
        "Hjärtfrekvens >100/min": 1.5,
        "Hemoptys": 1,
        "Immobiliserad i >3 dagar / Opererad senaste 4 v.": 1.5,
        "LE mer sannolik än annan diagnos": 3,
        "Malignitet behandlad inom 6 mån alt. palliation": 1
        }
    wells_header = "Wells' Lungemboli"
    viz_header = "Riskvisualisering"
else:
    hide_pages(["Röntgen"])
    dct_lungemboli = {
        "Clinical signs of DVT": 3,
        "Previous PE/DVT diagnosis": 1.5,
        "Heart rate >100/min": 1.5,
        "Hemoptysis": 1,
        "Immobility for >3 days / Surgery in last 4 weeks": 1.5,
        "PE more likely than alternative diagnosis": 3,
        "Malignancy treated within 6 months or palliation": 1
        }

    wells_header = "Wells' PE"
    viz_header = "Visualization of Risk"


#################################### css  #####################################

f.button_style()
f.hide_anchor_link()
f.hide_footer()
f.hide_hamburger()
f.hide_padding_top()
f.hide_img_fullscreen()
f.reduce_padding()


########################### Initialize Variables ##############################
if "wells_påbörjad" not in st.session_state:
    st.session_state["wells_påbörjad"] = True

############################# Local Variables #################################

name_lungemboli = "lungemboli"

######################### Session State Variables #############################

f.initialize_widget_keys(dct_lungemboli, name_lungemboli)

if "total_score_pe" not in st.session_state:
    st.session_state["total_score_pe"] = 0

####################### Initialize Variables THE END ##########################
############################## Program and UI #################################



# generate checkboxes
# first five are synced with PERC questionnaire
st.header(wells_header)
for i, j in enumerate(dct_lungemboli.items()):
    if i < 5:
        st.checkbox(
            j[0],\
            key=f"{name_lungemboli}_{i}",\
            #help=f"Poäng: {j[1]}",\
            on_change=f.sync_lungemboli_to_perc, 
            args=(i,))
    else:
        st.checkbox(
            j[0],\
            key=f"{name_lungemboli}_{i}",\
            #help=f"Poäng: {j[1]}"
            )

# calculate score and display vizualization, text & "change-page-button"
st.session_state["total_score_pe"] = f.calc_score(dct_lungemboli, name_lungemboli)

with st.expander(viz_header, expanded=True):
    f.lungemboli_display_viz_v1(st.session_state["total_score_pe"])


st.markdown("""
    <style>
    .css-ocqkz7 [data-testid=stVerticalBlock]{
        gap: 0.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    if st.session_state["lang"] == "English":
        f.lungemboli_display_button(st.session_state["total_score_pe"], True)
    else:
        f.lungemboli_display_button(st.session_state["total_score_pe"], False)
    f.lungemboli_display_lottie(st.session_state["total_score_pe"])

f.lungemboli_display_txt(st.session_state["total_score_pe"])


############################ Flow Illustration  ###############################
with st.sidebar:
    f.display_flow_v2()