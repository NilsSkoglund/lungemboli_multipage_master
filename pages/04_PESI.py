import streamlit as st
from functions import f
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.session_state.update(st.session_state)

f.button_style()
f.reduce_padding()
f.hide_anchor_link()
f.hide_footer()
f.hide_hamburger()
f.hide_padding_top()
f.hide_img_fullscreen()
f.control_tooltip()
f.col_control_rem()

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

if "Ddimer_age" not in st.session_state:
    st.session_state["Ddimer_age"] = 50

st.number_input("Ange ålder"
    , value=50
    , step=1
    , key="pesi_age"
    )

# Create checkboxes
for i, j in enumerate(dct_pesi.items()):
    st.checkbox(
        j[0]\
        , key=f"{name_pesi}_{i}"\
        , help=f"Poäng: {j[1]}"
        )
pesi_score = f.calc_score(dct_pesi, name_pesi)

pesi_score += st.session_state["pesi_age"]

#st.metric("Totalpoäng PESI", value=pesi_score)

with st.expander("Riskvisualisering", expanded=True):
    pesi_score = min(180, pesi_score)
    img_string = str(pesi_score)
    image = Image.open(f"pages/img_pesi/pesi_{img_string}.png")
    st.image(image)

container = st.container()

col1, col2 = st.columns([1, 1])

from threading import Thread

if pesi_score < 86: 
    container.warning("Låg risk. (gränsen är för tillfället satt till 86)")
    with col1:
        knapp_behandling = st.button("Gå vidare till behandling")
        f.pesi_display_lottie(188.75)
        if knapp_behandling:
            switch_page("Behandling")
else:
    container.error("Hög risk. (gränsen är för tillfället satt till 86)")
    with col1:
            knapp_inläggning = st.button("Gå vidare till inläggning")
            knapp_ultraljud = st.button("Gå vidare till ultraljud")
            a = f.pesi_display_lottie(183.19)
        # if __name__ == '__main__':
        #     t1 = Thread(target=f.pesi_display_lottie,args=(183.19,))
        #     t2 = Thread(target=f.pesi_display_lottie, args=(169.89,))
            
        #     t1.start()
        #     t2.start()
        #     knapp_inläggning = st.button("Gå vidare till inläggning")
        #     knapp_ultraljud = st.button("Gå vidare till ultraljud")
        #     t2.run()
    
    if knapp_inläggning:
        switch_page("Inläggning")
    if knapp_ultraljud:
        switch_page("Ultraljud")

    css_example = '''                                                                                                                                                    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">                                                                                                    

    <i class="fa-solid fa-phone"></i> 
    <a style="color:white" href='tel:+4673-712-9109'>Ring Jour</a>

    '''
    st.write(css_example, unsafe_allow_html=True)