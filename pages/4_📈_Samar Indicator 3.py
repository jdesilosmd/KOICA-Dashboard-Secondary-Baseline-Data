import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwKvqsNtKWqBgIwhVv6TDzCJMMwpr4uvBR9hdkb57qHsnFtIsJI3l2kFs1oIa2LhsQePTGtYjLIj4U/pub?output=xlsx"
ind3 = pd.read_excel(data_link, sheet_name='mCPR')
all_sites = pd.read_excel(data_link, sheet_name='mCPR All')
#ind3['Year'] = ind3['Year'].astype('Int64')
ind3['Year'] = ind3['Year'].astype(str)

st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Southern Leyte')




st.header('Indicator 3:')
st.subheader('Modern Contraceptive Prevalence Rate (mCPR) in KOICA Sites')    
st.write('Indicator 3 looks at the number and proportion of adolescent girls of reproductive age (aged 15-19 years) \
            who have their need for family planning satisfied with modern methods. It is measured by looking at the \
            modern Contraceptive Prevalence Rate (mCPR), which serves as a proxy measure of access to reproductive health services.')


option_mcpr = st.selectbox(
        'Please select a City/Municipality',
        ('Basey', 'Calbayog', 'Calbiga', 'Catbalogan', 'Marabut',
            'Paranas', 'San Jose De Buan', 'San Sebastian', 'Santa Rita', 'Villareal'),
            key='selectbox_7')

if option_mcpr == 'Basey':
    fig_mcpr = px.scatter(ind3.loc[ind3['LGU']=='Basey', :], x='Year', y='mCPR', template='seaborn',
                      trendline='ols', trendline_color_override='black',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    
    fig_mcpr.update_traces(mode='lines')
    model = px.get_trendline_results(fig_mcpr)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0]
    slope = results.params[1]
    xnew = [2023, 2024, 2025, 2026]
    ynew = [slope*x+intercept for x in xnew]
    ynew = [0 if y < 0 else y for y in ynew]
    extrapolated2 = {'Year': xnew, 'Predicted ABR': ynew}
    extrapolated2 = pd.DataFrame(extrapolated2)
    extrapolated2['Year'] = extrapolated2['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
    st.dataframe(extrapolated2, hide_index=True)
    extrapolated2['Year'] = extrapolated2['Year'].astype(int)
    

    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Calbayog':
    fig_mcpr = px.scatter(ind3.loc[ind3['LGU']=='Calbayog', :], x='Year', y='mCPR', template='seaborn',
                      trendline='ols', trendline_color_override='black',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    fig_mcpr.update_traces(mode='lines')
    model = px.get_trendline_results(fig_mcpr)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0]
    slope = results.params[1]
    xnew = [2023, 2024, 2025, 2026]
    ynew = [slope*x+intercept for x in xnew]
    ynew = [0 if y < 0 else y for y in ynew]
    extrapolated2 = {'Year': xnew, 'Predicted ABR': ynew}
    extrapolated2 = pd.DataFrame(extrapolated2)
    extrapolated2['Year'] = extrapolated2['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
    st.dataframe(extrapolated2, hide_index=True)
    extrapolated2['Year'] = extrapolated2['Year'].astype(int)
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Calbiga':
    fig_mcpr = px.scatter(ind3.loc[ind3['LGU']=='Calbiga', :], x='Year', y='mCPR', template='seaborn',
                      trendline='ols', trendline_color_override='black',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    fig_mcpr.update_traces(mode='lines')
    model = px.get_trendline_results(fig_mcpr)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0]
    slope = results.params[1]
    xnew = [2023, 2024, 2025, 2026]
    ynew = [slope*x+intercept for x in xnew]
    ynew = [0 if y < 0 else y for y in ynew]
    extrapolated2 = {'Year': xnew, 'Predicted ABR': ynew}
    extrapolated2 = pd.DataFrame(extrapolated2)
    extrapolated2['Year'] = extrapolated2['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
    st.dataframe(extrapolated2, hide_index=True)
    extrapolated2['Year'] = extrapolated2['Year'].astype(int)
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Catbalogan':
    fig_mcpr = px.scatter(ind3.loc[ind3['LGU']=='Catbalogan', :], x='Year', y='mCPR', template='seaborn',
                      trendline='ols', trendline_color_override='black',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    fig_mcpr.update_traces(mode='lines')
    model = px.get_trendline_results(fig_mcpr)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0]
    slope = results.params[1]
    xnew = [2023, 2024, 2025, 2026]
    ynew = [slope*x+intercept for x in xnew]
    ynew = [0 if y < 0 else y for y in ynew]
    extrapolated2 = {'Year': xnew, 'Predicted ABR': ynew}
    extrapolated2 = pd.DataFrame(extrapolated2)
    extrapolated2['Year'] = extrapolated2['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
    st.dataframe(extrapolated2, hide_index=True)
    extrapolated2['Year'] = extrapolated2['Year'].astype(int)
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Marabut':
    fig_mcpr = px.scatter(ind3.loc[ind3['LGU']=='Marabut', :], x='Year', y='mCPR', template='seaborn',
                      trendline='ols', trendline_color_override='black',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    fig_mcpr.update_traces(mode='lines')
    model = px.get_trendline_results(fig_mcpr)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0]
    slope = results.params[1]
    xnew = [2023, 2024, 2025, 2026]
    ynew = [slope*x+intercept for x in xnew]
    ynew = [0 if y < 0 else y for y in ynew]
    extrapolated2 = {'Year': xnew, 'Predicted ABR': ynew}
    extrapolated2 = pd.DataFrame(extrapolated2)
    extrapolated2['Year'] = extrapolated2['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
    st.dataframe(extrapolated2, hide_index=True)
    extrapolated2['Year'] = extrapolated2['Year'].astype(int)
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Paranas':
    fig_mcpr = px.scatter(ind3.loc[ind3['LGU']=='Paranas', :], x='Year', y='mCPR', template='seaborn',
                      trendline='ols', trendline_color_override='black',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    fig_mcpr.update_traces(mode='lines')
    model = px.get_trendline_results(fig_mcpr)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0]
    slope = results.params[1]
    xnew = [2023, 2024, 2025, 2026]
    ynew = [slope*x+intercept for x in xnew]
    ynew = [0 if y < 0 else y for y in ynew]
    extrapolated2 = {'Year': xnew, 'Predicted ABR': ynew}
    extrapolated2 = pd.DataFrame(extrapolated2)
    extrapolated2['Year'] = extrapolated2['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
    st.dataframe(extrapolated2, hide_index=True)
    extrapolated2['Year'] = extrapolated2['Year'].astype(int)
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'San Jose De Buan':
    fig_mcpr = px.scatter(ind3.loc[ind3['LGU']=='San Jose De Buan', :], x='Year', y='mCPR', template='seaborn',
                      trendline='ols', trendline_color_override='black',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    fig_mcpr.update_traces(mode='lines')
    model = px.get_trendline_results(fig_mcpr)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0]
    slope = results.params[1]
    xnew = [2023, 2024, 2025, 2026]
    ynew = [slope*x+intercept for x in xnew]
    ynew = [0 if y < 0 else y for y in ynew]
    extrapolated2 = {'Year': xnew, 'Predicted ABR': ynew}
    extrapolated2 = pd.DataFrame(extrapolated2)
    extrapolated2['Year'] = extrapolated2['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
    st.dataframe(extrapolated2, hide_index=True)
    extrapolated2['Year'] = extrapolated2['Year'].astype(int)
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'San Sebastian':
    fig_mcpr = px.scatter(ind3.loc[ind3['LGU']=='San Sebastian', :], x='Year', y='mCPR', template='seaborn',
                      trendline='ols', trendline_color_override='black',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    fig_mcpr.update_traces(mode='lines')
    model = px.get_trendline_results(fig_mcpr)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0]
    slope = results.params[1]
    xnew = [2023, 2024, 2025, 2026]
    ynew = [slope*x+intercept for x in xnew]
    ynew = [0 if y < 0 else y for y in ynew]
    extrapolated2 = {'Year': xnew, 'Predicted ABR': ynew}
    extrapolated2 = pd.DataFrame(extrapolated2)
    extrapolated2['Year'] = extrapolated2['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
    st.dataframe(extrapolated2, hide_index=True)
    extrapolated2['Year'] = extrapolated2['Year'].astype(int)
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Santa Rita':
    fig_mcpr = px.scatter(ind3.loc[ind3['LGU']=='Santa Rita', :], x='Year', y='mCPR', template='seaborn',
                      trendline='ols', trendline_color_override='black',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    fig_mcpr.update_traces(mode='lines')
    model = px.get_trendline_results(fig_mcpr)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0]
    slope = results.params[1]
    xnew = [2023, 2024, 2025, 2026]
    ynew = [slope*x+intercept for x in xnew]
    ynew = [0 if y < 0 else y for y in ynew]
    extrapolated2 = {'Year': xnew, 'Predicted ABR': ynew}
    extrapolated2 = pd.DataFrame(extrapolated2)
    extrapolated2['Year'] = extrapolated2['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
    st.dataframe(extrapolated2, hide_index=True)
    extrapolated2['Year'] = extrapolated2['Year'].astype(int)
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Villareal':
    fig_mcpr = px.scatter(ind3.loc[ind3['LGU']=='Villareal', :], x='Year', y='mCPR', template='seaborn',
                      trendline='ols', trendline_color_override='black',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    fig_mcpr.update_traces(mode='lines')
    model = px.get_trendline_results(fig_mcpr)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0]
    slope = results.params[1]
    xnew = [2023, 2024, 2025, 2026]
    ynew = [slope*x+intercept for x in xnew]
    ynew = [0 if y < 0 else y for y in ynew]
    extrapolated2 = {'Year': xnew, 'Predicted ABR': ynew}
    extrapolated2 = pd.DataFrame(extrapolated2)
    extrapolated2['Year'] = extrapolated2['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
    st.dataframe(extrapolated2, hide_index=True)
    extrapolated2['Year'] = extrapolated2['Year'].astype(int)
    st.plotly_chart(fig_mcpr, use_container_width=True)



# OLS Analysis

with st.expander('Click to see trend analysis'):
    results = px.get_trendline_results(fig_mcpr)
    st.write(results.px_fit_results.iloc[0].summary())



# Dataframe

with st.expander('Click to see data table'):
    st.markdown('###### Modern Contraceptive Prevalence Rate (mCPR), 15-19 Females in KOICA Sites (2019-2022)')
    st.dataframe(ind3, use_container_width=True, hide_index=True)


# All Sites

fig_mcpr_all = px.scatter(all_sites, x='Year', y='mCPR', template='seaborn',
                      trendline='ols', trendline_color_override='black',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in All Samar Sites (2020-2022)')
fig_mcpr_all.update_traces(mode='lines')
st.plotly_chart(fig_mcpr_all, use_container_width=True)

# Summary Chart

with st.expander('Click to see summary chart'):
    fig_mcpr_all = px.scatter(ind3, x='Year', y='mCPR',
                        color='LGU', facet_col='LGU', facet_col_wrap=2,
                        facet_col_spacing=0.09, template='seaborn', height=1200,
                        trendline='ols', trendline_color_override='black',
                        title='Modern Contraceptive Prevalence Rate (mCPR), 15-19 Females in KOICA Sites (2019-2022)'
                      )
    
    fig_mcpr_all.update_layout(showlegend=False)
    fig_mcpr_all.update_traces(mode='lines')
    fig_mcpr_all.update_xaxes(matches=None)
    fig_mcpr_all.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
    fig_mcpr_all.update_yaxes(matches=None)
    fig_mcpr_all.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))

    st.plotly_chart(fig_mcpr_all, use_container_width=True)