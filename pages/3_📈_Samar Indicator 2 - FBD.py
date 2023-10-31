import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwKvqsNtKWqBgIwhVv6TDzCJMMwpr4uvBR9hdkb57qHsnFtIsJI3l2kFs1oIa2LhsQePTGtYjLIj4U/pub?output=xlsx"
ind2a = pd.read_excel(data_link, sheet_name=3)
ind2b = pd.read_excel(data_link, sheet_name=4)

st.title('UN-KOICA Sites in Region VIII: Secondary Data for Select Indicators in UN-KOICA Sites in Samar')


st.header('Indicator 2:')
st.subheader('Number of adolescent births done in a health facility among adolescents aged 10-19 in UN-KOICA Sites in Samar')





ind2_tab1, ind2_tab2 = st.tabs(["By Mother's Residence",
                                'By Place of Occurrence'])


maternal_10_14 = ind2a.loc[ind2a['Age Range']=='10 to 14',:]


maternal_15_19 = ind2a.loc[ind2a['Age Range']=='15 to 19',:]


# By Mother's Residence

with ind2_tab1:      
        
    # Show Table


    maternal_10_14['Year'] = maternal_10_14['Year'].astype(str)


    maternal_15_19['Year'] = maternal_15_19['Year'].astype(str)

    maternal_15_19 = maternal_15_19.fillna(0)


    with st.expander('Please click to see the chart for the combined data of the 10 sites in this province'):
        maternal_all = pd.read_excel(data_link, sheet_name='FBD Maternal All')

        maternal_10_14_all = maternal_all.loc[maternal_all['Age Range']=='10 to 14', :]
       

        maternal_15_19_all = maternal_all.loc[maternal_all['Age Range']=='15 to 19', :]
       

        fig_graph_10_14_all = px.scatter(maternal_10_14_all, x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in Samar Sites (2013-2021)')
        
        fig_graph_15_19_all = px.scatter(maternal_15_19_all, x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in Samar Sites (2013-2021)')
        
        fig_graph_10_14_all.update_traces(mode='lines')
        fig_graph_15_19_all.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14_all, use_container_width=True)
        st.plotly_chart(fig_graph_15_19_all, use_container_width=True)




    option_table = st.selectbox(
        'Please select a City/Municipality',
        ('Basey', 'Calbayog', 'Calbiga', 'Catbalogan', 'Marabut',
            'Paranas', 'San Jose De Buan', 'San Sebastian', 'Santa Rita', 'Villareal'),
            key='selectbox_3'
    )

    
    if option_table == 'Basey':
                    
        graph = st.radio(
            'Birth attendant type:',
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_1'
        )

       
        if graph == 'Health Facility':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Basey',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Basey',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Basey',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Basey',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Basey',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Basey',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Basey',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Basey',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_2'
        )
        
        
        if graph == 'Health Facility':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbayog',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbayog',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbayog',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbayog',:], x='Year', y='Percent Home', template='seaborn',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbayog',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbayog',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbayog',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbayog',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_3'
        )
        
        if graph == 'Health Facility':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbiga',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbiga',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbiga',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbiga',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbiga',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbiga',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Calbiga',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Calbiga',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_4'
        )
        
        
        if graph == 'Health Facility':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Catbalogan',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Catbalogan',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Catbalogan',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Catbalogan',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Catbalogan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Catbalogan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Catbalogan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Catbalogan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_5'
        )
        
        if graph == 'Health Facility':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Marabut',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Marabut',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Marabut',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Marabut',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Marabut',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Marabut',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Marabut',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Marabut',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_6'
        )
        
        if graph == 'Health Facility':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Paranas',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Paranas',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Paranas',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Paranas',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Paranas',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Paranas',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Paranas',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Paranas',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_7'
        )
        
        if graph == 'Health Facility':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Jose De Buan',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Jose De Buan',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Jose De Buan',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Jose De Buan',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Jose De Buan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Jose De Buan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Jose De Buan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Jose De Buan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        


        
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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_8'
        )
        
        if graph == 'Health Facility':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Sebastian',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Sebastian',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Sebastian',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Sebastian',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Sebastian',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Sebastian',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='San Sebastian',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='San Sebastian',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_9'
        )
        
        if graph == 'Health Facility':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Santa Rita',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Santa Rita',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Santa Rita',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Santa Rita',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Santa Rita',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Santa Rita',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Santa Rita',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Santa Rita',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_10'
        )
        
        if graph == 'Health Facility':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Villareal',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Villareal',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Villareal',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Villareal',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Villareal',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Villareal',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Villareal',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Villareal',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            ('Percent Health Facility', 'Percent Home', 'Percent Others', 'Percent Not Stated'),
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
                                        title='Adolescent Birth (10-14 years) by Birthing Location in Samar Sites (2013-2021)')

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
                                        title='Adolescent Birth (15-19 years) by Birthing Location in Samar Sites (2013-2021)')

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


occurrence_10_14 = ind2b.loc[ind2b['Age Range']=='10 to 14', :]


occurrence_15_19 = ind2b.loc[ind2b['Age Range']=='15 to 19', :]


with ind2_tab2:      
    
    # Show Table
    
    occurrence_10_14['Year'] = occurrence_10_14['Year'].astype(str)
    occurrence_15_19['Year'] = occurrence_15_19['Year'].astype(str)




    with st.expander('Please click to see the chart for the combined data of the 10 sites in this province'):
        occurrence_all = pd.read_excel(data_link, sheet_name='FBD Occurrence All')
        occurrence_10_14_all = occurrence_all.loc[occurrence_all['Age Range']=='10 to 14', :]

        occurrence_15_19_all = occurrence_all.loc[occurrence_all['Age Range']=='15 to 19', :]

        fig_graph2_10_14_all = px.scatter(occurrence_10_14_all, x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in Samar Sites (2013-2021)')
        
        fig_graph2_15_19_all = px.scatter(occurrence_15_19_all, x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birthing Location in Samar Sites (2013-2021)')
        

        fig_graph2_10_14_all.update_traces(mode='lines')
        fig_graph2_15_19_all.update_traces(mode='lines')
        st.plotly_chart(fig_graph2_10_14_all, use_container_width=True)
        st.plotly_chart(fig_graph2_15_19_all, use_container_width=True)



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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_21'
        )

        if graph == 'Health Facility':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Basey',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Basey',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Basey',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Basey',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Basey',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Basey',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Basey',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Basey',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        


        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        




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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_22'
        )
        
        if graph == 'Health Facility':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbayog',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbayog',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbayog',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbayog',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbayog',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbayog',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbayog',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbayog',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        



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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_3'
        )
        
        if graph == 'Health Facility':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbiga',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbiga',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbiga',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbiga',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbiga',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbiga',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Calbiga',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Calbiga',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        



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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_3'
        )
        
        if graph == 'Health Facility':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Catbalogan',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Catbalogan',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Catbalogan',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Catbalogan',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Catbalogan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Catbalogan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Catbalogan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Catbalogan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        



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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_5'
        )
        
        if graph == 'Health Facility':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Marabut',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Marabut',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Marabut',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Marabut',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Marabut',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Marabut',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Marabut',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Marabut',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        



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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_6'
        )
        
        if graph == 'Health Facility':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Paranas',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Paranas',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Paranas',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Paranas',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Paranas',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Paranas',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Paranas',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Paranas',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)




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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_7'
        )
        
        if graph == 'Health Facility':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Jose De Buan',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Jose De Buan',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Jose De Buan',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Jose De Buan',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Jose De Buan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Jose De Buan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Jose De Buan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Jose De Buan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        



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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_8'
        )
        
        if graph == 'Health Facility':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Sebastian',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Sebastian',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Sebastian',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Sebastian',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Sebastian',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Sebastian',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='San Sebastian',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='San Sebastian',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        

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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_8'
        )
        
        if graph == 'Health Facility':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Santa Rita',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Santa Rita',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Santa Rita',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Santa Rita',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Santa Rita',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Santa Rita',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Santa Rita',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Santa Rita',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
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
            ['Health Facility', 'Home', 'Others', 'Not Stated'],
             key='radio_10'
        )
        
        if graph == 'Health Facility':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Villareal',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Villareal',:], x='Year', y='Percent Health Facility', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Home':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Villareal',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Villareal',:], x='Year', y='Percent Home', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Villareal',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Villareal',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Villareal',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Villareal',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birthing Location in {} (2013-2021)'.format(option_table))
        
        fig_occ_10_14.update_traces(mode='lines')
        fig_occ_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_occ_10_14, use_container_width=True)
        st.plotly_chart(fig_occ_15_19, use_container_width=True)

        
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
            ('Percent Health Facility', 'Percent Home', 'Percent Others', 'Percent Not Stated'),
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
                                        title='Adolescent Birth (10-14 years) by Place of Occurrence in UN-KOICA Sites (2013-2021)')

                
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
                                        title='Adolescent Birth (15_19 years) by Place of Occurrence in UN-KOICA Sites (2013-2021)')

                
            fig_occurrence_15_19.update_layout(showlegend=False)
            fig_occurrence_15_19.update_traces(mode='lines')
            fig_occurrence_15_19.update_xaxes(matches=None)
            fig_occurrence_15_19.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
            fig_occurrence_15_19.update_yaxes(matches=None)
            fig_occurrence_15_19.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))

            st.plotly_chart(fig_occurrence_15_19, use_container_width=True)




