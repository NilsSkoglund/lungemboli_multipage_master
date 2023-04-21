import streamlit as st
from functions import f
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages

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

############################# language choice #################################
with st.sidebar:
    st.radio(label="Language"
             , options=["Svenska", "English"]
             , key="lang"
             , label_visibility="collapsed"
             , horizontal=True)
    
if "lang" not in st.session_state:
    st.session_state["lang"] = "Svenska"

if st.session_state["lang"] == "Svenska":
    hide_pages(["X-ray"])
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
    age_input = "Ange ålder"
    risk_viz = "Riskvisualisering"
    nästa = "Gå vidare"
else:
    hide_pages(["Röntgen"])
    dct_pesi = {
    "Male gender": 30,
    "Malignancy": 30,
    "Heart failure": 10,
    "Chronic lung disease": 10,
    "Pulse ≥110/min": 20,
    "Systolic BP <100 mmHg": 30,
    "Respiratory rate ≥30/min": 20,
    "Body temperature <36ºC": 20,
    "Mental impairment": 60,
    "Oxygen saturation <90%": 20
}
    age_input = "Enter age"
    risk_viz = "Risk visualization"
    nästa = "Proceed"

########################### Initialize Variables ##############################
st.session_state["pesi_påbörjad"] = True

name_pesi = "pesi"

############################## Program and UI #################################

st.header("PESI")

if "Ddimer_age" not in st.session_state:
    st.session_state["Ddimer_age"] = 50

st.number_input(age_input
    , step=1
    , key="Ddimer_age"
    )

# Create checkboxes
for i, j in enumerate(dct_pesi.items()):
    st.checkbox(
        j[0]\
        , key=f"{name_pesi}_{i}"\
        #, help=f"Poäng: {j[1]}"
        )
pesi_score = f.calc_score(dct_pesi, name_pesi)

pesi_score += st.session_state["Ddimer_age"]

#st.metric("Totalpoäng PESI", value=pesi_score)

with st.expander(risk_viz, expanded=True):
    pesi_score = min(180, pesi_score)
    img_string = str(pesi_score)
    image = Image.open(f"pages/img_pesi/pesi_{img_string}.png")
    st.image(image)

container = st.container()

col1, col2 = st.columns([1, 1])

# if pesi_score < 66: 
#     container.warning("Riskgrupp 1.")
# elif pesi_score < 86:
#     container.warning("Riskgrupp 2.")
# elif pesi_score < 106:
#     container.warning("Riskgrupp 3.")
# elif pesi_score < 126:
#     container.warning("Riskgrupp 4.")
# elif pesi_score > 125:
#     container.warning("Riskgrupp 5.")

st.markdown("""
    <style>
    .css-ocqkz7 [data-testid=stVerticalBlock]{
        gap: 0.1rem;
    }
    </style>
    """, unsafe_allow_html=True)
st.session_state["pesi_score"] = pesi_score
knapp_behandling = st.button(nästa)
if st.session_state["lang"] == "English":
    f.pesi_display_lottie(81)
else:
    f.pesi_display_lottie(89)
if knapp_behandling:
    switch_page("guide")

############################ Flow Illustration  ###############################
with st.sidebar:
    if st.session_state["lang"] == "English":
        f.display_flow_v2_eng()
    else:
        f.display_flow_v2()


# if pesi_score < 66: 
#     container.warning("Riskgrupp 1.")
#     with col1:
#         knapp_behandling = st.button("Gå vidare till behandling")
#         f.pesi_display_lottie(188.75)
#         if knapp_behandling:
#             switch_page("Behandling")
# else:
#     container.error("Hög risk. (gränsen är för tillfället satt till 86)")
#     with col1:
#             knapp_inläggning = st.button("Gå vidare till inläggning")
#             f.pesi_display_lottie(183.19)
#             knapp_ultraljud = st.button("Gå vidare till ultraljud")
#             f.pesi_display_lottie(169.89)
    
#     if knapp_inläggning:
#         switch_page("Inläggning")
#     if knapp_ultraljud:
#         switch_page("Ultraljud")

#     css_example = '''                                                                                                                                                    
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">                                                                                                    

#     <i class="fa-solid fa-phone"></i> 
#     <a style="color:white" href='tel:+4673-712-9109'>Ring Jour</a>

#     '''
#     st.write(css_example, unsafe_allow_html=True)