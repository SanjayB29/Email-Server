import streamlit as st
import pandas as pd

def show_inbox_page():
    st.subheader("Check Your Inbox")

    email_id = st.text_input("Your Email ID")
    
    if email_id:
        try:
            df = pd.read_excel('emails.xlsx')
            inbox = df[df["TO"] == email_id][["FROM", "Unique_id"]]
            selected_email = st.selectbox("Select an Email", options=inbox["Unique_id"], format_func=lambda x: f"From: {inbox[inbox['Unique_id'] == x]['FROM'].values[0]}, ID: {x}")
            
            if st.button("View Email"):
                st.session_state['selected_email'] = selected_email
                st.session_state['view_email'] = True
                st.experimental_rerun()
        except FileNotFoundError:
            st.error("Inbox is empty.")

    if st.button("Go Back"):
        st.experimental_rerun()

