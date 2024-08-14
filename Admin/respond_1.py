import streamlit as st 
import pandas as pd


#@st.cache_data(experimental_allow_widgets=True)  # 👈 Set the parameter
#def get_data():
 #   password_guess = st.text_input('What is the Password? Hint: password2')
  #  if password_guess != 'password2':
   #     st.stop()
    #return password_guess


st.write("Limited Colums")

main_df = pd.read_csv("Nandi Marketplace Seller Details.csv")

st.write(main_df.loc[:,["Seller Name", 'Products', 'type', 'category', 'Contact Person Name', 'Phone Number', 'Email', 'Town']])

st.write(f"You are logged in as {st.session_state.role}.")