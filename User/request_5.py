import streamlit as st 
import pandas as pd
import pydeck as pdk
import plotly.express as px 

st.write("This app Displays the location of Coops by Town")

main_df = pd.read_csv('Nandi Marketplace Seller Details.csv')

towns = [None,  'Morisot', 'Kapkerer', 'Kabiyet', 'Kapsabet', 'Nandi Hills', 'Baraton University', 'Chepsangor', 'Chemundu', 'Chepterit']
selected_town = st.selectbox('Select the Town?', towns)

if selected_town == None:
    main_df = main_df[main_df['Town'] == None] 
if selected_town == 'Morisot':
    main_df = main_df[main_df['Town'] == 'Morisot'] 
if selected_town == 'Kapkerer':
    main_df = main_df[main_df['Town'] == 'Kapkerer'] 
if selected_town == 'Kabiyet':
    main_df = main_df[main_df['Town'] == 'Kabiyet'] 
if selected_town == 'Kapsabet':
    main_df = main_df[main_df['Town'] == 'Kapsabet'] 
if selected_town == 'Nandi Hills':
    main_df = main_df[main_df['Town'] == 'Nandi Hills']
if selected_town == 'Baraton University':
    main_df = main_df[main_df['Town'] == 'Baraton University']
if selected_town == 'Chepsangor':
    main_df = main_df[main_df['Town'] == 'Chepsangor']
if selected_town == 'Chemundu':
    main_df = main_df[main_df['Town'] == 'Chemundu']
elif selected_town == 'Chepterit':
    main_df = main_df[main_df['Town'] == 'Chepterit']
else:
    pass

fig_pl = px.scatter_mapbox(main_df, lon=main_df['longitude'], lat=main_df['latitude'], zoom=9, hover_data=['Seller Name', 'Products'], opacity=0.8, color='c_id', title="Nandi Map by Town", width=900, height=700)
fig_pl.update_layout(mapbox_style="open-street-map")
fig_pl.update_layout(margin={"r":0, "t":50, "l":0, "b":10})

st.plotly_chart(fig_pl, use_container_width=True)


st.write(f"You are logged in as {st.session_state.role}.")


#nan_initial_view = pdk.ViewState(
#latitude=0,
#longitude=35.5,
#zoom=9)
#st.pydeck_chart(pdk.Deck(
#initial_view_state=nan_initial_view,))

#py_layer = pdk.Layer(
#'ScatterplotLayer',
#data = main_df,
#get_position = ['longitude', 'latitude'],
#get_radius=30)
#st.pydeck_chart(pdk.Deck(initial_view_state=nan_initial_view,layers = [py_layer]))
