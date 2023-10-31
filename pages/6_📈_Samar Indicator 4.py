import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwKvqsNtKWqBgIwhVv6TDzCJMMwpr4uvBR9hdkb57qHsnFtIsJI3l2kFs1oIa2LhsQePTGtYjLIj4U/pub?output=xlsx"
ind4 = pd.read_excel(data_link, sheet_name='Women 15-19 Informed Decisions')

top_label = ['15-19<br>Female<br>Population', '%<br>15-19-Year-Old<br>Females<br>with<br>Positive<br>KAP<br>Change<br>in<br>ASRH']
x_data1 = ind4['% Positive KAP Change']
x_data2 = ind4['% Rest of 15-19 Female Population']
y_data = ind4['LGU']

st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Samar')
st.header('Indicator 4: Number (Percentage) of Adolescent Women Aged 15-19 Years who Make Their Own Informed Decisions Regarding Sexual Relations, Contraceptive Use, and Reproductive Health Care')
  


fig_ind4 = go.Figure()
fig_ind4.add_trace(go.Bar(x=x_data1, y=y_data, name='Adolescent 15-19-year-old women, with positive KAP change', orientation='h', marker=dict(color='#b22222')))
fig_ind4.add_trace(go.Bar(x=x_data2, y=y_data, name='Other Adolescent 15-19-year-old women', orientation='h', marker=dict(color='#6495ed'), opacity=0.2,))



fig_ind4.update_layout(barmode='stack', title='% Adolescent Women (15-19 years) with Positive Change in Knowledge, Attitude, and Practices',
                       legend=dict(
                           orientation='h',
                           yanchor="bottom",
                           y=-0.25,
                           xanchor="auto",
))


st.plotly_chart(fig_ind4)



with st.expander('Click to see data table'):
    st.markdown('###### % Adolescent Women (15-19 years) with Positive Change in Knowledge, Attitude, and Practices')
    st.dataframe(ind4, use_container_width=True, hide_index=True)