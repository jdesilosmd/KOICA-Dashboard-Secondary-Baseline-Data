import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwKvqsNtKWqBgIwhVv6TDzCJMMwpr4uvBR9hdkb57qHsnFtIsJI3l2kFs1oIa2LhsQePTGtYjLIj4U/pub?output=xlsx"
ind7 = pd.read_excel(data_link, sheet_name='Number of HW Trained on ASRH')


st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Samar')
st.header('Indicator 7: Number of Health Workers Trained in Adolescent Sexual and Reproductive Health (ASRH)')


st.dataframe(ind7)

