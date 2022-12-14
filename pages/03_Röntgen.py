import streamlit as st
from functions import f
from streamlit_extras.switch_page_button import switch_page

st.session_state.update(st.session_state)

f.button_style()
f.hide_anchor_link()
f.hide_footer()
f.hide_hamburger()
f.hide_padding_top()

# Initialize variables for radiology_report
	# dct with report_answer:score
	# name for key
dct_radiology_report={
	"Ingen lungemboli": 0,
    "Perifer lungemboli": 1,
	"Lungemboli på subsegmentell nivå": 2,
	"Lungemboli på segmentell nivå": 3,
	"Lungemboli på lobär nivå": 4,
	"Sadelemboli": 5
	}

name_rad = "dtla"

st.header("Röntgen")
    
for i, j in enumerate(dct_radiology_report.items()):
    st.checkbox(
        j[0]\
        , key=f"{name_rad}_{i}"
    )

st.warning("visa bilder här baserat på svar")

if "verifierad_lungemboli" not in st.session_state:
    st.session_state["verifierad_lungemboli"] = False

for i in range(1,6):
    if st.session_state[f"dtla_{i}"]:
        st.session_state["verifierad_lungemboli"] = True
        break
    else:
        st.session_state["verifierad_lungemboli"] = False

if st.session_state["dtla_0"] and st.session_state["verifierad_lungemboli"]:
    st.session_state["verifierad_lungemboli"] = False
    st.warning("Konflikterande information.")
elif st.session_state["dtla_0"]:
    st.session_state["verifierad_lungemboli"] = False
    st.success("Lungemboli kan uteslutas. Överväg annan diagnos.")
    f.klar()
elif st.session_state["verifierad_lungemboli"]:
    st.error("Patienten har en verifierad lungemboli. Bedöm vårdnivå med hjälp av PESI.")

    col1, col2 = st.columns([1, 1])
    f.col_control_rem()
    with col1:
        knapp_pesi = st.button("Riskstratifiera enligt PESI")
        f.dtla_display_lottie()
        if knapp_pesi:
            switch_page("PESI")
