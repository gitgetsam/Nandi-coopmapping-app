import streamlit as st
import pandas as pd
import altair as alt 
import matplotlib.pyplot as plt 


st.title('Graphs & Charts')
st.write("Various Visualizations of Data")

main_df = pd.read_csv('Nandi Marketplace Seller Details.csv') 

df_Town = main_df.groupby(['Town']).count()['c_id'].reset_index()
df_Town.columns = ['Town', 'No of coop']

t1, t2 = st.tabs(["Bar chart", "Pie chart"])
with t1:
    st.subheader("Bar chart with Altair")
    fig_alt = alt.Chart(df_Town).mark_bar().encode(x = 'Town', y =
    'No of coop') 
    st.altair_chart(fig_alt, use_container_width=True)
    
with t2:
    st.subheader("Pie chart with matplotlib")
    fig_mpl, ax = plt.subplots()
    ax.pie(df_Town, labels='Town')
    st.pyplot(fig_mpl)
    
st.write(f"You are logged in as {st.session_state.role}.")
