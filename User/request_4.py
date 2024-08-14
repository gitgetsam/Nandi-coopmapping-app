import streamlit as st
import pandas as pd
import altair as alt
import pydeck as pdk


st.title("Types of Coops in Nandi County")

towns = ['Morisot', 'Kapkerer', 'Kabiyet', 'Kapsabet', 'Nandi Hills', 'Baraton University', 'Chepsangor', 'Chemundu', 'Chepterit']

st.markdown('Use this app to Know the loations of Coops')
selected_town = st.selectbox('The Town?', towns)

selected_category = st.selectbox('Category of Coops',
['Agriculture', 'Manufacturing'])
selected_type = st.selectbox('The Type of Coops',
['Maize', 'Millet', 'Dairy', 'Poultry', 'Tea', 'Water', 'Bread', 'Horticulture', 'Manufacturing', 'Potato', 'Artifacts', 'Coffee'])

main_df = pd.read_csv('Nandi Marketplace Seller Details.csv')
main_df.dropna(how='any', inplace=True).dropna(how='any', inplace=True)
main_df = main_df[main_df['Town'] == selected_town]

nan_initial_view = pdk.ViewState(
latitude=0,
longitude=35,
zoom=9
)
st.pydeck_chart(pdk.Deck(
map_style='mapbox://styles/mapbox/light-v9',
initial_view_state=nan_initial_view,
))

py_layer = pdk.Layer(
'py Layer',
data = main_df,
get_position = ['longitude', 'latitude'],
get_radius=30)
st.pydeck_chart(pdk.Deck(
map_style='mapbox://styles/mapbox/light-v9',
initial_view_state=nan_initial_view,
layers = [py_layer]
))

st.write(f"You are logged in as {st.session_state.role}.")








