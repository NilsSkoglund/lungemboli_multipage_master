import streamlit as st
from functions import f

st.session_state.update(st.session_state)

########################### Initialize Variables ##############################

st.header("PESI")

dct_pesi = {
	"Manligt kön":30,
	"Malignitet":30,
	"Hjärtsvikt":10,
	"Kronisk lungsjukdom":10,
	"Puls ≥110/min":20,
	"Systoliskt BT <100 mmHG":30,
	"Andningsfrekvens ≥30/min":20,
	"Kroppstemperatur <36ºC":20,
	"Mental påverkan":60,
	"Syrgassaturation <90%":20
}

name_pesi = "pesi"

############################## Program and UI #################################

for i, j in enumerate(dct_pesi.items()):
    st.checkbox(
        j[0]\
        , key=f"{name_pesi}_{i}"\
        , help=f"Poäng: {j[i]}"
        )

st.markdown("---")
st.metric("Totalpoäng PESI", value=f.calc_score(dct_pesi, name_pesi))