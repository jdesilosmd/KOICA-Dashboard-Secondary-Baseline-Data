import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRp2M0ySSYySdadzJmA93oPOYsoF_0bH_dweGzqrtYn_xS3ugEtZQnIamGXuZIxxQP6TRqcuhcPrnSO/pub?output=xlsx"
ind2a = pd.read_excel(data_link, sheet_name=3)
ind2b = pd.read_excel(data_link, sheet_name=4)

st.title('UN-KOICA Sites in Region VIII: Secondary Data for Select Indicators in UN-KOICA Sites in Southern Leyte')


st.header('Indicator 2:')
st.subheader('Number of births done in health facilities among adolescents aged 10-19 in UN-KOICA Sites in Southern Leyte')





ind2_tab1, ind2_tab2 = st.tabs(["By Mother's Residence",
                                'By Place of Occurrence'])


maternal_10_14 = ind2a.loc[ind2a['Age Range']=='10 to 14',
                           ['LGU',
                            'Year',
                            'Total',
                            'Health Facilities',
                            'Home',
                            'Others',
                            'Not Stated']]


maternal_15_19 = ind2a.loc[ind2a['Age Range']=='15 to 19',
                           ['LGU',
                            'Year',
                            'Total',
                            'Health Facilities',
                            'Home',
                            'Others',
                            'Not Stated']]


# By Mother's Residence

with ind2_tab1:      
        
    # Show Table


    maternal_10_14['Year'] = maternal_10_14['Year'].astype(str)
    maternal_10_14['Health Facilities/Total'] = maternal_10_14['Health Facilities']/maternal_10_14['Total']
    maternal_10_14['Home/Total'] = maternal_10_14['Home']/maternal_10_14['Total']
    maternal_10_14['Others/Total'] = maternal_10_14['Others']/maternal_10_14['Total']
    maternal_10_14['NS/Total'] = maternal_10_14['Not Stated']/maternal_10_14['Total']
    maternal_10_14 = maternal_10_14.fillna(0)


    maternal_15_19['Year'] = maternal_15_19['Year'].astype(str)
    maternal_15_19['Health Facilities/Total'] = maternal_15_19['Health Facilities']/maternal_15_19['Total']
    maternal_15_19['Home/Total'] = maternal_15_19['Home']/maternal_15_19['Total']
    maternal_15_19['Others/Total'] = maternal_15_19['Others']/maternal_15_19['Total']
    maternal_15_19['NS/Total'] = maternal_15_19['Not Stated']/maternal_15_19['Total']
    maternal_15_19 = maternal_15_19.fillna(0)


    option_table = st.selectbox(
        'Please select a City/Municipality',
        ('Bontoc', 'Libagon', 'Liloan', 'Limasawa', 'Maasin',
            'Macrohon', 'Malitbog', 'Padre Burgos', 'Sogod', 'Tomas Oppus'),
            key='selectbox_3'
    )

    
    if option_table == 'Bontoc':
                    
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_1'
        )

       
        if graph == 'Health Facilities':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Bontoc',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Bontoc',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Bontoc',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Bontoc',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())


        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Bontoc', :],
                hide_index=True, use_container_width=True)

            
    ### Libagon

    elif option_table == 'Libagon':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_2'
        )
        
        
        if graph == 'Health Facilities':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Libagon',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Libagon',:], x='Year', y='Home/Total', template='seaborn',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Libagon',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Libagon',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Libagon', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Libagon', :],
                hide_index=True, use_container_width=True)
            

    ### Liloan
        
    elif option_table == 'Liloan':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_3'
        )
        
        if graph == 'Health Facilities':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Liloan',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Liloan',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Liloan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Liloan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Liloan', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Liloan', :],
                hide_index=True, use_container_width=True)
            

    
    ### Limasawa

    elif option_table == 'Limasawa':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_4'
        )
        
        
        if graph == 'Health Facilities':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Limasawa',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Limasawa',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Limasawa',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Limasawa',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Limasawa', :],
                hide_index=True, use_container_width=True)
            

    
    ### Maasin

    elif option_table == 'Maasin':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_5'
        )
        
        if graph == 'Health Facilities':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Maasin',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Maasin',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Maasin',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Maasin',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Maasin', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Maasin', :],
                hide_index=True, use_container_width=True)
            

        
    ### Macrohon

    elif option_table == 'Macrohon':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_6'
        )
        
        if graph == 'Health Facilities':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Macrohon',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Macrohon',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Macrohon',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Macrohon',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Macrohon', :],
                hide_index=True, use_container_width=True)
            


    ### Malitbog
        
    elif option_table == 'Malitbog':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_7'
        )
        
        if graph == 'Health Facilities':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Malitbog',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Malitbog',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Malitbog',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Malitbog',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Malitbog', :],
                hide_index=True, use_container_width=True)
            

        
    ### Padre Burgos

    elif option_table == 'Padre Burgos':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_8'
        )
        
        if graph == 'Health Facilities':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Padre Burgos',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Padre Burgos',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Padre Burgos',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Padre Burgos',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Padre Burgos', :],
                hide_index=True, use_container_width=True)
            

        
    ### Sogod:

    elif option_table == 'Sogod':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_9'
        )
        
        if graph == 'Health Facilities':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Sogod',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Sogod',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Sogod',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Sogod',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Sogod', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Sogod', :],
                hide_index=True, use_container_width=True)
            

        
    
    ### Tomas Oppus

    elif option_table == 'Tomas Oppus':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_10'
        )
        
        if graph == 'Health Facilities':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Tomas Oppus',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_graph_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())

        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_table))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                maternal_15_19.loc[maternal_15_19['LGU']=='Tomas Oppus', :],
                hide_index=True, use_container_width=True)
            

    
    maternal_10_14['Year'] = maternal_10_14['Year'].astype(int)
    maternal_15_19['Year'] = maternal_15_19['Year'].astype(int)
    


    # Facet Grid
    with st.expander('Click to see summary chart'):
        option_maternal_10_19 = st.selectbox(
            'Please select Location of Birth type:',
            ('Total', 'Health Facilities', 'Home', 'Others', 'Not Stated'),
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
                                        title='Adolescent Birth (10-14 years) by Location of Birth in Southern Leyte Sites (2012-2021)')

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
                                        title='Adolescent Birth (15-19 years) by Location of Birth in Southern Leyte Sites (2012-2021)')

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
                                'Health Facilities',
                                'Home',
                                'Others',
                                'Not Stated']]


occurrence_15_19 = ind2b.loc[ind2b['Age Range']=='15 to 19',
                                ['LGU',
                                'Year',
                                'Total',
                                'Health Facilities',
                                'Home',
                                'Others',
                                'Not Stated']]


with ind2_tab2:      
    
    # Show Table
    
    occurrence_10_14['Year'] = occurrence_10_14['Year'].astype(str)
    occurrence_15_19['Year'] = occurrence_15_19['Year'].astype(str)


    occurrence_10_14['Year'] = occurrence_10_14['Year'].astype(str)
    occurrence_10_14['Health Facilities/Total'] = occurrence_10_14['Health Facilities']/occurrence_10_14['Total']
    occurrence_10_14['Home/Total'] = occurrence_10_14['Home']/occurrence_10_14['Total']
    occurrence_10_14['Others/Total'] = occurrence_10_14['Others']/occurrence_10_14['Total']
    occurrence_10_14['NS/Total'] = occurrence_10_14['Not Stated']/occurrence_10_14['Total']
    occurrence_10_14 = occurrence_10_14.fillna(0)

    occurrence_15_19['Year'] = occurrence_15_19['Year'].astype(str)
    occurrence_15_19['Health Facilities/Total'] = occurrence_15_19['Health Facilities']/occurrence_15_19['Total']
    occurrence_15_19['Home/Total'] = occurrence_15_19['Home']/occurrence_15_19['Total']
    occurrence_15_19['Others/Total'] = occurrence_15_19['Others']/occurrence_15_19['Total']
    occurrence_15_19['NS/Total'] = occurrence_15_19['Not Stated']/occurrence_15_19['Total']
    occurrence_15_19 = occurrence_15_19.fillna(0)



    option_occurrence = st.selectbox(
        'Please select a City/Municipality',
        ('Bontoc', 'Libagon', 'Liloan', 'Limasawa', 'Maasin',
            'Macrohon', 'Malitbog', 'Padre Burgos', 'Sogod', 'Tomas Oppus'),
            key='selectbox_5'
    )

    

    ### Bontoc

    if option_occurrence == 'Bontoc':
                    
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_21'
        )

        if graph == 'Health Facilities':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Bontoc',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Bontoc',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Bontoc',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Bontoc',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        


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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Bontoc', :],
                hide_index=True, use_container_width=True)
            
            
    ### Libagon

    elif option_occurrence == 'Libagon':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_22'
        )
        
        if graph == 'Health Facilities':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Libagon',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Libagon',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Libagon',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Libagon',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Libagon', :],
                hide_index=True, use_container_width=True)
            

    
    ### Liloan

    elif option_table == 'Liloan':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_3'
        )
        
        if graph == 'Health Facilities':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Liloan',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Liloan',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Liloan',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Liloan',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Liloan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Liloan',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Liloan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Liloan',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Liloan', :],
                hide_index=True, use_container_width=True)



    ### Limasawa

    elif option_table == 'Limasawa':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_3'
        )
        
        if graph == 'Health Facilities':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Limasawa',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Limasawa',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Limasawa',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Limasawa',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Limasawa',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Limasawa',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Limasawa',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Limasawa',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Limasawa', :],
                hide_index=True, use_container_width=True)



    
    ### Maasin

    elif option_table == 'Maasin':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_5'
        )
        
        if graph == 'Health Facilities':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Maasin',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Maasin',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Maasin',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Maasin',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Maasin',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Maasin',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Maasin',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Maasin',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Maasin', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Maasin', :],
                hide_index=True, use_container_width=True)
            


    ### Macrohon
        
    elif option_table == 'Macrohon':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_6'
        )
        
        if graph == 'Health Facilities':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Macrohon',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Macrohon',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Macrohon',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Macrohon',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Macrohon',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Macrohon',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Macrohon',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Macrohon',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Macrohon', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Macrohon', :],
                hide_index=True, use_container_width=True)
            


    ### Malitbog
        
    elif option_table == 'Malitbog':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_7'
        )
        
        if graph == 'Health Facilities':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Malitbog',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Malitbog',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Malitbog',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Malitbog',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Malitbog',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Malitbog',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Malitbog',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Malitbog',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Malitbog', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Malitbog', :],
                hide_index=True, use_container_width=True)
        
    
    ### Padre Burgos

    elif option_table == 'Padre Burgos':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_8'
        )
        
        if graph == 'Health Facilities':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Padre Burgos',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Padre Burgos',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Padre Burgos',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Padre Burgos',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Padre Burgos',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Padre Burgos',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Padre Burgos',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Padre Burgos',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Padre Burgos', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Padre Burgos', :],
                hide_index=True, use_container_width=True)
            



    ### Sogod

    elif option_table == 'Sogod':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_8'
        )
        
        if graph == 'Health Facilities':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Sogod',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Sogod',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Sogod',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Sogod',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Sogod',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Sogod',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Sogod',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Sogod',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Sogod', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Sogod', :],
                hide_index=True, use_container_width=True)

    
    ### Tomas Oppus

    elif option_table == 'Tomas Oppus':
        graph = st.radio(
            'Location of Birth type:',
            ['Health Facilities', 'Home', 'Others', 'Not Stated'],
            captions=['Health Facility (i.e., hospitals, lying-in clinics, etc.)',
                        'Home Deliveries',
                        'Neither Health Facilities nor Home',
                        'Not reported'], key='radio_10'
        )
        
        if graph == 'Health Facilities':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Health Facilities/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Home/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Others/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Tomas Oppus',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Tomas Oppus',:], x='Year', y='NS/Total', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Location of Birth in {} (2012-2021)'.format(option_table))
        
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
                    st.markdown('###### Analysis of Birth (10-14 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_10_14)
                    st.write(results.px_fit_results.iloc[0].summary())
                
                
                elif analysis == '15-19 Years':
                    st.markdown('###### Analysis of Birth (15-19 years) by Location of Birth Trend using Ordinary Least Squares (OLS):')
                    results = px.get_trendline_results(fig_occ_15_19)
                    st.write(results.px_fit_results.iloc[0].summary())



        st.markdown('######')
        
        with st.expander('Click to see data table'):

            st.markdown('###### City/ Municipality = {}'.format(option_occurrence))
            st.markdown('###### Age = 10-14')
            st.markdown('######')
            st.dataframe(
                occurrence_10_14.loc[occurrence_10_14['LGU']=='Tomas Oppus', :],
                hide_index=True, use_container_width=True)
            st.markdown('###### Age = 15-19')
            st.markdown('######')
            st.dataframe(
                occurrence_15_19.loc[occurrence_15_19['LGU']=='Tomas Oppus', :],
                hide_index=True, use_container_width=True)
            

        
    
    
    occurrence_10_14['Year'] = occurrence_10_14['Year'].astype(int)
    occurrence_15_19['Year'] = occurrence_15_19['Year'].astype(int)
    


    # Facet Grid
    with st.expander('Click to see summary chart'):
        option_occurrence_10_19 = st.selectbox(
            'Please select Location of Birth type:',
            ('Total', 'Health Facilities', 'Home', 'Others', 'Not Stated'),
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
