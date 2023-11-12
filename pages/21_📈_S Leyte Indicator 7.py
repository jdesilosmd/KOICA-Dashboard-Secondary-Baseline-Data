import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


projected_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRuOM0mbpu6ThzB3HLRcKkXk3LCwE-0n-nAptaowFoNLQekgFX7FqU3IClSjl5rlX85bi-7REtyqEJt/pub?output=xlsx"
data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRp2M0ySSYySdadzJmA93oPOYsoF_0bH_dweGzqrtYn_xS3ugEtZQnIamGXuZIxxQP6TRqcuhcPrnSO/pub?output=xlsx"
ind7 = pd.read_excel(data_link, sheet_name='Number of HW Trained on ASRH')
ind7 = ind7.fillna(0)
ind7 = ind7.astype({'Foundational Course': np.int64,
                    'ADEPT': np.int64,
                    'FPCBT 1': np.int64,
                    'FPCBT 2': np.int64,
                    'HYO PLUS': np.int64,
                    'BEMONC': np.int64}, errors='ignore')

st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Southern Leyte')
st.header('Indicator 7: Number of Health Workers Trained in Adolescent Sexual and Reproductive Health (ASRH)')



st.dataframe(ind7)

