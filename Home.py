import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Data Source

data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ2EHB1dgXuYi5EgtgVFDs7iZp4fnchhacLHkUe3CX0KyzWDj1wnVZWYlHw44JDxC8Jafs8_ktCu-Ry/pub?output=xlsx"
df = pd.read_excel(data_link, sheet_name='ABR All')
df_samar = df.loc[df['Location']=='Samar', :]
df_sleyte = df.loc[df['Location']=='Southern Leyte', :]
df_ph = df.loc[df['Location']=='Philippines', :]


### DASHBOARD CODE STARTS HERE ###
# Title

st.title('UN-KOICA Sites in Region VIII: Secondary Data for Select Indicators in Southern Leyte')
st.subheader('')
st.header('Adolescent Birth Rate (15-19 Years Only) in UN-KOICA Sites Compared to Country Data')


fig_abr_summary = px.line(df, x='Year', y='ABR (15 to 19)', template='seaborn',
                          color='Location',
                          title='Adolescent Birth Rate for the UN-KOICA Sites and the Philippines')

fig_abr_samar = px.line(df_samar, x='Year', y='ABR (15 to 19)', template='seaborn',
                          title='Adolescent Birth Rate, Samar UN-KOICA Sites')


fig_abr_sleyte = px.line(df_sleyte, x='Year', y='ABR (15 to 19)', template='seaborn',
                          title='Adolescent Birth Rate, Southern Leyte UN-KOICA Sites')


fig_abr_ph = px.line(df_ph, x='Year', y='ABR (15 to 19)', template='seaborn',
                          title='Adolescent Birth Rate, Philippines')



with st.expander('Click to see ABR summary for all sites and the Philippines'):
    st.plotly_chart(fig_abr_summary, use_container_width=True)

with st.expander('Click to see ABR summary for Samar'):
    st.plotly_chart(fig_abr_samar, use_container_width=True)

with st.expander('Click to see ABR summary for Southern Leyte'):
    st.plotly_chart(fig_abr_sleyte, use_container_width=True)

with st.expander('Click to see ABR summary for the Philippines'):
    st.plotly_chart(fig_abr_ph, use_container_width=True)




