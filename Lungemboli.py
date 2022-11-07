import streamlit as st
from functions import f

st.session_state.update(st.session_state)

f.hide_anchor_link()
f.hide_footer()
f.hide_hamburger()
f.hide_padding()

########################### Initialize Variables ##############################

############################# Local Variables #################################

dct_lungemboli = {
    "Kliniska tecken på DVT": 3,
    "Tidigare LE/DVT diagnos": 1.5,
    "Hjärtfrekvens >100/min": 1.5,
    "Hemoptys": 1,
    "Immobiliserad i >3 dagar / Opererad senaste 4 v.": 1.5,
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
# st.markdown(tooltip_style,unsafe_allow_html=True)

st.header("Formulär: Wells' Lungemboli")
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

#with st.empty():
hide_img_fullscreen = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
st.markdown(hide_img_fullscreen, unsafe_allow_html=True)

button_style_red = """
        <style>
        .stButton > button {
            color: #ffffff;
            background: #eb4034;
            border: 1px solid #ffffff;
        }
        </style>
        """

button_style = """
        <style>
        .stButton > button {
            border: 1px solid #ffffff;
        }
        </style>
        """
#st.markdown(button_style, unsafe_allow_html=True)

f.lungemboli_display_viz_v1(st.session_state["total_score_pe"])

st.markdown("""
    <style>
    div:nth-child(16) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)

f.lungemboli_display_txt(st.session_state["total_score_pe"])




