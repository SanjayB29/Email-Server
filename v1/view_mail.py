import streamlit as st
import pandas as pd
from openpyxl import load_workbook

def find_mail_details(mail_id, username):
    """
    Searches for an email by mail_id in the given username's sheet.
    Returns a dictionary with mail details if found, else None.
    """
    try:
        df = pd.read_excel('email_server.xlsx', sheet_name=username)
        mail_row = df[df['MailID'] == mail_id]

        if not mail_row.empty:
            # Assuming mail could be either sent or received
            if 'From' in mail_row:
                return {'from_to': mail_row.iloc[0]['From'], 'content': mail_row.iloc[0]['Contents']}
            else:
                return {'from_to': mail_row.iloc[0]['To'], 'content': mail_row.iloc[0]['Contents']}
    except Exception as e:
        st.error(f"Error finding mail: {e}")
    return None

def view_mail_page(username, mail_id):
    """
    Displays mail details for a given mail_id and provides a back button.
    """
    mail_details = find_mail_details(mail_id, username)

    if mail_details:
        st.title("Mail Details")
        st.write(f"From/To: {mail_details['from_to']}")
        st.write(f"Content: {mail_details['content']}")
    else:
        st.error("Mail not found.")

    if st.button("Back"):
        st.session_state['current_page'] = 'main_page'  # Adjust as per your page routing logic
        st.experimental_rerun()
