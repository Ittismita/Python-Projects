import streamlit as st
from send_email import send_email
st.header("contact us")


with st.form(key="contact_form"):
    email=st.text_input("Enter email")
    msg=st.text_area("Your message")
    message=f"""\
Subject:New email from {email}

From:{email}
{msg}
    
"""
    # adding backslash implies that their is no breakline which is required when sending the subject
    # without \ implies their is a breakline which shouldnt be there while sending a subject
    button=st.form_submit_button()
    if button:
        send_email(message)
        st.info("your email was sent")
