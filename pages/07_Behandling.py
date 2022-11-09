import streamlit as st

st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)

with st.expander("Behandling                           \r\n 1 Behandling 1Behandling 1Behandling 1Behandling 1Behandling 1Behandling\
     1Behandling 1Behandling 1Behandling 1Behandling 1Behandling 1Behandling 1Behandling 1Behandling 1..."):
    st.write("...")

with st.expander("Behandling 2"):
    st.write("...")

with st.expander("Behandling 3"):
    st.write("...")
'''
    <html>
  <head>
    <title>Title of the document</title>
  </head>
  <body>
    <h1>Button with line break</h1>
  </body>
'''

css_example = '''                                                                                                                                                    
        <button type="submit">My<br />Button</button>

    '''
st.write(css_example, unsafe_allow_html=True)
