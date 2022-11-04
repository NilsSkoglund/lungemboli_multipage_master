import streamlit as st
from functions import f
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

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
		key = f"{name}_{index}"
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

def pe_display(total_score):
	'''
    Takes a float as input and ...
	displays result image for PE. One of 24 different images based on score
	'''
	text_total_score = str(int(total_score*10))
	image = Image.open(f"img/t{text_total_score}.png")
	return st.image(image)

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


for i, j in enumerate(dct_lungemboli.items()):
    if i < 5:
        st.checkbox(
            j[0],\
            key=f"{name_lungemboli}_{i}",\
            help=f"Poäng: {j[1]}",\
            on_change=sync_lungemboli_to_perc, 
            args=(i,))
    else:
        st.checkbox(
            j[0],\
            key=f"{name_lungemboli}_{i}",\
            help=f"Poäng: hej {j[1]}")


st.session_state["total_score_pe"] = calc_score(dct_lungemboli, name_lungemboli)

pe_display(st.session_state["total_score_pe"])

if st.session_state["total_score_pe"] < 2:
    st.info("Patienten har en låg risk för lungemboli. För att kunna utesluta\
             lungemboli rekommenderas genomgång av PERC (Pulmonary Embolism Rule-out Criteria).")
    knapp_låg = st.button("Gå till PERC")
    if knapp_låg:
        switch_page("PERC")
elif st.session_state["total_score_pe"] < 6.5:
    st.info("Patienten har en måttlig risk för lungemboli. \
        För att undvika onödig strålning rekommenderas att man tar D-dimer för \
            att avgöra om man kan avfärda lungemboli utan ytterligare bildundersökning.")
    knapp_måttlig = st.button("Gå till D-dimer")
    if knapp_måttlig:
        switch_page("Ddimer")
else:
    st.info("Patienten har en hög risk för lungemboli. Patienten skall omgående\
         startas på antikoagulantia-behandling och göra en akut DTLA. D-dimer\
             är ej förlitligt för att utesluta lungemboli.")
    knapp_hög = st.button("Gå till Röntgen")
    if knapp_hög:
        switch_page("Röntgen")