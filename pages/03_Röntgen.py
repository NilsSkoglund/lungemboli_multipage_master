import streamlit as st

st.session_state.update(st.session_state)

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 2rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
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