import streamlit as st


st.write("""Applicazione web inutile""")

x = st.slider("Seleziona un numero", min_value = 1, max_value = 100)

st.write(f"""
Il numero scelto è {x}, il quadrato è {x**2}, mentre il cubo è {x**3}
""")
