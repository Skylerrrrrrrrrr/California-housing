import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) by Skyler')
df = pd.read_csv('housing.csv')

value_filter = st.slider('Median Housing Price:', 0, 500001, 20000)  

df = df[df.median_house_value >= value_filter]


location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults


income_genre = st.sidebar.radio("Choose the income level", ('Low','Median','High'))


if income_genre == 'Low':
    df = df[df.median_income <= 2.5]
elif income_genre == 'Median':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:
    df = df[df.median_income >= 4.5]


df = df[df.ocean_proximity.isin(location_filter)]

st.subheader('see more filter on the sidebar')

st.map(df)


st.subheader('Histogram of the Median House Price')
fig, ax = plt.subplots(figsize=(20,5))
df.median_income.hist(bins=30)
st.pyplot(fig)
