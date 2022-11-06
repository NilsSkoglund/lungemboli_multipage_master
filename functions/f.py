### Hej Puran ###
################################# Imports #####################################
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

################################ Functions ####################################
############################# General functions ###############################
    # used for multiple different pages
        # calc_score
        # intialize_widget_keys

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

def initialize_widget_keys(dct, name):
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
######################### General functions THE END ###########################
################################ Lungemboli ###################################
# used only for Lungemboli page
        # sync_lungemboli_to_perc
        # lungemboli_display_viz
        # lungemboli_display_txt

def sync_lungemboli_to_perc(idx):
    st.session_state[f"perc_{idx}"] = st.session_state[f"lungemboli_{idx}"]

def lungemboli_display_viz(total_score):
	'''
    Takes a float as input and ...
	displays result image for PE. One of 24 different images based on score
	'''
	text_total_score = str(int(total_score*10))
	image = Image.open(f"img/t{text_total_score}.png")
	return st.image(image)

def lungemboli_display_txt(total_score):
    if total_score < 2:
        st.success("Patienten har en låg risk för lungemboli. För att kunna utesluta\
             lungemboli rekommenderas genomgång av PERC\
                 (Pulmonary Embolism Rule-out Criteria).")

        col1, col2, col3 , col4, col5 = st.columns(5)

        with col1:
            pass
        with col2:
            pass
        with col4:
            pass
        with col5:
            pass
        with col3:
            knapp_låg = st.button("Gå till PERC")
            if knapp_låg:
                switch_page("PERC")
    elif total_score < 6.5:
        st.warning("Patienten har en måttlig risk för lungemboli. För att undvika\
             onödig strålning rekommenderas att man tar D-dimer för att avgöra\
                 om man kan avfärda lungemboli utan ytterligare\
                     bildundersökning.")
        knapp_måttlig = st.button("Gå till D-dimer")
        if knapp_måttlig:
            switch_page("Ddimer")
    else:
        st.error("Patienten har en hög risk för lungemboli. Patienten skall\
             omgående startas på antikoagulantia-behandling och göra en akut\
                 DTLA. D-dimer är ej förlitligt för att utesluta lungemboli.")
        knapp_hög = st.button("Gå till Röntgen")
        if knapp_hög:
            switch_page("Röntgen")