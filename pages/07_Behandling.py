import streamlit as st

st.session_state.update(st.session_state)
horizontal_line = """<hr style="height:1px;background-color:#dcdcdc;" /> """
## Fragmin
st.markdown(horizontal_line, unsafe_allow_html=True)
st.header("Fragmin (dalteparin)")
st.markdown(
"""
**Dos:** 200 E/kg/dygn

**Att tänka på:** Överkänslighet, vikt, koagulationsrubbning, HIT
"""
)
with st.expander("Visa kontraindikationer", expanded=False):
    st.markdown(
    """
    **Absoluta kontraindikationer**
    - Ti överkänslighet för Fragmin
    """
)
    st.write("")
    st.markdown(
    """
    **Relativa ki**
    - Pågående blödning
    - Tidigare HIT typ II
    - Svår koagulationsrubbning
    """
    )

## Eliquis
st.markdown(horizontal_line, unsafe_allow_html=True)
st.header("Eliquis (apixaban)")
st.markdown(
"""
**Dos:** 10 mg x 2 i 7 dagar, därefter 5 mg x 2

**Att tänka på:** Överkänsliget, njurfunktion, leversjukdom,\
     blödning, annan ak behandlig, obesitas op.
"""
)
with st.expander("Visa kontraindikationer", expanded=False):
    st.markdown(
    """
    **Absoluta kontraindikationer:**
    - Ti överkänslighet Eliquis
    """
)
    st.write("")
    st.markdown(    
    """
    **Relativa ki:**
    - Graviditet
    - Pågående blödning
    - Leversjukdom associerad med koagulationsrubbning
    - Tillstånd med ökad blödningsrisk såsom esofagus varicer
    - Svår koagulationsrubbning
    - Ti obesitasoperation
    - Samtidig behandling med annat antikoagulantium
    """
)
st.markdown(horizontal_line, unsafe_allow_html=True)

# with st.expander("Eliquis (apixaban)", expanded=True):
#     st.markdown(
# """
# **Dos:**
# - 10 mg x 2 i 7 dagar, därefter 5 mg x 2
# """
# )
#     st.write("")
#     st.markdown(
# """
# **Absoluta kontraindikationer:**
# - Ti överkänslighet Eliquis
# """
# )
#     st.write("")
#     st.checkbox("Visa mer info", key = "mer_info_2")
#     if st.session_state["mer_info_2"]: 
#         st.markdown(
# """
# **Relativa ki:**
# - Graviditet
# - Pågående blödning
# - Leversjukdom associerad med koagulationsrubbning
# - Tillstånd med ökad blödningsrisk såsom esofagus varicer
# - Svår koagulationsrubbning
# - Ti obesitasoperation
# - Samtidig behandling med annat antikoagulantium
# """
# )


