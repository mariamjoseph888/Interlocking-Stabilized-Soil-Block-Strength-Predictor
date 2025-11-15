import streamlit as st

st.title("ISSB Strength Predictor")

cement = st.number_input("Cement content (%)", min_value=0.0)
lime = st.number_input("Lime content (%)", min_value=0.0)

if st.button("Predict Strength"):
    fcb1 = 2.283 * (cement - (3 * lime / 761)) - 9.995
    fcw2 = 2.64 * fcb1 + 0.08
    st.write(f"Block Strength: {round(fcb1, 3)} MPa")
    st.write(f"Wall Strength: {round(fcw2, 3)} MPa")
