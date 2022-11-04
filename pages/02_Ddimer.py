import streamlit as st
from streamlit_extras.switch_page_button import switch_page

########################### Initialize Variables ##############################

if "beslutsgräns" not in st.session_state:
    st.session_state["beslutsgräns"] = 50

############################## Program and UI #################################

st.subheader("D-dimer")
st.write("Ange ålder och resultat från D-dimer testet")

st.number_input("Ange ålder",
    step=1,
    key="Ddimer_age"
    )

if st.session_state["Ddimer_age"]:
    st.session_state["beslutsgräns"] = max([0.50, st.session_state["Ddimer_age"]*0.01])
    st.write(f"Åldersbaserad beslutsgräns: {st.session_state["beslutsgräns"]}")

st.number_input("Ange resultat D-dimer",
    key="Ddimer_result"
    )
if st.session_state["Ddimer_result"]:
    st.write(f"Resultat: {st.session_state["Ddimer_result"]}")

if st.session_state["Ddimer_result"] > st.session_state["beslutsgräns"]:
    st.error(f"Positivt D-dimer test")
    kanpp_positiv_ddimer = st.button("Gå till Röntgen")
    if kanpp_positiv_ddimer:
        switch_page("Röntgen")
else:
    st.success(f"Negativt D-dimer test, Lungemboli kan uteslutas")