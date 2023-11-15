import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Data Source

data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ2EHB1dgXuYi5EgtgVFDs7iZp4fnchhacLHkUe3CX0KyzWDj1wnVZWYlHw44JDxC8Jafs8_ktCu-Ry/pub?output=xlsx"
data_link_sba = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTljI6-LcAcanEbMN-tdSIOT19GL7jQu9DtFNmJXdRyHxaNgcg6ZGiFFto-twKA4Q_uOJGit_Y4BLve/pub?output=xlsx"
df = pd.read_excel(data_link, sheet_name='ABR All')
df2 = pd.read_excel(data_link, sheet_name='ABR 10-14')
df_samar = df.loc[df['Location']=='Samar', :]
df_sleyte = df.loc[df['Location']=='Southern Leyte', :]
df_ph = df.loc[df['Location']=='Philippines', :]
df2_samar = df2.loc[df2['Location']=='Samar', :]
df2_sleyte = df2.loc[df2['Location']=='Southern Leyte', :]
df_abr_summary = pd.read_excel(data_link, sheet_name='ABR Projection')




### DASHBOARD CODE STARTS HERE ###
# Title

st.title('UN-KOICA Sites in Region VIII: Secondary Data for Select Indicators in Southern Leyte')
st.subheader('')
st.header('Adolescent Birth Rate (15-19 Years Only) in UN-KOICA Sites Compared to Country Data')


fig_abr_summary = px.line(df, x='Year', y='ABR (15 to 19)', template='seaborn',
                          color='Location',
                          title='Adolescent Birth Rate for the UN-KOICA Sites and the Philippines')
fig_abr_summary.update_yaxes(title_font=dict(size=20))
fig_abr_summary.update_xaxes(title_font=dict(size=20))
fig_abr_summary.update_layout(title=dict(font=dict(size=22)))

fig_abr_samar = px.scatter(df2_samar, x='Year', y='ABR (10 to 14)', template='seaborn',
                          trendline='ols', trendline_color_override='black',
                          title='Adolescent Birth Rate, Samar UN-KOICA Sites')
fig_abr_samar.update_traces(mode='lines')


fig_abr_sleyte = px.scatter(df2_sleyte, x='Year', y='ABR (10 to 14)', template='seaborn',
                          trendline='ols', trendline_color_override='black',
                          title='Adolescent Birth Rate, Southern Leyte UN-KOICA Sites')
fig_abr_sleyte.update_traces(mode='lines')


fig_abr_samar2 = px.scatter(df_samar, x='Year', y='ABR (15 to 19)', template='seaborn',
                          trendline='ols', trendline_color_override='black',
                          title='Adolescent Birth Rate, Samar UN-KOICA Sites')
fig_abr_samar2.update_traces(mode='lines')
fig_abr_samar2.update_yaxes(range=[0, 100])



fig_abr_sleyte2 = px.scatter(df_sleyte, x='Year', y='ABR (15 to 19)', template='seaborn',
                          trendline='ols', trendline_color_override='black',
                          title='Adolescent Birth Rate, Southern Leyte UN-KOICA Sites')
fig_abr_sleyte2.update_traces(mode='lines')
fig_abr_sleyte2.update_yaxes(range=[0, 100])



fig_abr_ph = px.scatter(df_ph, x='Year', y='ABR (15 to 19)', template='seaborn',
                          trendline='ols', trendline_color_override='black',
                          title='Adolescent Birth Rate, Philippines')
fig_abr_ph.update_yaxes(range=[0, 100])
fig_abr_ph.update_traces(mode='lines')



with st.expander('Click to see ABR summary for all sites and the Philippines (15-19 Years Old)'):
    st.plotly_chart(fig_abr_summary, use_container_width=True)

with st.expander('Click to see ABR summary for Samar (10-14 Years Old)'):
    st.plotly_chart(fig_abr_samar, use_container_width=True)

with st.expander('Click to see ABR summary for Southern Leyte (10-14 Years Old)'):
    st.plotly_chart(fig_abr_sleyte, use_container_width=True)

with st.expander('Click to see ABR summary for Samar (15-19 Years Old)'):
    st.plotly_chart(fig_abr_samar2, use_container_width=True)

with st.expander('Click to see ABR summary for Southern Leyte (15-19 Years Old)'):
    st.plotly_chart(fig_abr_sleyte2, use_container_width=True)

with st.expander('Click to see ABR summary for the Philippines (15-19 Years Old)'):
    st.plotly_chart(fig_abr_ph, use_container_width=True)

st.write('ABR Projection')
st.dataframe(df_abr_summary, hide_index=True)


### Additional charts:

#### ABR 10-14
fig_abr_all_10_14 = px.line(df2, x='Year', y='ABR (10 to 14)', template='seaborn',
                          color='Location',
                          title='Adolescent Birth Rate for Samar and Southern leyte Sites (10-14 Years Old)')
fig_abr_all_10_14.update_yaxes(title_font=dict(size=20))
fig_abr_all_10_14.update_xaxes(title_font=dict(size=20))
fig_abr_all_10_14.update_layout(title=dict(font=dict(size=22)))

with st.expander('Click to see ABR summary for Samar and Southern leyte Sites (10-14 Years Old)'):
    st.plotly_chart(fig_abr_all_10_14, use_container_width=True)


#### SBA
df_sba = pd.read_excel(data_link_sba)
df_sba_10_14 = df_sba.loc[df_sba['Age Range']=='10 to 14', :]
df_sba_15_19 = df_sba.loc[df_sba['Age Range']=='15 to 19', :]


#### SBA 10-14
fig_sba_all_10_14 = px.line(df_sba_10_14, x='Year', y='Percent SBA', template='seaborn',
                          color='Location',
                          title='% Births Performed by Skilled Birth Attendants (SBA), <br>All UN-KOICA Sites (10-14 Years Old)')
fig_sba_all_10_14.update_yaxes(title_font=dict(size=20))
fig_sba_all_10_14.update_xaxes(title_font=dict(size=20))
fig_sba_all_10_14.update_layout(title=dict(font=dict(size=18)))
fig_sba_all_10_14.update_yaxes(range=[0, 100])

with st.expander('Click to see SBA summary for All UN-KOICA Sites (10-14 Years Old)'):
    st.plotly_chart(fig_sba_all_10_14, use_container_width=True)


#### TBA 10-14
fig_sba_all_10_14 = px.line(df_sba_10_14, x='Year', y='Percent TBA', template='seaborn',
                          color='Location',
                          title='% Births Performed by Traditional Birth Attendants (SBA), <br>All UN-KOICA Sites (10-14 Years Old)')
fig_sba_all_10_14.update_yaxes(title_font=dict(size=20))
fig_sba_all_10_14.update_xaxes(title_font=dict(size=20))
fig_sba_all_10_14.update_layout(title=dict(font=dict(size=18)))
fig_sba_all_10_14.update_yaxes(range=[0, 100])

with st.expander('Click to see TBA summary for All UN-KOICA Sites (10-14 Years Old)'):
    st.plotly_chart(fig_sba_all_10_14, use_container_width=True)


#### SBA 15-19
fig_sba_all_15_19 = px.line(df_sba_15_19, x='Year', y='Percent SBA', template='seaborn',
                          color='Location',
                          title='% Births Performed by Skilled Birth Attendants (SBA), <br>All UN-KOICA Sites (15-19 Years Old)')
fig_sba_all_15_19.update_yaxes(title_font=dict(size=20))
fig_sba_all_15_19.update_xaxes(title_font=dict(size=20))
fig_sba_all_15_19.update_layout(title=dict(font=dict(size=18)))
fig_sba_all_15_19.update_yaxes(range=[0, 100])

with st.expander('Click to see SBA summary for All UN-KOICA Sites (15-19 Years Old)'):
    st.plotly_chart(fig_sba_all_15_19, use_container_width=True)


#### TBA 15-19
fig_sba_all_15_19 = px.line(df_sba_15_19, x='Year', y='Percent TBA', template='seaborn',
                          color='Location',
                          title='% Births Performed by Traditional Birth Attendants (SBA), <br>All UN-KOICA Sites (15-19 Years Old)')
fig_sba_all_15_19.update_yaxes(title_font=dict(size=20))
fig_sba_all_15_19.update_xaxes(title_font=dict(size=20))
fig_sba_all_15_19.update_layout(title=dict(font=dict(size=18)))
fig_sba_all_15_19.update_yaxes(range=[0, 100])

with st.expander('Click to see TBA summary for All UN-KOICA Sites (15-19 Years Old)'):
    st.plotly_chart(fig_sba_all_15_19, use_container_width=True)



### mCPR
df_mcpr = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vT-4-JITmOM93QoV_XtRCJCCibF1jofRqKnUdzZ0FKNJl4yKQupnRPaf-ZcNx7eoqHKIwum3czKjYfe/pub?output=xlsx")
fig_mcpr_all = px.line(df_mcpr, x='Year', y='mCPR (in percent)', template='seaborn',
                          color='Location',
                          title='Modern Contraceptive Prevalence Rate (mCPR), in Percent,<br>All UN-KOICA Sites (15-19 Years Old)')
fig_mcpr_all.update_yaxes(title_font=dict(size=20))
fig_mcpr_all.update_xaxes(title_font=dict(size=20))
fig_mcpr_all.update_layout(title=dict(font=dict(size=18)))
fig_mcpr_all.update_yaxes(range=[0, 8])

with st.expander('Click to see mCPR summary for All UN-KOICA Sites (15-19 Years Old)'):
    st.plotly_chart(fig_mcpr_all, use_container_width=True)
