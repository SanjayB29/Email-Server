import streamlit as st
import pandas as pd

def show_view_email_page():
    st.subheader("Email Content")
    try:
        df = pd.read_excel('emails.xlsx')
        selected_email = df[df["Unique_id"] == st.session_state['selected_email']].iloc[0]
        st.write(f"From: {selected_email['FROM']}")
        st.write(f"To: {selected_email['TO']}")
        st.write(f"Content: {selected_email['CONTENT']}")
    except Exception as e:
        st.error("Failed to load email.")
    
    if st.button("Back to Inbox"):
        st.session_state['view_email'] = False
        st.experimental_rerun()
