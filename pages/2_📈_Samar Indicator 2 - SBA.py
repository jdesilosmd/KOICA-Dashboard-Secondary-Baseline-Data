import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwKvqsNtKWqBgIwhVv6TDzCJMMwpr4uvBR9hdkb57qHsnFtIsJI3l2kFs1oIa2LhsQePTGtYjLIj4U/pub?output=xlsx"
ind2a = pd.read_excel(data_link, sheet_name=1)
ind2b = pd.read_excel(data_link, sheet_name=2)

st.title('UN-KOICA Sites in Region VIII: Secondary Data for Select Indicators in UN-KOICA Sites in Samar')


st.header('Indicator 2:')
st.subheader('Number of adolescent births attended by skilled health personnel among adolescents aged 10-19 in UN-KOICA Sites in Samar')





ind2_tab1, ind2_tab2 = st.tabs(["By Mother's Residence",
                                'By Place of Occurrence'])


maternal_10_14 = ind2a.loc[ind2a['Age Range']=='10 to 14',
                           ['LGU',
                            'Year',
                            'Total',
                            'SBA',
                            'TBA',
                            'Others',
                            'Not Stated']]


maternal_15_19 = ind2a.loc[ind2a['Age Range']=='15 to 19',
                           ['LGU',
                            'Year',
                            'Total',
                            'SBA',
                            'TBA',
                            'Others',
                            'Not Stated']]


# By Mother's Residence

with ind2_tab1:      
        
    # Show Table


    maternal_10_14['Year'] = maternal_10_14['Year'].astype(str)
    maternal_10_14['SBA/Total'] = maternal_10_14['SBA']/maternal_10_14['Total']
    maternal_10_14['TBA/Total'] = maternal_10_14['TBA']/maternal_10_14['Total']
    maternal_10_14['Others/Total'] = maternal_10_14['Others']/maternal_10_14['Total']
    maternal_10_14['NS/Total'] = maternal_10_14['Not Stated']/maternal_10_14['Total']
    maternal_10_14 = maternal_10_14.fillna(0)


    maternal_15_19['Year'] = maternal_15_19['Year'].astype(str)
    maternal_15_19['SBA/Total'] = maternal_15_19['SBA']/maternal_15_19['Total']
    maternal_15_19['TBA/Total'] = maternal_15_19['TBA']/maternal_15_19['Total']
    maternal_15_19['Others/Total'] = maternal_15_19['Others']/maternal_15_19['Total']
    maternal_15_19['NS/Total'] = maternal_15_19['Not Stated']/maternal_15_19['Total']
    maternal_15_19 = maternal_15_19.fillna(0)


    with st.expander('Please click to see the chart for the combined data of the 10 sites in this province'):
        maternal_all = pd.read_excel(data_link, sheet_name='SBA Maternal All')

        maternal_10_14_all = maternal_all.loc[maternal_all['Age Range']=='10 to 14', :]
        maternal_10_14_all['Year'] = maternal_10_14_all['Year'].astype(str)
        maternal_10_14_all['SBA/Total'] = maternal_10_14_all['SBA']/maternal_10_14_all['Total']
        maternal_10_14_all['TBA/Total'] = maternal_10_14_all['TBA']/maternal_10_14_all['Total']
        maternal_10_14_all['Others/Total'] = maternal_10_14_all['Others']/maternal_10_14_all['Total']
        maternal_10_14_all['NS/Total'] = maternal_10_14_all['Not Stated']/maternal_10_14_all['Total']
        maternal_10_14_all = maternal_10_14_all.fillna(0)

        maternal_15_19_all = maternal_all.loc[maternal_all['Age Range']=='15 to 19', :]
        maternal_15_19_all = pd.read_excel(data_link, sheet_name='SBA Occurrence All')
        maternal_15_19_all['Year'] = maternal_15_19_all['Year'].astype(str)
        maternal_15_19_all['SBA/Total'] = maternal_15_19_all['SBA']/maternal_15_19_all['Total']
        maternal_15_19_all['TBA/Total'] = maternal_15_19_all['TBA']/maternal_15_19_all['Total']
        maternal_15_19_all['Others/Total'] = maternal_15_19_all['Others']/maternal_15_19_all['Total']
        maternal_15_19_all['NS/Total'] = maternal_15_19_all['Not Stated']/maternal_15_19_all['Total']
        maternal_15_19_all = maternal_15_19_all.fillna(0)

        fig_graph_10_14_all = px.scatter(maternal_10_14_all, x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in Samar Sites (2012-2021)')
        
        fig_graph_15_19_all = px.scatter(maternal_10_14_all, x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in Samar Sites (2012-2021)')

        analyze = st.radio('Select Age Group:',
                           ['10-14 Years', '15-19 Years'],
                           horizontal=True)
        if analyze == '10-14 Years':
            fig_graph_10_14_all.update_traces(mode='lines')
            st.plotly_chart(fig_graph_10_14_all, use_container_width=True)
            st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
            results = px.get_trendline_results(fig_graph_10_14_all)
            st.write(results.px_fit_results.iloc[0].summary())
        
        elif analyze == '15-19 Years':
            fig_graph_15_19_all.update_traces(mode='lines')
            st.plotly_chart(fig_graph_15_19_all, use_container_width=True)
            st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
            results = px.get_trendline_results(fig_graph_15_19_all)
            st.write(results.px_fit_results.iloc[0].summary())



    option_table = st.selectbox(
        'Please select a City/Municipality',
        ('Basey', 'Calbayog', 'Calbiga', 'Catbalogan', 'Marabut',
            'Paranas', 'San Jose De Buan', 'San Sebastian', 'Santa Rita', 'Villareal'),
            key='selectbox_3'
    )

    
    if option_table == 'Basey':
                    
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_1'
        )

       
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Basey',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Basey',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Basey',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Basey',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Basey',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Basey',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Basey',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Basey',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis1'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())


        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Basey', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Basey', :],
                hide_index=True, use_container_width=True)

            
    ### Calbayog

    elif option_table == 'Calbayog':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_2'
        )
        
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbayog',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbayog',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbayog',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbayog',:], x='Year', y='TBA/Total', template='seaborn',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbayog',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbayog',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbayog',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbayog',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis2'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Calbayog', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Calbayog', :],
                hide_index=True, use_container_width=True)
            

    ### Calbiga
        
    elif option_table == 'Calbiga':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_3'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbiga',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbiga',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbiga',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbiga',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbiga',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbiga',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbiga',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbiga',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis3'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Calbiga', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Calbiga', :],
                hide_index=True, use_container_width=True)
            

    
    ### Catbalogan

    elif option_table == 'Catbalogan':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_4'
        )
        
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Catbalogan',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Catbalogan',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Catbalogan',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Catbalogan',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Catbalogan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Catbalogan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Catbalogan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Catbalogan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis4'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Catbalogan', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Catbalogan', :],
                hide_index=True, use_container_width=True)
            

    
    ### Marabut

    elif option_table == 'Marabut':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_5'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Marabut',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Marabut',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Marabut',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Marabut',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Marabut',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Marabut',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Marabut',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Marabut',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis5'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Marabut', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Marabut', :],
                hide_index=True, use_container_width=True)
            

        
    ### Paranas

    elif option_table == 'Paranas':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_6'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Paranas',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Paranas',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Paranas',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Paranas',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Paranas',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Paranas',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Paranas',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Paranas',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis6'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Paranas', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Paranas', :],
                hide_index=True, use_container_width=True)
            


    ### San Jose De Buan
        
    elif option_table == 'San Jose De Buan':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_7'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Jose De Buan',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Jose De Buan',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Jose De Buan',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Jose De Buan',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Jose De Buan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Jose De Buan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Jose De Buan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Jose De Buan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis7'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='San Jose De Buan', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='San Jose De Buan', :],
                hide_index=True, use_container_width=True)
            

        
    ### San Sebastian

    elif option_table == 'San Sebastian':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_8'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Sebastian',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Sebastian',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Sebastian',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Sebastian',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Sebastian',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Sebastian',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Sebastian',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Sebastian',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis8'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='San Sebastian', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='San Sebastian', :],
                hide_index=True, use_container_width=True)
            

        
    ### Santa Rita:

    elif option_table == 'Santa Rita':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_9'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Santa Rita',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Santa Rita',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Santa Rita',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Santa Rita',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Santa Rita',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Santa Rita',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Santa Rita',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Santa Rita',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis9'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Santa Rita', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Santa Rita', :],
                hide_index=True, use_container_width=True)
            

        
    
    ### Villareal

    elif option_table == 'Villareal':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_10'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Villareal',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Villareal',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Villareal',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Villareal',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Villareal',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Villareal',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Villareal',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Villareal',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis10'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Villareal', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Villareal', :],
                hide_index=True, use_container_width=True)
            

    
    maternal_10_14['Year'] = maternal_10_14['Year'].astype(int)
    maternal_15_19['Year'] = maternal_15_19['Year'].astype(int)
    


    # Facet Grid
    with st.expander('Click to see summary chart'):
        option_maternal_10_19 = st.selectbox(
            'Please select birth attendant type:',
            ('Total', 'SBA', 'TBA', 'Others', 'Not Stated'),
            key='selectbox_4'
        )


        age_picker = st.radio(
            'Select age group:',
            ['10-14 Years', '15-19 Years'],
            horizontal=True
        )

        if age_picker == '10-14 Years':
            

            fig_maternal_10_14 = px.scatter(maternal_10_14, x='Year',
                                        y=option_maternal_10_19,
                                        color='LGU', facet_col='LGU', facet_col_wrap=2,
                                        facet_col_spacing=0.09, template='seaborn', height=1200,
                                        trendline='ols', trendline_color_override='black',
                                        title='Adolescent Birth (10-14 years) by Birth Attendant in Samar Sites (2012-2021)')

            fig_maternal_10_14.update_layout(showlegend=False)
            fig_maternal_10_14.update_traces(mode='lines')
            fig_maternal_10_14.update_xaxes(matches=None)
            fig_maternal_10_14.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
            fig_maternal_10_14.update_yaxes(matches=None)
            fig_maternal_10_14.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))

            st.plotly_chart(fig_maternal_10_14, use_container_width=True)

        

        elif age_picker == '15-19 Years':
            

            fig_maternal_15_19 = px.scatter(maternal_15_19, x='Year',
                                        y=option_maternal_10_19,
                                        color='LGU', facet_col='LGU', facet_col_wrap=2,
                                        facet_col_spacing=0.09, template='seaborn', height=1200,
                                        trendline='ols', trendline_color_override='black',
                                        title='Adolescent Birth (15-19 years) by Birth Attendant in Samar Sites (2012-2021)')

            fig_maternal_15_19.update_layout(showlegend=False)
            fig_maternal_15_19.update_traces(mode='lines')
            fig_maternal_15_19.update_xaxes(matches=None)
            fig_maternal_15_19.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
            fig_maternal_15_19.update_yaxes(matches=None)
            fig_maternal_15_19.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))

            st.plotly_chart(fig_maternal_15_19, use_container_width=True)



#############################
#############################
#############################
#############################
#############################
#############################
#############################
#############################
#############################
#############################



# By Place of Occurrence


occurrence_10_14 = ind2b.loc[ind2b['Age Range']=='10 to 14',
                                ['LGU',
                                'Year',
                                'Total',
                                'SBA',
                                'TBA',
                                'Others',
                                'Not Stated']]


occurrence_15_19 = ind2b.loc[ind2b['Age Range']=='15 to 19',
                                ['LGU',
                                'Year',
                                'Total',
                                'SBA',
                                'TBA',
                                'Others',
                                'Not Stated']]


with ind2_tab2:      
    
    # Show Table
    
    occurrence_10_14['Year'] = occurrence_10_14['Year'].astype(str)
    occurrence_15_19['Year'] = occurrence_15_19['Year'].astype(str)


    occurrence_10_14['Year'] = occurrence_10_14['Year'].astype(str)
    occurrence_10_14['SBA/Total'] = occurrence_10_14['SBA']/occurrence_10_14['Total']
    occurrence_10_14['TBA/Total'] = occurrence_10_14['TBA']/occurrence_10_14['Total']
    occurrence_10_14['Others/Total'] = occurrence_10_14['Others']/occurrence_10_14['Total']
    occurrence_10_14['NS/Total'] = occurrence_10_14['Not Stated']/occurrence_10_14['Total']
    occurrence_10_14 = occurrence_10_14.fillna(0)

    occurrence_15_19['Year'] = occurrence_15_19['Year'].astype(str)
    occurrence_15_19['SBA/Total'] = occurrence_15_19['SBA']/occurrence_15_19['Total']
    occurrence_15_19['TBA/Total'] = occurrence_15_19['TBA']/occurrence_15_19['Total']
    occurrence_15_19['Others/Total'] = occurrence_15_19['Others']/occurrence_15_19['Total']
    occurrence_15_19['NS/Total'] = occurrence_15_19['Not Stated']/occurrence_15_19['Total']
    occurrence_15_19 = occurrence_15_19.fillna(0)


    with st.expander('Please click to see the chart for the combined data of the 10 sites in this province'):
        occurrence_all = pd.read_excel(data_link, sheet_name='SBA Occurrence All')
        occurrence_10_14_all = occurrence_all.loc[occurrence_all['Age Range']=='10-14', :]
        occurrence_10_14_all['Year'] =  occurrence_10_14_all['Year'].astype(str)
        occurrence_10_14_all['SBA/Total'] =  occurrence_10_14_all['SBA']/ occurrence_10_14_all['Total']
        occurrence_10_14_all['TBA/Total'] =  occurrence_10_14_all['TBA']/ occurrence_10_14_all['Total']
        occurrence_10_14_all['Others/Total'] =  occurrence_10_14_all['Others']/ occurrence_10_14_all['Total']
        occurrence_10_14_all['NS/Total'] =  occurrence_10_14_all['Not Stated']/ occurrence_10_14_all['Total']
        occurrence_10_14_all =  occurrence_10_14_all.fillna(0)

        occurrence_15_19_all = occurrence_all.loc[occurrence_all['Age Range']=='15-19', :]
        occurrence_15_19_all['Year'] = occurrence_15_19_all['Year'].astype(str)
        occurrence_15_19_all['SBA/Total'] = occurrence_15_19_all['SBA']/occurrence_15_19_all['Total']
        occurrence_15_19_all['TBA/Total'] = occurrence_15_19_all['TBA']/occurrence_15_19_all['Total']
        occurrence_15_19_all['Others/Total'] = occurrence_15_19_all['Others']/occurrence_15_19_all['Total']
        occurrence_15_19_all['NS/Total'] = occurrence_15_19_all['Not Stated']/occurrence_15_19_all['Total']
        occurrence_15_19_all = occurrence_15_19_all.fillna(0)

        fig_graph2_10_14_all = px.scatter(occurrence_10_14_all, x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in Samar Sites (2012-2021)')
        
        fig_graph2_15_19_all = px.scatter(occurrence_15_19_all, x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in Samar Sites (2012-2021)')

        analyze = st.radio('Select Age Group:',
                           ['10-14 Years', '15-19 Years'],
                           horizontal=True, key='alt_1')
        if analyze == '10-14 Years':
            fig_graph2_10_14_all.update_traces(mode='lines')
            st.plotly_chart(fig_graph_10_14_all, use_container_width=True)
            st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
            results = px.get_trendline_results(fig_graph_10_14_all)
            st.write(results.px_fit_results.iloc[0].summary())
        
        elif analyze == '15-19 Years':
            fig_graph2_15_19_all.update_traces(mode='lines')
            st.plotly_chart(fig_graph_15_19_all, use_container_width=True)
            st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
            results = px.get_trendline_results(fig_graph_15_19_all)
            st.write(results.px_fit_results.iloc[0].summary())



    option_occurrence = st.selectbox(
        'Please select a City/Municipality',
        ('Basey', 'Calbayog', 'Calbiga', 'Catbalogan', 'Marabut',
            'Paranas', 'San Jose De Buan', 'San Sebastian', 'Santa Rita', 'Villareal'),
            key='selectbox_5'
    )

    

    ### Basey

    if option_occurrence == 'Basey':
                    
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_21'
        )

        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Basey',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Basey',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Basey',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Basey',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Basey',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Basey',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Basey',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Basey',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        


        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis11'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Basey', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Basey', :],
                hide_index=True, use_container_width=True)
            
            
    ### Calbayog

    elif option_occurrence == 'Calbayog':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_22'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbayog',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbayog',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbayog',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbayog',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbayog',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbayog',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbayog',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbayog',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis12'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbayog', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbayog', :],
                hide_index=True, use_container_width=True)
            

    
    ### Calbiga

    elif option_table == 'Calbiga':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_3'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbiga',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbiga',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbiga',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbiga',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbiga',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbiga',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbiga',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbiga',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis13'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Basey', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbiga', :],
                hide_index=True, use_container_width=True)



    ### Catbalogan

    elif option_table == 'Catbalogan':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_3'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Catbalogan',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Catbalogan',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Catbalogan',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Catbalogan',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Catbalogan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Catbalogan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Catbalogan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Catbalogan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis13'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Basey', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Catbalogan', :],
                hide_index=True, use_container_width=True)



    
    ### Marabut

    elif option_table == 'Marabut':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_5'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Marabut',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Marabut',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Marabut',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Marabut',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Marabut',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Marabut',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Marabut',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Marabut',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis14'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Marabut', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Marabut', :],
                hide_index=True, use_container_width=True)
            


    ### Paranas
        
    elif option_table == 'Paranas':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_6'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Paranas',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Paranas',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Paranas',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Paranas',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Paranas',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Paranas',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Paranas',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Paranas',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis15'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Paranas', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Paranas', :],
                hide_index=True, use_container_width=True)
            


    ### San Jose De Buan
        
    elif option_table == 'San Jose De Buan':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_7'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Jose De Buan',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Jose De Buan',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Jose De Buan',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Jose De Buan',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Jose De Buan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Jose De Buan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Jose De Buan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Jose De Buan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis16'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='San Jose De Buan', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='San Jose De Buan', :],
                hide_index=True, use_container_width=True)
        
    
    ### San Sebastian

    elif option_table == 'San Sebastian':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_8'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Sebastian',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Sebastian',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Sebastian',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Sebastian',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Sebastian',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Sebastian',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Sebastian',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Sebastian',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis17'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='San Sebastian', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='San Sebastian', :],
                hide_index=True, use_container_width=True)
            



    ### Santa Rita

    elif option_table == 'Santa Rita':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_8'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Santa Rita',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Santa Rita',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Santa Rita',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Santa Rita',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Santa Rita',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Santa Rita',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Santa Rita',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Santa Rita',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis18'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Santa Rita', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Santa Rita', :],
                hide_index=True, use_container_width=True)

    
    ### Villareal

    elif option_table == 'Villareal':
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_10'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Villareal',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Villareal',:], x='Year', y='SBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Villareal',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Villareal',:], x='Year', y='TBA/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Villareal',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Villareal',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Villareal',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Villareal',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
        with st.expander('Click to see trend analysis'):
                analysis = st.radio(
                'Trend Analysis - Select Age Group:',
                ['10-14 Years', '15-19 Years'], horizontal=True,
                key='analysis19'
                )
                
                if analysis == '10-14 Years':
                    st.markdown('###### Analysis of Birth (10-14 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Birth Attendant Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Villareal', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Villareal', :],
                hide_index=True, use_container_width=True)
            

        
    
    
    occurrence_10_14['Year'] = occurrence_10_14['Year'].astype(int)
    occurrence_15_19['Year'] = occurrence_15_19['Year'].astype(int)
    


    # Facet Grid
    with st.expander('Click to see summary chart'):
        option_occurrence_10_19 = st.selectbox(
            'Please select birth attendant type:',
            ('Total', 'SBA', 'TBA', 'Others', 'Not Stated'),
            key='selectbox_6'
        )


        age_picker_occ = st.radio(
            'Select age group:',
            ['10-14 Years', '15-19 Years'],
            horizontal=True, key='picker_1'
        )

        if age_picker_occ == '10-14 Years':


            fig_occurrence_10_14 = px.scatter(occurrence_10_14, x='Year',
                                        y=option_occurrence_10_19,
                                        color='LGU', facet_col='LGU', facet_col_wrap=2,
                                        facet_col_spacing=0.09, template='seaborn', height=1200,
                                        trendline='ols', trendline_color_override='black',
                                        title='Adolescent Birth (10-14 years) by Place of Occurrence in UN-KOICA Sites (2012-2021)')

                
            fig_occurrence_10_14.update_layout(showlegend=False)
            fig_occurrence_10_14.update_traces(mode='lines')
            fig_occurrence_10_14.update_xaxes(matches=None)
            fig_occurrence_10_14.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
            fig_occurrence_10_14.update_yaxes(matches=None)
            fig_occurrence_10_14.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))

            st.plotly_chart(fig_occurrence_10_14, use_container_width=True)
        


        elif age_picker_occ == '15-19 Years':


            fig_occurrence_15_19 = px.scatter(occurrence_15_19, x='Year',
                                        y=option_occurrence_10_19,
                                        color='LGU', facet_col='LGU', facet_col_wrap=2,
                                        facet_col_spacing=0.09, template='seaborn', height=1200,
                                        trendline='ols', trendline_color_override='black',
                                        title='Adolescent Birth (15_19 years) by Place of Occurrence in UN-KOICA Sites (2012-2021)')

                
            fig_occurrence_15_19.update_layout(showlegend=False)
            fig_occurrence_15_19.update_traces(mode='lines')
            fig_occurrence_15_19.update_xaxes(matches=None)
            fig_occurrence_15_19.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
            fig_occurrence_15_19.update_yaxes(matches=None)
            fig_occurrence_15_19.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))

            st.plotly_chart(fig_occurrence_15_19, use_container_width=True)




