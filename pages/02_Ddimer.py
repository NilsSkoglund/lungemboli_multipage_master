import streamlit as st

def Ddimer_display():
    '''
    display function for D-dimer. Checks if score is above/below threshold ...
    and displays result/recommendations accordingly
    '''
    if st.session_state["Ddimer_result"] > Ddimer_beslutsgräns():
        st.write(f"Ålderbaserad beslutsgräns: >{Ddimer_beslutsgräns()}")
        st.write(f"Resultat: {round(st.session_state['Ddimer_result'],2)}")
        st.error(f"Positivt D-dimer test")
        st.markdown("[Gå vidare till röntgen](#röntgen)")
    else:
        st.write(f"Ålderbaserad beslutsgräns: >{Ddimer_beslutsgräns()}")
        st.write(f"Resultat: {round(st.session_state['Ddimer_result'],2)}")
        st.success(f"Negativt D-dimer test, lungemboli kan uteslutas")
        st.markdown("[Gå till överblick](#verblick)")

st.subheader("D-dimer")

st.write("Fyll i Ålder och resultat från D-dimer testet.\
     När du är färdig, markera rutan 'D-dimer klar'")


st.number_input("Ange ålder",
    step=1,
    key="Ddimer_age"
    )

if st.session_state["Ddimer_age"]:
    beslutsgräns = max([0.50, st.session_state["Ddimer_age"]*0.01])
    st.write(f"Beslutsgräns: {beslutsgräns}")


st.number_input("Ange resultat D-dimer",
    key="Ddimer_result"
    )


#Ddimer_display()