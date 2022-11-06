import streamlit as st
from functions import f

st.session_state.update(st.session_state)

f.hide_anchor_link()
f.hide_footer()
f.hide_hamburger()
f.hide_padding()

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

tooltip_style = """
<style>
div[data-baseweb="tooltip"] {
  width: 100px;
}
</style>
"""
st.markdown(tooltip_style,unsafe_allow_html=True)
for i, j in enumerate(dct_pesi.items()):
    st.checkbox(
        j[0]\
        , key=f"{name_pesi}_{i}"\
        , help=f"Poäng: {j[1]}"
        )

st.markdown("---")
pesi_score = f.calc_score(dct_pesi, name_pesi)
st.metric("Totalpoäng PESI", value=pesi_score)


#text_total_score = str(int(total_score*10))
#image = 
Image.open(f"img_pesi/pesi_{str(pesi_score)}.png")
#return st.image(image)