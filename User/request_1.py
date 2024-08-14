import streamlit as st 
import pandas as pd 

st.write("Very Limited Colums")

main_df = pd.read_csv("Nandi Marketplace Seller Details.csv")

st.write(main_df.loc[:,["Seller Name", 'Products', 'type', 'category', 'Town']])

st.write(f"You are logged in as {st.session_state.role}.")
