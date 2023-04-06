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

if "beslutsgräns" not in st.session_state:
    st.session_state["beslutsgräns"] = 50

############################## Program and UI #################################

st.header("D-dimer")

if "Ddimer_result" not in st.session_state:
    st.session_state["Ddimer_result"] = 0.5

st.number_input("Ange resultat från D-dimer"
    , step=0.01
    , key="Ddimer_result"
    #, on_change=ddimer_update_slider
    )

if 0.5 < st.session_state["Ddimer_result"] < 1.0:

    if "Ddimer_age" not in st.session_state:
        st.session_state["Ddimer_age"] = 50

    def update_pesi_from_ddimer():
        st.session_state["pesi_age"] = st.session_state["Ddimer_age"]
        
    st.number_input("Ange ålder"
        , step=1
        , key="Ddimer_age"
        , on_change=update_pesi_from_ddimer
        )


    if st.session_state["Ddimer_age"]:
        st.session_state["beslutsgräns"] =\
            max([0.50, st.session_state["Ddimer_age"]*0.01])
        st.session_state["beslutsgräns"] =\
            round(st.session_state["beslutsgräns"],2)
        st.write(f"Åldersbaserad beslutsgräns: {st.session_state['beslutsgräns']}")

# om man har fyllt i resulatunder 0.5 --> presentera slutsats
if st.session_state["Ddimer_result"] < 0.5:
    st.success(f"Negativt D-dimer test. Lungemboli kan uteslutas.\
         Överväg annan diagnos.")
    f.klar()

elif st.session_state["Ddimer_result"] > 1.0:
    st.error(f"Positivt D-dimer test. Det går ej att utesluta lungemboli. Fortsätt utredning med DTLA.")

    col1, col2 = st.columns([1, 1])
    f.col_control_rem()
    with col1:
        knapp_positiv_ddimer = st.button("Fyll i röntgensvar")
        f.ddimer_display_lottie()
        if knapp_positiv_ddimer:
            switch_page("Röntgen")


# om man har fyllt i både ålder och resulat --> presentera slutsats
if "Ddimer_age" in st.session_state:
    if st.session_state["Ddimer_result"] > st.session_state["beslutsgräns"]:
        st.error(f"Positivt D-dimer test. Det går ej att utesluta lungemboli. Fortsätt utredning med DTLA.")

        col1, col2 = st.columns([1, 1])
        f.col_control_rem()
        with col1:
            knapp_positiv_ddimer = st.button("Fyll i röntgensvar")
            f.ddimer_display_lottie()
            if knapp_positiv_ddimer:
                switch_page("Röntgen")
    else:
        st.success(f"Negativt D-dimer test. Lungemboli kan uteslutas.\
         Överväg annan diagnos.")
        f.klar()