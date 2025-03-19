 
import streamlit as st

# Title
st.title("Streamlit Application")

# Button
if st.button("Button"):
    st.write("Clicked!")

# Slider
value = st.slider("Select a value", min_value=0, max_value=100, value=50)
st.write(f"Selected value: {value}")

# Image with Caption
st.image("Catto.png", caption="Sample image", use_container_width=True)

