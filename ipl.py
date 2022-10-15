import altair as alt
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="IPL Match Data", page_icon="⬇", layout="centered"
)



df = pd.read_csv('matches.csv')
df.head(10)


alt.Chart(df).mark_bar().encode(
    x='season',
    y='win_by_runs',
    color = 'toss_decision'
)


# plotting the line chart
fig = px.pie(df, values="win_by_wickets", names="season")
 
# showing the plot
#fig.show()
st.plotly_chart(fig, use_container_width=True)

# plotting the line chart
fig = px.pie(df, values="win_by_runs", names="season")
 
# showing the plot
#fig.show()
st.plotly_chart(fig, use_container_width=True)
