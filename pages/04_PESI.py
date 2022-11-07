import streamlit as st
from functions import f
from PIL import Image

st.session_state.update(st.session_state)

f.hide_anchor_link()
f.hide_footer()
f.hide_hamburger()
f.hide_padding()

########################### Initialize Variables ##############################

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

st.header("PESI")

# st.number_input("Ange ålder"
#     , value=st.session_state["Ddimer_age"]
#     , step=1
#     , key="pesi_age"
#     #, on_change=age_update_slider
#     )

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
pesi_score = f.calc_score(dct_pesi, name_pesi)

#st.metric("Totalpoäng PESI", value=pesi_score)

img_string = str(pesi_score)
image = Image.open(f"pages/img_pesi/pesi_{img_string}.png")
st.image(image)