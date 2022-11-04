import streamlit as st
from functions import f

def calc_score(dct, name):
	'''
    Takes a dictionary (dct) and a string (name) as inputs and ...
	calculates total score for:
        DVT
        PE
        PERC
        PESI
	'''
	total_score = 0
	for index, question in enumerate(dct):
		key = f"{name}{index}"
		if st.session_state[key]: # if True means the checkbox is ticked
			total_score += dct.get(question)
	return total_score

def initialize_keys(dct, name):
	'''
    Takes a dictionary (dvt) and a string (name) as inputs and ...
	initializes session state 'keys' for:
        DVT
        PE
        PERC
        PESI
    
    Note! More session state 'keys' are initialized ...
    at other places for other purposes for DVT, PE, PERC & PESI
	'''
	for index, j in enumerate(dct):
		key = f"{name}_{index}"
		if key not in st.session_state:
			st.session_state[key] = False
	return None

dct_perc = {
    "Kliniska tecken på DVT": 1,
    "Tidigare LE/DVT diagnos": 1,
    "Hjärtfrekvens >100/min": 1,
    "Hemoptys": 1,
    "Immobiliserad i >3 dagar / Opererad senaste 4 veckor": 1,
    "Ålder ≥50": 1,
    "Saturation >94% utan syrgas": 1,
    "Östrogenbehandling": 1,
    }

name_perc = "perc"

dct_lungemboli = {
    "Kliniska tecken på DVT": 3,
    "Tidigare LE/DVT diagnos": 1.5,
    "Hjärtfrekvens >100/min": 1.5,
    "Hemoptys": 1,
    "Immobiliserad i >3 dagar / Opererad senaste 4 veckor": 1.5,
    "LE mer sannolik än annan diagnos": 3,
    "Malignitet behandlad inom 6 mån eller palliation": 1
    }

name_lungemboli = "lungemboli"

if "total_score_pe" not in st.session_state:
	    st.session_state["total_score_pe"] = 0


initialize_keys(dct_lungemboli, name_lungemboli)

def sync_lungemboli_to_perc(idx):

    st.session_state[f"perc_{idx}"] = st.session_state[f"lungemboli_{idx}"]

st.checkbox(
    dct_lungemboli[0][0],\
    key=f"lungemboli_0",\
    help=f"Poäng: {dct_lungemboli[0][1]}",\
    on_change=lungemboli_01_to_perc_01, 
    args=())

def create_checkboxes_lungemboli():
    for i, j in enumerate(dct_lungemboli):
        st.checkbox(
            j[0],\
            key=f"{name_lungemboli}_{i}",\
            help=f"Poäng: {j[1]}",\
            on_change=sync_lungemboli_to_perc, 
            args=(i,))