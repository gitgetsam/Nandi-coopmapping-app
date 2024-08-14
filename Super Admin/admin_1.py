import streamlit as st 
import pandas as pd
import time

#password_attempt = st.text_input('Please Enter The Password. Hint: password')

#if password_attempt == 'password':
 #   placeholder = st.empty()
  #  placeholder = st.success("Logged in")
   # time.sleep(0.5)
    #placeholder.empty()
#else:
 #   st.stop()
    

st.write("All Colums")
main_df = pd.read_csv("Nandi Marketplace Seller Details.csv")
st.write( main_df)


st.write(f"You are logged in as {st.session_state.role}.")
