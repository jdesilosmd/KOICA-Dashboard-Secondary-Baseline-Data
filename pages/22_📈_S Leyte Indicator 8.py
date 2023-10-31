import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


projected_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRuOM0mbpu6ThzB3HLRcKkXk3LCwE-0n-nAptaowFoNLQekgFX7FqU3IClSjl5rlX85bi-7REtyqEJt/pub?output=xlsx"
data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRp2M0ySSYySdadzJmA93oPOYsoF_0bH_dweGzqrtYn_xS3ugEtZQnIamGXuZIxxQP6TRqcuhcPrnSO/pub?output=xlsx"


st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Southern Leyte')
st.header('Indicator 8: Number of educators trained on Comprehensive Sexuality Education (CSE) in KOICA Sites')


ind8 = pd.read_excel(data_link, sheet_name=8)

tab1, tab2, tab3 = st.tabs(['Total CSE-Trained', 'Female CSE-Trained', 'Male CSE-Trained'])

with tab1:
    fig_ind8 = px.bar(ind8, x='Total CSE-Trained Educators', y='LGU',
                    orientation='h', title='Number of CSE-Trained Educators in KOICA Sites in Southern Leyte (2023)')
    fig_ind8.update_layout(yaxis={'categoryorder': 'total ascending'})

    st.plotly_chart(fig_ind8, use_container_width=True)

with tab2:
    fig_ind8 = px.bar(ind8, x='CSE-Trained Female Educators', y='LGU',
                    orientation='h', title='Number of CSE-Trained Female Educators in KOICA Sites in Southern Leyte (2023)')
    fig_ind8.update_layout(yaxis={'categoryorder': 'total ascending'})

    st.plotly_chart(fig_ind8, use_container_width=True)

with tab3:
    fig_ind8 = px.bar(ind8, x='CSE-Trained Male Educators', y='LGU',
                    orientation='h', title='Number of CSE-Trained Male Educators in KOICA Sites in Southern Leyte (2023)')
    fig_ind8.update_layout(yaxis={'categoryorder': 'total ascending'})

    st.plotly_chart(fig_ind8, use_container_width=True)



with st.expander('Click to see the data table on the number of CSE-trained educators'):
    st.markdown('###### Number of educators trained on CSE in KOICA Sites')
    st.dataframe(ind8, use_container_width=True,hide_index=True)
