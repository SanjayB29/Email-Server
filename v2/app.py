import streamlit as st
# Ensure these imports match your module and structure names
from authorization_signup_login import signup, login

# Page Configuration
st.set_page_config(page_title="Email Server App", layout="wide")

def show_initial_choice():
    """Shows the initial page to choose directly between Signup or Login."""
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Signup"):
            st.session_state['page'] = 'signup'
            
    with col2:
        if st.button("Login"):
            st.session_state['page'] = 'login'

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
            st.session_state['page'] = 'main_page'
            st.session_state['user'] = username  # Store the username in session state
            st.experimental_rerun()  # Rerun the app to redirect to the main page
        else:
            st.error(message)

# Page routing
if 'page' not in st.session_state:
    st.session_state['page'] = 'initial_choice'  # Set to 'initial_choice' to show the initial selection

if st.session_state['page'] == 'initial_choice':
    show_initial_choice()
elif st.session_state['page'] == 'login':
    show_login_page()
elif st.session_state['page'] == 'signup':
    show_signup_page()
elif st.session_state['page'] == 'main_page':
    # Redirect to the main page script
    st.experimental_rerun()
