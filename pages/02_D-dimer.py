import streamlit as st
from functions import f
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages

f.button_style()
f.hide_anchor_link()
f.hide_footer()
f.hide_hamburger()
f.hide_padding_top()

st.session_state.update(st.session_state)

############################# language choice #################################
if "lang" not in st.session_state:
    st.session_state["lang"] == "Svenska"

if st.session_state["lang"] == "Svenska":
    hide_pages(["X-ray"])
    result_header = "Ange resultat från D-dimer"
    neg_txt = f"Negativt D-dimer test. Lungemboli kan uteslutas.\
         Överväg annan diagnos."
    pos_txt = f"Positivt D-dimer test. Det går ej att utesluta lungemboli.\
          Fortsätt utredning med DTLA."
else:
    hide_pages(["Röntgen"])
    result_header = "Enter D-dimer result"
    neg_txt = f"Negative D-dimer test. Pulmonary embolism can be ruled out.\
         Consider an alternative diagnosis."
    pos_txt = f"Positive D-dimer test. Pulmonary embolism cannot be ruled out.\
          Continue the investigation with CTPA."



########################### Initialize Variables ##############################

st.session_state["D-dimer_påbörjad"] = True

if "beslutsgräns" not in st.session_state:
    st.session_state["beslutsgräns"] = 50

############################## Program and UI #################################

st.header("D-dimer")

# if "Ddimer_result" not in st.session_state:
#     st.session_state["Ddimer_result"] = 0.5

st.number_input(result_header
    , step=0.01
    , key="Ddimer_result"
    #, on_change=ddimer_update_slider
    )


# om man har fyllt i resulatunder 0.5 --> presentera slutsats
if 0 < st.session_state["Ddimer_result"] <= 0.5:
    st.session_state["Ddimer_status"] = "negative"
    st.success(neg_txt)
    f.klar()

elif st.session_state["Ddimer_result"] >= 1.0:
    st.session_state["Ddimer_status"] = "positive"
    st.error(pos_txt)

    col1, col2 = st.columns([1, 1])
    f.col_control_rem()
    with col1:
        knapp_positiv_ddimer = st.button("Fyll i röntgensvar")
        f.ddimer_display_lottie()
        if knapp_positiv_ddimer:
            switch_page("Röntgen")

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

# om man har fyllt i både ålder och resulat --> presentera slutsats
if "Ddimer_age" in st.session_state and 0.5 < st.session_state["Ddimer_result"] < 1.0:
    if st.session_state["Ddimer_result"] > st.session_state["beslutsgräns"]:
        st.session_state["Ddimer_status"] = "positive"
        st.error(pos_txt)

        col1, col2 = st.columns([1, 1])
        f.col_control_rem()
        with col1:
            if st.session_state["lang"] == "English":
                knapp_positiv_ddimer = st.button("Fill in the X-ray result")
                f.ddimer_display_lottie_eng()
            else:
                knapp_positiv_ddimer = st.button("Fyll i röntgensvar")
                f.ddimer_display_lottie()
            if knapp_positiv_ddimer:
                switch_page("Röntgen")
    else:
        st.session_state["Ddimer_status"] = "negative"
        st.success(neg_txt)
        # KLAR knapp
        if st.session_state["lang"] == "English":
            f.klar_eng()
        else:
            f.klar()
############################ Flow Illustration  ###############################
with st.sidebar:
    f.display_flow_v2()