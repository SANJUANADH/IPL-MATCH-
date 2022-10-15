import altair as alt
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="IPL Match Data", page_icon="⬇", layout="centered"
)
st.header('IPL Matches')


df = pd.read_csv('matches.csv')
df.head(10)
st.dataframe(df.head(10))


alt.Chart(df).mark_bar().encode(
    x='season',
    y='win_by_runs',
    color = 'toss_decision'
)

st.subheader('Win by wickets - Season Pie chart Data')
# plotting the line chart
fig = px.pie(df, values="win_by_wickets", names="season")
 
# showing the plot
#fig.show()
st.plotly_chart(fig, use_container_width=True)


st.subheader('Win by runs - Season Pie chart Data')
# plotting the line chart
fig = px.pie(df, values="win_by_runs", names="season")
 
# showing the plot
#fig.show()
st.plotly_chart(fig, use_container_width=True)

st.subheader('Histogram - Winning Wickets')
san = px.histogram(df, x="winner", y="win_by_wickets")
st.plotly_chart(san, use_container_width=True)


st.subheader('Histogram - Winning Runs')
san = px.histogram(df, x="winner", y="win_by_runs")
st.plotly_chart(san, use_container_width=True)




st.subheader('3D scatter')
sun = px.scatter_3d(df, x = 'toss_winner',
                    y = 'winner',
                    z = 'season',
                    color = 'toss_decision')
st.plotly_chart(sun, use_container_width=True)
