import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from sklearn.linear_model import LinearRegression


projected_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRuOM0mbpu6ThzB3HLRcKkXk3LCwE-0n-nAptaowFoNLQekgFX7FqU3IClSjl5rlX85bi-7REtyqEJt/pub?output=xlsx"
data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwKvqsNtKWqBgIwhVv6TDzCJMMwpr4uvBR9hdkb57qHsnFtIsJI3l2kFs1oIa2LhsQePTGtYjLIj4U/pub?output=xlsx"

projected_10_14 = pd.read_excel(projected_link, '10-14 Women')
projected_15_19 = pd.read_excel(projected_link, '15-19 Women')
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

    option_abr_10_14_table = st.selectbox(
        'Please select a City/Municipality',
        ('Basey', 'Calbayog', 'Calbiga', 'Catbalogan', 'Marabut',
            'Paranas', 'San Jose De Buan', 'San Sebastian', 'Santa Rita', 'Villareal'),
            key='selectbox_1'
    )


# ABR 10-14 Chart per LGU
    
    if option_abr_10_14_table == 'Basey':
        
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Basey',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)

    elif option_abr_10_14_table == 'Calbayog':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Calbayog',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'Calbiga':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Calbiga',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black', title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)

    elif option_abr_10_14_table == 'Catbalogan':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Catbalogan',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'Marabut':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Marabut',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'Paranas':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Paranas',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'San Jose De Buan':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='San Jose De Buan',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'San Sebastian':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='San Sebastian',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'Santa Rita':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Santa Rita',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
    
    elif option_abr_10_14_table == 'Villareal':
        fig_abr_10_14_lgu = px.scatter(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Villareal',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
        fig_abr_10_14_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)

    results = px.get_trendline_results(fig_abr_10_14_lgu)
    st.write(results.px_fit_results.iloc[0].summary())

# Summary Chart for ABR (10-14)
    fig_abr_10_14 = px.scatter(abr_10_14_melt, x='Year', y='ABR',color='LGU', facet_col='LGU', facet_col_wrap=2,
                               facet_col_spacing=0.09, template='streamlit', height=1200,
                               trendline='ols', trendline_color_override='black',
                               title='Adolescent Birth Rate (10-14 years) in KOICA Sites (2012-2021)')
    

    fig_abr_10_14.update_layout(showlegend=False)
    fig_abr_10_14.update_traces(mode='lines')
    fig_abr_10_14.update_xaxes(matches=None)
    fig_abr_10_14.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
    fig_abr_10_14.update_yaxes(matches=None)
    fig_abr_10_14.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))

    with st.expander('Click to see data table'):
        st.markdown('###### Adolescent Birth Rate in KOICA Sites from 2012 to 2021')
        st.dataframe(abr_10_14_melt, use_container_width=True, hide_index=True)

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


    option_abr_15_19_table = st.selectbox(
        'Please select a City/Municipality',
        ('Basey', 'Calbayog', 'Calbiga', 'Catbalogan', 'Marabut',
            'Paranas', 'San Jose De Buan', 'San Sebastian', 'Santa Rita', 'Villareal'),
            key='selectbox_2'
    )


# ABR 15-19 Chart per LGU
    
    if option_abr_15_19_table == 'Basey':
        
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Basey',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    
    elif option_abr_15_19_table == 'Calbayog':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Calbayog',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'Calbiga':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Calbiga',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)

    elif option_abr_15_19_table == 'Catbalogan':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Catbalogan',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'Marabut':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Marabut',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'Paranas':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Paranas',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'San Jose De Buan':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='San Jose De Buan',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'San Sebastian':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='San Sebastian',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'Santa Rita':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Santa Rita',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
    
    elif option_abr_15_19_table == 'Villareal':
        fig_abr_15_19_lgu = px.scatter(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Villareal',:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='black',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
        fig_abr_15_19_lgu.update_traces(mode='lines')
        st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)

    
    results = px.get_trendline_results(fig_abr_15_19_lgu)
    st.write(results.px_fit_results.iloc[0].summary())

# Summary graph for 15-19
    fig_abr_15_19 = px.scatter(abr_15_19_melt, x='Year', y='ABR',color='LGU', facet_col='LGU', facet_col_wrap=2,
                               facet_col_spacing=0.09, template='seaborn', height=1200,
                               trendline='ols', trendline_color_override='black',
                               title='Adolescent Birth Rate (15-19 years) in Samar Sites (2012-2021)')
    
    fig_abr_15_19.update_layout(showlegend=False)
    fig_abr_15_19.update_traces(mode='lines')
    fig_abr_15_19.update_xaxes(matches=None)
    fig_abr_15_19.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
    fig_abr_15_19.update_yaxes(matches=None)
    fig_abr_15_19.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))


    with st.expander('Click to see data table'):
        st.markdown('###### Adolescent Birth Rate in Samar Sites from 2012 to 2021')
        st.dataframe(abr_15_19_melt, use_container_width=True, hide_index=True)
    

    with st.expander('Click to see summary chart'):
        st.plotly_chart(fig_abr_15_19, use_container_width=True)
