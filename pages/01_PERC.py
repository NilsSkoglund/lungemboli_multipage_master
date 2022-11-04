import streamlit as st

st.session_state.update(st.session_state)

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


st.header("PERC")

st.info("5 av 8 frågor i PERC ingår i Wells' PE formuläret.\
 När dessa frågor besvaras i Wells' PE formuläret \
    ges de samma svar i PERC-formuläret.")

for i, j in enumerate(dct_perc.items()):
    if i < 5:
        st.checkbox(
            j[0],\
            value=st.session_state[f"{name_lungemboli}_{i}"],\
            key=f"{name_perc}_{i}")
    else:
        st.checkbox(
            j[0],\
            key=f"{name_perc}_{i}")


if calc_score(dct_perc, name_perc) > 0:
    st.warning("Inget av kriterierna får vara uppfyllt")
    st.markdown("[Gå vidare till D-dimer](#d-dimer)")
    
else:
    st.success("PERC-regeln ej bruten, lungemboli kan uteslutas")
    st.markdown("[Gå till Överblick](#verblick)")
