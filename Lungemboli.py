import streamlit as st
from functions import f

st.session_state.update(st.session_state)

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 2rem;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
########################### Initialize Variables ##############################

############################# Local Variables #################################

dct_lungemboli = {
    "Kliniska tecken på DVT": 3,
    "Tidigare LE/DVT diagnos": 1.5,
    "Hjärtfrekvens >100/min": 1.5,
    "Hemoptys": 1,
    "Immobiliserad i >3 dagar / Opererad senaste 4 veckor": 1.5,
    "LE mer sannolik än annan diagnos": 3,
    "Malignitet behandlad inom 6 mån alt. palliation": 1
    }
name_lungemboli = "lungemboli"

######################### Session State Variables #############################

f.initialize_widget_keys(dct_lungemboli, name_lungemboli)

if "total_score_pe" not in st.session_state:
    st.session_state["total_score_pe"] = 0

####################### Initialize Variables THE END ##########################
############################## Program and UI #################################



# generate checkboxes
# first five are synced with PERC questionnaire
tooltip_style = """
<style>
div[data-baseweb="tooltip"] {
  width: 100px;
}
</style>
"""
st.markdown(tooltip_style,unsafe_allow_html=True)
st.header("Formulär: Wells'")
for i, j in enumerate(dct_lungemboli.items()):
    if i < 5:
        st.checkbox(
            j[0],\
            key=f"{name_lungemboli}_{i}",\
            help=f"Poäng: {j[1]}",\
            on_change=f.sync_lungemboli_to_perc, 
            args=(i,))
    else:
        st.checkbox(
            j[0],\
            key=f"{name_lungemboli}_{i}",\
            help=f"Poäng: {j[1]}")

# calculate score and display vizualization, text & "change-page-button"
st.session_state["total_score_pe"] = f.calc_score(dct_lungemboli, name_lungemboli)
f.lungemboli_display_viz(st.session_state["total_score_pe"])
f.lungemboli_display_txt(st.session_state["total_score_pe"])




