import streamlit as st
from functions import f
from streamlit_extras.switch_page_button import switch_page

st.session_state.update(st.session_state)

f.hide_anchor_link()
f.hide_footer()
f.hide_hamburger()
f.hide_padding()

# Initialize variables for radiology_report
	# dct with report_answer:score
	# name for key
dct_radiology_report={
	"Ingen lungemboli": 0,
	"Lungemboli på subsegmentell nivå": 1,
	"Lungemboli på segmentell nivå": 2,
	"Lungemboli på lobär nivå": 3,
	"Sadelemboli": 4
	}

name_rad = "dtla"

st.header("Röntgen")

for i, j in enumerate(dct_radiology_report.items()):
    st.checkbox(
        j[0]\
        , key=f"{name_rad}_{i}"
    )

st.warning("visa bilder här baserat på svar")

if st.session_state["dtla_0"]:
    st.success("Lungemboli kan uteslutas. Överväg annan diagnos.")
    st.markdown(
        '''
            <style>
            a
            {
            color: red;
            }
            </style>
        '''
        , unsafe_allow_html=True)

    st.markdown('<a href="/Lungemboli" target="_self">KLAR</a>', unsafe_allow_html=True)

verifierad_lungemboli = False

for i in range(1,5):
    if st.session_state[f"dtla_{i}"]:
        verifierad_lungemboli = True

if verifierad_lungemboli:
    st.info("Patienten har en verifierad lungemboli")
    knapp_pesi = st.button("Riskstratifiera enligt PESI")
    if knapp_pesi:
        switch_page("PESI")


#om lungemboli:
#    "Patienten har en verifierad lungemboli."
#    knapp = "Riskstratifiera enligt PESI"

#om ej:
# gå hem, avlusta session
