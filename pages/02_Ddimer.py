import streamlit as st

st.subheader("D-dimer")

st.write("Fyll i Ålder och resultat från D-dimer testet.\
     När du är färdig, markera rutan 'D-dimer klar'")


st.number_input("Ange ålder",
    step=1,
    key="Ddimer_age"
    )

if st.session_state["Ddimer_age"]:
    st.write("hej")


st.number_input("Ange resultat D-dimer",
    key="Ddimer_result"
    )


#Ddimer_display()