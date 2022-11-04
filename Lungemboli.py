import streamlit as st
from functions import f
from streamlit_extras.switch_page_button import switch_page




st.checkbox("press me!", key="test")










f.initialize_session_variables()

############################### Initialize PE #################################

f.initialize_keys(st.session_state["wells_pe_dct"], st.session_state["wells_pe_name"])

############################## Initialize PERC ################################

f.initialize_keys(st.session_state["perc_dct"], st.session_state["perc_name"])

################################## Program ####################################
#################################### PE #######################################

st.header("Well's Kriterier för Lungemboli")
st.markdown("---")
f.create_checkboxes_pe(st.session_state["wells_pe_dct"], st.session_state["wells_pe_name"])
st.markdown("---")

# Kolla om PERC är bruten
if f.calc_score(st.session_state["perc_dct"], st.session_state["perc_name"]) > 0:
        st.error("PERC bruten")

# räkna ut och visa poäng för PE
st.session_state["total_score_pe"] =\
        f.calc_score(st.session_state["wells_pe_dct"], st.session_state["wells_pe_name"])
f.pe_display(st.session_state["total_score_pe"])


################################## PE KLAR ####################################

################################ Nästa steg ###################################
if st.session_state["total_score_pe"] < 2 and f.calc_score(st.session_state["perc_dct"], st.session_state["perc_name"]) == 0:
    st.info("Patienten har en låg risk för lungemboli. För att kunna utesluta\
             lungemboli rekommenderas genomgång av PERC (Pulmonary Embolism Rule-out Criteria).")
    knapp_låg = st.button("Gå till PERC")
    if knapp_låg:
        switch_page("PERC")
elif st.session_state["total_score_pe"] < 2 and f.calc_score(st.session_state["perc_dct"], st.session_state["perc_name"]) > 0:
    
    knapp_låg_perc_bruten = st.button("Gå till D-dimer")
    if knapp_låg_perc_bruten:
        switch_page("Ddimer")
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




#html_låg = 'Om Låg --> <a href="/PERC" target="_self">PERC</a>'
#st.markdown(html_låg, unsafe_allow_html=True)

#html_låg_perc = 'Om Låg och PERC bruten --> <a href="/Ddimer" target="_self">D-dimer</a>'
#st.markdown(html_låg_perc, unsafe_allow_html=True)

#html_måttlig = 'Om Måttlig --> <a href="/Ddimer" target="_self">D-dimer</a>'
#st.markdown(html_måttlig, unsafe_allow_html=True)

#html_hög = 'Om Hög --> <a href="/Röntgen" target="_self">Röntgen</a>'
#st.markdown(html_hög, unsafe_allow_html=True)
