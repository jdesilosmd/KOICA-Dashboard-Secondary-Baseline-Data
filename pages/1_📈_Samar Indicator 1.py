import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st



data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwKvqsNtKWqBgIwhVv6TDzCJMMwpr4uvBR9hdkb57qHsnFtIsJI3l2kFs1oIa2LhsQePTGtYjLIj4U/pub?output=xlsx"


ind1 = pd.read_excel(data_link, sheet_name=0)

st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Samar')


tab1, tab2 = st.tabs(['10-14 years', '15-19 years'])

with tab1:
    st.header('Indicator 1:')
    st.subheader('Adolescent Birth Rate (10-14 years of age)')

    
    
    abr_10_14_melt = ind1.loc[ind1['Age Group']=='10 to 14',
                              ['LGU',
                               'Year',
                               'ABR']]


    fig_abr_10_14_lgu_all = px.line(abr_10_14_melt, x='Year', y='ABR', template='seaborn',
                                    color='LGU',
                                    title='Adolescent Birth Rate (10-14 years) in All Samar Sites (2012-2021)')
    
    fig_abr_10_14_lgu_all.update_layout(legend=dict(orientation='h'))
    st.plotly_chart(fig_abr_10_14_lgu_all, use_container_width=True)


 # ABR 10-14 Chart per LGU   
    st.subheader('Adolescent Birth Rate Per Samar Site:')

    option_abr_10_14_table = st.selectbox(
        'Please select a City/Municipality',
        ('Basey', 'Calbayog', 'Calbiga', 'Catbalogan', 'Marabut',
            'Paranas', 'San Jose De Buan', 'San Sebastian', 'Santa Rita', 'Villareal'),
            key='selectbox_1'
    )
   
    if option_abr_10_14_table == 'Basey':
        
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Basey',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_10_14_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_10_14_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_10_14_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)

    elif option_abr_10_14_table == 'Calbayog':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Calbayog',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_10_14_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_10_14_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_10_14_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'Calbiga':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Calbiga',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black', title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_10_14_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_10_14_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_10_14_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)

    elif option_abr_10_14_table == 'Catbalogan':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Catbalogan',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_10_14_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_10_14_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_10_14_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'Marabut':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Marabut',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_10_14_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_10_14_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_10_14_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'Paranas':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Paranas',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_10_14_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_10_14_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_10_14_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'San Jose De Buan':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='San Jose De Buan',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_10_14_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_10_14_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_10_14_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'San Sebastian':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='San Sebastian',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_10_14_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_10_14_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_10_14_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'Santa Rita':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Santa Rita',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_10_14_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_10_14_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_10_14_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'Villareal':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Villareal',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_10_14_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_10_14_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_10_14_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)

#    results = px.get_trendline_results(fig_abr_10_14_lgu)
#    st.write(results.px_fit_results.iloc[0].summary())

# Summary Chart for ABR (10-14)
    fig_abr_10_14 = px.scatter(abr_10_14_melt, x='Year', y='ABR',color='LGU', facet_col='LGU', facet_col_wrap=2,
                               facet_col_spacing=0.09, template='streamlit', height=1200,
                               trendline='ols', trendline_color_override='black',
                               title='Adolescent Birth Rate (10-14 years) in KOICA Sites (2012-2021)')
    

    fig_abr_10_14.update_layout(showlegend=False,)
    fig_abr_10_14.update_traces(mode='lines')


    with st.expander('Click to see data table'):
        st.markdown('###### Adolescent Birth Rate in KOICA Sites from 2012 to 2021')
        abr_10_14_melt['Year'] = abr_10_14_melt['Year'].astype(str)
        st.dataframe(abr_10_14_melt, use_container_width=True, hide_index=True)
        abr_10_14_melt['Year'] = abr_10_14_melt['Year'].astype(int)

    with st.expander('Click to see summary chart'):
        st.plotly_chart(fig_abr_10_14, use_container_width=True)



# ABR (15-19)       

with tab2:
    st.header('Indicator 1:')
    st.subheader('Adolescent Birth Rate (15-19 years of age)')
    
    abr_15_19_melt = ind1.loc[ind1['Age Group']=='15 to 19',
                              ['LGU',
                               'Year',
                               'ABR']]

    fig_abr_15_19_lgu_all = px.line(abr_15_19_melt, x='Year', y='ABR', template='seaborn',
                                    color='LGU',
                                    title='Adolescent Birth Rate (15-19 years) in All Samar Sites (2012-2021)')
    
    fig_abr_15_19_lgu_all.update_layout(legend=dict(orientation='h'))
    st.plotly_chart(fig_abr_15_19_lgu_all, use_container_width=True)


    # ABR 15-19 Chart per LGU
   
    st.subheader('Adolescent Birth Rate Per Samar Site:')

    option_abr_15_19_table = st.selectbox(
        'Please select a City/Municipality',
        ('Basey', 'Calbayog', 'Calbiga', 'Catbalogan', 'Marabut',
            'Paranas', 'San Jose De Buan', 'San Sebastian', 'Santa Rita', 'Villareal'),
            key='selectbox_2'
    )
    
    if option_abr_15_19_table == 'Basey':
        
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Basey',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_15_19_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_15_19_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_15_19_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    
    elif option_abr_15_19_table == 'Calbayog':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Calbayog',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_15_19_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_15_19_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_15_19_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'Calbiga':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Calbiga',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_15_19_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_15_19_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_15_19_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)

    elif option_abr_15_19_table == 'Catbalogan':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Catbalogan',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_15_19_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_15_19_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_15_19_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'Marabut':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Marabut',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_15_19_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_15_19_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_15_19_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'Paranas':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Paranas',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_15_19_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_15_19_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_15_19_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'San Jose De Buan':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='San Jose De Buan',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_15_19_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_15_19_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_15_19_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'San Sebastian':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='San Sebastian',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_15_19_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_15_19_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_15_19_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'Santa Rita':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Santa Rita',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_15_19_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_15_19_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_15_19_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'Villareal':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Villareal',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        model = px.get_trendline_results(fig_abr_15_19_lgu)
        results =  model.iloc[0]["px_fit_results"]
        intercept = results.params[0]
        slope = results.params[1]
        xnew = [2022, 2023, 2024, 2025, 2026]
        ynew = [slope*x+intercept for x in xnew]
        ynew = [0 if y < 0 else y for y in ynew]
        extrapolated = {'Year': xnew, 'Predicted ABR': ynew}
        df_extrapolated = pd.DataFrame(extrapolated)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(str)
        st.write('Predictions for 2022 to 2026 using Ordinary Least Squares:')
        st.dataframe(df_extrapolated, hide_index=True)
        df_extrapolated['Year'] = df_extrapolated['Year'].astype(int)

        fig_abr_15_19_lgu.add_trace(go.Scatter(x=xnew, y=ynew,
                                               mode='markers',
                                               name='Predicted ABR'))
        fig_abr_15_19_lgu.update_layout(legend=dict(orientation='h',
                                                    yanchor='bottom',
                                                    y=-.3))
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)

    
#    results = px.get_trendline_results(fig_abr_15_19_lgu)
#    st.write(results.px_fit_results.iloc[0].summary())

# Summary graph for 15-19
    fig_abr_15_19 = px.scatter(abr_15_19_melt, x='Year', y='ABR',color='LGU', facet_col='LGU', facet_col_wrap=2,
                               facet_col_spacing=0.09, template='seaborn', height=1200,
                               trendline='ols', trendline_color_override='black',
                               title='Adolescent Birth Rate (15-19 years) in Samar Sites (2012-2021)')
    
    fig_abr_15_19.update_layout(showlegend=False)
    fig_abr_15_19.update_traces(mode='lines')




    with st.expander('Click to see data table'):
        st.markdown('###### Adolescent Birth Rate in Samar Sites from 2012 to 2021')
        abr_15_19_melt['Year'] = abr_15_19_melt['Year'].astype(str)
        st.dataframe(abr_15_19_melt, use_container_width=True, hide_index=True)
        abr_15_19_melt['Year'] = abr_15_19_melt['Year'].astype(int)
    

    with st.expander('Click to see summary chart'):
        st.plotly_chart(fig_abr_15_19, use_container_width=True)

    

