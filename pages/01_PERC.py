import streamlit as st
from functions import f
from streamlit_extras.switch_page_button import switch_page

st.session_state.update(st.session_state)
########################### Initialize Variables ##############################

############################# Local Variables #################################

dct_perc = {
    "Kliniska tecken på DVT": 1,
    "Tidigare LE/DVT diagnos": 1,
    "Hjärtfrekvens >100/min": 1,
    "Hemoptys": 1,
    "Immobiliserad i >3 dagar / Opererad senaste 4 veckor": 1.5,
    "LE mer sannolik än annan diagnos": 3,
    "Malignitet behandlad inom 6 mån eller palliation": 1
    }
name_perc = "perc"

############################## Program and UI #################################

st.header("PERC")
st.info("5 av 8 frågor i PERC ingår i Wells' PE formuläret.\
 När dessa frågor besvaras i Wells' PE formuläret \
    ges de samma svar i PERC-formuläret.")

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
    st.warning("Inget av kriterierna får vara uppfyllt")
    knapp_perc_bruten = st.button("Gå till Ddimer")
    if knapp_perc_bruten:
        switch_page("Ddimer")
else:
    st.success("PERC-regeln ej bruten, lungemboli kan uteslutas")
