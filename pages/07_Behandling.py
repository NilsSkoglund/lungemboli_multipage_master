import streamlit as st

st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)

with st.expander("Behandling 1"):
    st.write("...")

with st.expander("Behandling 2"):
    st.write("...")

with st.expander("Behandling 3"):
    st.write("...")


css_example = '''                                                                                                                                                    
        <button type="submit">My<br />Button</button>

    '''
#st.write(css_example, unsafe_allow_html=True)
