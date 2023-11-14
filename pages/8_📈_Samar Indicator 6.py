import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwKvqsNtKWqBgIwhVv6TDzCJMMwpr4uvBR9hdkb57qHsnFtIsJI3l2kFs1oIa2LhsQePTGtYjLIj4U/pub?output=xlsx"
facility_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTbcYBUdJa7vzuL98tyH7YoDFOZ_7CZtf_0Ba0iDxUyHXN6IohENnIi-yXYoT0ifNWBoooY3sjrCQKq/pub?output=xlsx"

facility_list = pd.read_excel(facility_link, sheet_name='Samar')
fig_ind6 = pd.read_excel(data_link, sheet_name='Number of AFHF')
fig_ind6.rename(columns={
    'Num_AFHF_Facilities': 'Number of AFHF',
    'All_Facilities': 'All Facilities'  
}, inplace=True)

dataset = fig_ind6.loc[:, ['LGU',
                       'Number of AFHF',
                       'All Facilities',
                       'Percentage of AFHF']]

dataset['Percentage of AFHF'] = dataset['Percentage of AFHF'].round(0)
dataset['Percentage of non-AFHF'] = 100-dataset['Percentage of AFHF']

st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Samar')
st.header('Indicator 6: Number of Adolescent-Friendly Health Facilities in Samar')


x_data1 = dataset['Percentage of AFHF']
x_data2 = dataset['Percentage of non-AFHF']
y_data = dataset['LGU']

fig_ind6 = go.Figure()
fig_ind6.add_trace(go.Bar(x=x_data1, y=y_data, name='Adolescent-Friendly Health Facilities (AFHF) in KOICA Sites (2023)', orientation='h', marker=dict(color='#b22222')))
fig_ind6.add_trace(go.Bar(x=x_data2, y=y_data, name='Facilities not Classified as Adolescent-Friendly Health Facilities (AFHF) in KOICA Sites (2023)', orientation='h', marker=dict(color='#6495ed')))


fig_ind6.update_layout(barmode='stack', title='Percentage of Adolescent-Friendly Health Facilities (AFHF) in KOICA Sites (2023)',
                        legend=dict(
                        orientation='h',
                        yanchor="bottom",
                        y=-0.35,
                        xanchor="auto"
))


st.write('')
st.write('***Note:*** *All health facilities are based on the National Health Facility Repository (NHFR) data of the Department of Health (DOH). These facilities include registered health facilities coming from both the public and private sector.*')

st.plotly_chart(fig_ind6, use_container_width=True)


with st.expander('Click to see AFHF data table'):
    st.markdown('###### % Number of Adolescent-Friendly Health Facilities in Samar')
    st.dataframe(dataset, use_container_width=True, hide_index=True)

with st.expander('Click to see the list of health facilities in the KOICA sites'):
    st.markdown('###### List of Health Facilities in the KOICA Sites (*Source: NHFR*)')
    st.dataframe(facility_list, use_container_width=True, hide_index=True)
    st.write('A complete list of all registered health facilities in the Philippines can be found in the [National Health Facility Repository (NHFR)](https://nhfr.doh.gov.ph/VActivefacilitiesList) data repository.')