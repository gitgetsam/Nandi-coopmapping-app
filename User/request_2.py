import streamlit as st 
import pandas as pd
import pydeck as pdk 
import plotly.express as px 



st.title(' A Map of All Coops')
st.write("Amazing!")

main_df = pd.read_csv('Nandi Marketplace Seller Details.csv')

#main_df.dropna(how='any', inplace=True)
#viewport location
sf_initial_view = pdk.ViewState(   #viewport location
latitude=0,
longitude=35.5,
zoom=8,
bearing=0,
pitch=0
)
#layer to dispay on a map
sp_layer = pdk.Layer(
    'ScatterplotLayer',
    data = main_df,
    get_position = ['latitude', 'longitude'],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    extruded=True,
    coverage=1,
    opacity=0.8,
    #get_radius=0.2,
    get_fill_color='c_id',
    get_line_color=[0,0,0],
    get_radius=30)

#plotly
fig_pl = px.scatter_mapbox(main_df, lon=main_df['longitude'], lat=main_df['latitude'], zoom=8, hover_data=['Seller Name', 'Products'], opacity=0.8, color='c_id', title="Nandi Map", width=900, height=700)
fig_pl.update_layout(mapbox_style="open-street-map")
fig_pl.update_layout(margin={"r":0, "t":50, "l":0, "b":10})

t1, t2, t3 = st.tabs(["Plotly Map", "pyDeck Map", "st Map"])
with t1:
    st.plotly_chart(fig_pl, use_container_width=True)

with t2:
    st.pydeck_chart(pdk.Deck(width="100%", height=700, initial_view_state=sf_initial_view, layers = [sp_layer]), use_container_width=True)

with t3:
    main_df = main_df.dropna(subset=['latitude', 'longitude'])
    st.map(main_df)
    

st.write(f"You are logged in as {st.session_state.role}.")  
