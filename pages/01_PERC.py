import streamlit as st
from functions import f
from streamlit_extras.switch_page_button import switch_page

st.session_state.update(st.session_state)

f.button_style()
f.hide_anchor_link()
f.hide_footer()
f.hide_hamburger()
f.hide_padding_top()

########################### Initialize Variables ##############################

############################# Local Variables #################################

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
    st.markdown("""
    <style>
    .css-ocqkz7 [data-testid=stVerticalBlock]{
        gap: 0.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        f.lungemboli_display_button(st.session_state["total_score_pe"])
        f.lungemboli_display_lottie(st.session_state["total_score_pe"])
        st.error("PERC-positiv. Lungemboli kan ej uteslutas.")
        knapp_perc_bruten = st.button("Gå vidare till D-dimer")
        f.perc_display_lottie()
        if knapp_perc_bruten:
            switch_page("D-dimer")
else:
    st.success("PERC-negativ. Lungemboli kan uteslutas. Överväg annan diagnos.")
    f.klar()
    # KLAR knapp
