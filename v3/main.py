import streamlit as st
from send import show_send_page
from inbox import show_inbox_page
from view_mail import show_view_email_page

st.title("Simple Email Service")

page = st.radio("Choose your action", ["Send Email", "Check Inbox"])

if page == "Send Email":
    show_send_page()
elif page == "Check Inbox":
    if 'selected_email' in st.session_state and 'view_email' in st.session_state and st.session_state['view_email']:
        show_view_email_page()
    else:
        show_inbox_page()
