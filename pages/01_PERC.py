import streamlit as st
from functions import f
from streamlit_extras.switch_page_button import switch_page

st.session_state.update(st.session_state)

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 2rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
########################### Initialize Variables ##############################

############################# Local Variables #################################

dct_perc = {
    "Kliniska tecken på DVT": 1,
    "Tidigare LE/DVT diagnos": 1,
    "Hjärtfrekvens >100/min": 1,
    "Hemoptys": 1,
    "Immobiliserad i >3 dagar / Opererad senaste 4 veckor": 1,
    "Ålder ≥50": 1,
    "Saturation >94% utan syrgas": 1,
    "Östrogenbehandling": 1
    }
name_perc = "perc"

############################## Program and UI #################################

st.header("Formulär: PERC")
with st.expander("Klicka för info"):
    st.info("5 av 8 frågor i PERC ingår i Wells' kriterier för Lungemboli.\
    När dessa frågor besvaras i formuläret för Wells' kriterier\
    ges de samma svar i PERC-formuläret nedan")

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
    st.error("Inget av kriterierna får vara uppfyllt")
    knapp_perc_bruten = st.button("Gå till Ddimer")
    if knapp_perc_bruten:
        switch_page("Ddimer")
else:
    st.success("PERC-regeln ej bruten, Lungemboli kan uteslutas")
