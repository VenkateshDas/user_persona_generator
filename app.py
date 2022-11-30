import streamlit as st
from upg.upg import UserPersonaGenerator

# create a streamlit app with a title, a header, and text input for name, designation, and comments
st.title("User Persona Generator")
st.subheader("Enter a name, designation, and comments below to generate a user persona.")
st.write("Note: This is a demo app. The generated persona is not real.")
name = st.text_input("Name", placeholder="John Doe")
designation = st.text_input("Designation", placeholder="Software Engineer")
st.write("Note: Comments about the key points the user persona should cover.")
comments = st.text_input("Comments", placeholder="Likes to play tennis and looking for a sport club app.")

# create a button to generate the user persona
if st.button("Generate User Persona"):
    upg = UserPersonaGenerator()
    persona = upg.generate_persona(name, designation, comments)
    st.write("Here is your user persona:")
    # display the generated user persona in a text box
    st.text_area("", persona, height=500)
