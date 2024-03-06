import streamlit as st
import pandas as pd
from openpyxl import load_workbook
from authorization_signup_login import login  # Assuming login function is available for use
from send_mail import send_mail  # Adjust import according to your project structure

# Page Configuration
st.set_page_config(page_title="Main Page - Email Server App", layout="wide")

def show_main_page(user):
    """Shows the main page after successful login with options to send and view received mails."""
    st.write(f"Welcome, {user}!")
    
    # Navigation
    option = st.selectbox("Choose an option:", ["Send New Mail", "Check Received Mails"])
    
    if option == "Send New Mail":
        show_send_mail_page(user)
    elif option == "Check Received Mails":
        show_received_mails(user)

def show_send_mail_page(sender):
    """Displays the UI for sending a new email."""
    st.title("Send Mail")
    to = st.text_input("To Email:")
    content = st.text_area("Content:")
    
    if st.button("Send"):
        success, message = send_mail(sender, to, content)  # send_mail() function needs to be defined
        if success:
            st.success("Email sent successfully.")
        else:
            st.error(message)

def show_received_mails(username):
    """Displays received emails for the user."""
    # Assuming emails are stored in an Excel file named 'email_server.xlsx' with a sheet for each user
    try:
        df = pd.read_excel('email_server.xlsx', sheet_name=username)
    except Exception as e:
        st.error("Failed to load emails.")
        return

    received_mails = df[['From', 'Contents', 'MailID']].dropna().reset_index(drop=True)

    st.subheader("Received Mails")
    for index, row in received_mails.iterrows():
        with st.expander(f"From: {row['From']} (Mail ID: {row['MailID']})"):
            st.write(f"Contents: {row['Contents']}")

if __name__ == '__main__':
    # This example assumes that 'user' is set in st.session_state upon successful login
    # For demonstration purposes, let's set a placeholder user
    if 'user' not in st.session_state:
        st.session_state['user'] = 'placeholder_user'  # Placeholder; replace with actual login logic
    
    show_main_page(st.session_state['user'])
