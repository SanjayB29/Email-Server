import streamlit as st
import pandas as pd
from datetime import datetime

def show_send_page():
    st.subheader("Send an Email")

    from_email = st.text_input("Your Email")
    to_email = st.text_input("Recipient's Email")
    content = st.text_area("Email Content")

    if st.button("Send Email"):
        unique_id = datetime.now().strftime("%Y%m%d%H%M%S")
        new_email = pd.DataFrame([[to_email, from_email, content, unique_id]], columns=["TO", "FROM", "CONTENT", "Unique_id"])
        
        try:
            df = pd.read_excel('emails.xlsx')
            df = pd.concat([df, new_email], ignore_index=True)
        except FileNotFoundError:
            df = new_email
            
        df.to_excel('emails.xlsx', index=False)
        st.success("Email Sent!")

    if st.button("Go Back"):
        st.experimental_rerun()
