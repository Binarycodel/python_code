import streamlit as st 
from streamlit_extras import switch_page_button




# defining global parameter
login_status = False


# app title
st.title('Drug Discovery System')


# widgets
st.header('Login In')


# status message 
def status_message(status=False, message='error'):
    if status:
        status_l1.error(message)
    else:
        status_l1.success(message)

# layout definations (three columns)
status_l1, statusl_l2 = st.columns([2,1])
email1, email2 = st.columns([2,1])
pass1, pass2 = st.columns([2,1])




email = email1.text_input("Enter Email")
password = pass1.text_input('Enter Password', type='password')

col_one , col_two = st.columns(2)


if col_one.button('login'):
    # validate credentials 
    if email == 'kinshat1995@gmail.com' and password == 'binary': 
        status_message(False, 'login in successful')
        switch_page_button.switch_page("Home")
    else: 
        status_message(True, 'Wrong Email or Password')


col_two.checkbox('Remember Me?', value=True)


