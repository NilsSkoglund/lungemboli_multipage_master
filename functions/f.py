### Hej Puran ###
################################# Imports #####################################
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import base64
from streamlit_lottie import st_lottie
import requests


################################ Functions ####################################
############################# markdown functions ##############################
    # used for multiple different pages
        # col_control_rem
        # button_style
        # reduce_padding
        # hide_img_fullscreen
        # hide_anchor_link
        # hide_padding
        # hide_hamburger
        # hide_footer
        # control_tooltip

def col_control_rem():
    st.markdown("""
                <style>
                .css-ocqkz7 [data-testid=stVerticalBlock]{
                    gap: 0.1rem;
                }
                </style>
                """
                , unsafe_allow_html=True)

def button_style():
    st.markdown("""
                <style>
                .stButton > button {
                    color: #ffffff;
                    background: #1f498c;
                    border: 1px solid #ffffff;
                }
                </style>
                """
                , unsafe_allow_html=True)


def reduce_padding():
    st.markdown("""
                <style>
                [data-testid=stVerticalBlock]{gap: 0.7rem;}
                </style>
                """
                , unsafe_allow_html=True)

def hide_img_fullscreen():
    st.markdown('''
                <style>
                button[title="View fullscreen"]{
                    visibility: hidden;}
                </style>
                '''
                , unsafe_allow_html=True)

st.markdown(hide_img_fullscreen, unsafe_allow_html=True)

def hide_anchor_link():
    st.markdown("""
        <style>
        .css-15zrgzn {display: none}
        .css-eczf16 {display: none}
        .css-jn99sy {display: none}
        </style>
        """
        , unsafe_allow_html=True)

def hide_padding_top():
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
    </style>
        """
        , unsafe_allow_html=True)

def hide_hamburger():
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
        , unsafe_allow_html=True)

def hide_footer():
    st.markdown("""
        <style>
        footer {visibility: hidden;}
        </style>
        """
        , unsafe_allow_html=True)

def control_tooltip():
    st.markdown("""
                <style>
                div[data-baseweb="tooltip"] {
                width: 100px;
                }
                </style>
                """, unsafe_allow_html=True)

############################# General functions ###############################
    # used for multiple different pages
        # klar
        # calc_score
        # intialize_widget_keys
def klar():
    return st.markdown('<a href="/Lungemboli" style="display: block;\
    text-align: center; color: #FF4B4B; font-family: serif; font-size: 20px;"\
    target="_self">Avsluta</a>', unsafe_allow_html=True)

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
        # load_lottieurl
        # lungemboli_display_txt

def sync_lungemboli_to_perc(idx):
    st.session_state[f"perc_{idx}"] = st.session_state[f"lungemboli_{idx}"]

def lungemboli_display_viz_v1(total_score):
    '''
    Takes a float as input and ...
    displays result image for PE. One of 24 different images based on score
    '''
    text_total_score = str(int(total_score*10))
    image = Image.open(f"img/wells/t{text_total_score}.png")
    return st.image(image)

def lungemboli_display_viz_v2(total_score):
    '''
    Takes a float as input and ...
    displays result image for PE. One of 24 different images based on score
    '''
    text_total_score = str(int(total_score*10))
    image_path = f"img/t{text_total_score}.png"
    with open(image_path, 'rb') as f:
        image = f.read()

        image_bytes = base64.b64encode(image).decode()
        local_file = f'<p style="text-align:center;"><img src="data:image/jpeg;base64,{image_bytes}" alt="Image" width = 600> </p>'

    return st.markdown(local_file, unsafe_allow_html = True)

def lungemboli_display_txt(total_score):
    if total_score < 2:
        st.success("Patienten har en l??g risk f??r lungemboli. F??r att kunna\
             utesluta lungemboli rekommenderas genomg??ng av PERC\
                 (Pulmonary Embolism Rule-out Criteria).")
    elif total_score < 6.5:
        st.warning("Patienten har en m??ttlig risk f??r lungemboli. F??r att\
             undvika on??dig str??lning rekommenderas att man tar D-dimer f??r\
             att avg??ra om man kan avf??rda lungemboli utan ytterligare\
             bildunders??kning.")
    else:
        st.error("Patienten har en h??g risk f??r lungemboli. Patienten skall\
             omg??ende startas p?? antikoagulantia-behandling och g??ra en akut\
                 DTLA. D-dimer ??r ej tillf??rlitligt f??r att utesluta lungemboli.")

def lungemboli_display_button(total_score):
    if total_score < 2:
        knapp_l??g = st.button("G?? vidare till PERC")
        if knapp_l??g:
            switch_page("PERC")

    elif total_score < 6.5:
        knapp_m??ttlig = st.button("Ange D-dimer svar")
        if knapp_m??ttlig:
            switch_page("D-dimer")
    else:
        knapp_h??g = st.button("G?? till R??ntgen")
        if knapp_h??g:
            switch_page("R??ntgen")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def lungemboli_display_lottie(total_score):
    if total_score < 2:
        try:
            lottie_url = "https://assets7.lottiefiles.com/packages/lf20_inp8ddzw.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json, height=20, width=148.45)
        except:
            pass

    elif total_score < 6.5:
        try:
            lottie_url = "https://assets7.lottiefiles.com/packages/lf20_inp8ddzw.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json, height=20, width=167)
        except:
            pass
    else:
        try:
            lottie_url = "https://assets7.lottiefiles.com/packages/lf20_inp8ddzw.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json, height=20, width=124)
        except:
            pass

def perc_display_lottie():
    try:
        lottie_url = "https://assets7.lottiefiles.com/packages/lf20_inp8ddzw.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(lottie_json, height=20, width=167)
    except:
        pass
    else:
        pass

def ddimer_display_lottie():
    try:
        lottie_url = "https://assets7.lottiefiles.com/packages/lf20_inp8ddzw.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(lottie_json, height=20, width=124)
    except:
        pass
    else:
        pass

def dtla_display_lottie():
    try:
        lottie_url = "https://assets7.lottiefiles.com/packages/lf20_inp8ddzw.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(lottie_json, height=20, width=192)
    except:
        pass
    else:
        pass

def pesi_display_lottie(width):
    try:
        lottie_url = "https://assets7.lottiefiles.com/packages/lf20_inp8ddzw.json"
        lottie_json = load_lottieurl(lottie_url)
        return st_lottie(lottie_json, height=20, width=width)
    except:
        pass