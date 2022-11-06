import streamlit as st
from functions import f

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

st.info("visa bilder här baserat på svar")

#om lungemboli:
#    "Patienten har en verifierad lungemboli."
#    knapp = "Riskstratifiera enligt PESI"

#om ej:
# gå hem, avlusta session
