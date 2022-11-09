import streamlit as st
from functions import f
from streamlit_extras.switch_page_button import switch_page

st.session_state.update(st.session_state)

f.hide_anchor_link()
f.hide_footer()
f.hide_hamburger()
f.hide_padding()

########################### Initialize Variables ##############################

if "beslutsgräns" not in st.session_state:
    st.session_state["beslutsgräns"] = 50

############################## Program and UI #################################

st.header("D-dimer")

# def age_update_slider():
#     st.session_state.Ddimer_age_slider = st.session_state.Ddimer_age
# def age_update_numin():
#     st.session_state.Ddimer_age = st.session_state.Ddimer_age_slider  

# slider_value = st.slider('Ange ålder'
#                         , min_value=0
#                         , max_value=100
#                         , value=50
#                         , step=1
#                         , key="Ddimer_age"
#                         #, on_change=age_update_numin
#                         )




if "Ddimer_age" not in st.session_state:
    st.session_state["Ddimer_age"] = 50

def update_pesi_from_ddimer():
    st.session_state["pesi_age"] = st.session_state["Ddimer_age"]
    
st.number_input("Ange ålder"
    , value=st.session_state["Ddimer_age"]
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



# def ddimer_update_slider():
#     st.session_state.Ddimer_result_slider = st.session_state.Ddimer_result
# def ddimer_update_numin():
#     st.session_state.Ddimer_result = st.session_state.Ddimer_result_slider  

# slider_value = st.slider('Ange resultat D-dimer'
#                         , min_value=0.0
#                         , max_value=10.0
#                         , value=0.5
#                         , step=0.1
#                         , key="Ddimer_result_slider"
#                         , on_change=ddimer_update_numin)

st.number_input("Ange resultat från D-dimer"
    , value=0.0
    , step=0.01
    , key="Ddimer_result"
    #, on_change=ddimer_update_slider
    )




# om man har fyllt i både ålder och resulat --> presentera slutsats
if st.session_state["Ddimer_age"] and st.session_state["Ddimer_result"]:
    if st.session_state["Ddimer_result"] > st.session_state["beslutsgräns"]:
        st.error(f"Positivt D-dimer test")
        kanpp_positiv_ddimer = st.button("Gå till Röntgen")
        if kanpp_positiv_ddimer:
            switch_page("Röntgen")
    else:
        st.success(f"Negativt D-dimer test. Lungemboli kan uteslutas.\
         Överväg annan diagnos.")
        f.klar()