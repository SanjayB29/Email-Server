import streamlit as st
import pandas as pd
from authorization_login_signup import signup, login
from send_mail import send_mail_page
from view_mail import view_mail_page

# Page Configuration
st.set_page_config(page_title="Email Server App", layout="wide")

def show_signup_page():
    """Shows the signup page and handles user registration."""
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Signup"):
        success, message = signup(username, email, password)
        if success:
            st.success("Successfully signed up. Please log in.")
            st.session_state['page'] = 'login'
        else:
            st.error(message)

def show_login_page():
    """Shows the login page and handles user authentication."""
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        success, username, message = login(email, password)
        if success:
            st.session_state['page'] = 'main'
            st.session_state['user'] = username  # Store the username in session state
        else:
            st.error(message)

def show_main_page():
    """Shows the main page after successful login."""
    st.write(f"Welcome, {st.session_state['user']}!")
    option = st.selectbox("Choose an option:", ["Send New Mail", "Check Received Mails"])
    
    if option == "Send New Mail":
        st.session_state['page'] = 'send_mail'
    elif option == "Check Received Mails":
        st.session_state['page'] = 'received_mails'

def show_received_mails(username):
    """Function to display received mails for the user."""
    # Load user's mails from Excel
    user_df = pd.read_excel('email_server.xlsx', sheet_name=username)
    received_mails = user_df[['From', 'Contents', 'MailID']].dropna().reset_index(drop=True)

    st.subheader("Received Mails")
    for index, row in received_mails.iterrows():
        st.text(f"From: {row['From']}")
        st.text(f"Contents: {row['Contents'][:50]}...")  # Show a preview
        view_button = st.button("View", key=f"view{index}")
        
        if view_button:
            # Use the MailID to view details; set it in session state
            st.session_state['page'] = f'view_mail:{row["MailID"]}'

if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

# Page routing
if st.session_state['page'] == 'login':
    show_login_page()
elif st.session_state['page'] == 'signup':
    show_signup_page()
elif st.session_state['page'] == 'main':
    show_main_page()
elif st.session_state['page'] == 'send_mail':
    send_mail_page(st.session_state['user'])  # Pass the username to the send_mail_page function
elif st.session_state['page'] == 'received_mails':
    show_received_mails(st.session_state['user'])
elif st.session_state['page'].startswith('view_mail:'):
    mail_id = st.session_state['page'].split(':')[1]
    view_mail_page(st.session_state['user'], mail_id)  # Pass the username and mail_id to the view_mail_page function
