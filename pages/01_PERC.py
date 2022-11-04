import streamlit as st
from functions import f
from streamlit_extras.switch_page_button import switch_page

st.session_state.update(st.session_state)

st.checkbox("test me!", value=st.session_state["test"], key="test2")

st.header("PERC")
st.write("När du är färdig med formuläret, markera rutan 'PERC klar'")

st.info("5 av 8 frågor i PERC ingår i Wells' PE formuläret.\
 När Wells' PE markeras som klar ges dessa frågor samma svar i PERC-formuläret.\
 Frågorna blir även låsta.")
st.markdown("---")

f.create_checkboxes_perc(st.session_state["perc_dct"], st.session_state["perc_name"])

st.markdown("---")
st.checkbox("PERC klar", 
    key="perc_mark_inside", 
    value=st.session_state["perc_done"],
    on_change=f.change_perc_in_to_out)
if st.session_state["perc_done"] == True:
    if calc_score(st.session_state["perc_dct"], st.session_state["perc_name"]) > 0:
        st.warning("Inget av kriterierna får vara uppfyllt")
        st.markdown("[Gå vidare till D-dimer](#d-dimer)")
        
    else:
        st.success("PERC-regeln ej bruten, lungemboli kan uteslutas")
        st.markdown("[Gå till Överblick](#verblick)")
