import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


projected_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRuOM0mbpu6ThzB3HLRcKkXk3LCwE-0n-nAptaowFoNLQekgFX7FqU3IClSjl5rlX85bi-7REtyqEJt/pub?output=xlsx"
data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRp2M0ySSYySdadzJmA93oPOYsoF_0bH_dweGzqrtYn_xS3ugEtZQnIamGXuZIxxQP6TRqcuhcPrnSO/pub?output=xlsx"
ind2a = pd.read_excel(data_link, sheet_name=1)
ind2b = pd.read_excel(data_link, sheet_name=2)

st.title('UN-KOICA Sites in Region VIII: Secondary Data for Select Indicators in UN-KOICA Sites in Southern Leyte')


st.header('Indicator 2:')
st.subheader('Number of adolescent births attended by skilled health personnel among adolescents aged 10-19 in UN-KOICA Sites in Southern Leyte')





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
        maternal_all = pd.read_excel(data_link, sheet_name='SBA Maternal All')

        maternal_10_14_all = maternal_all.loc[maternal_all['Age Range']=='10 to 14', :]
       

        maternal_15_19_all = maternal_all.loc[maternal_all['Age Range']=='15 to 19', :]
       

        fig_graph_10_14_all = px.scatter(maternal_10_14_all, x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in Southern Leyte Sites (2012-2021)')
        
        fig_graph_15_19_all = px.scatter(maternal_15_19_all, x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in Southern Leyte Sites (2012-2021)')
        
        fig_graph_10_14_all.update_traces(mode='lines')
        fig_graph_15_19_all.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14_all, use_container_width=True)
        st.plotly_chart(fig_graph_15_19_all, use_container_width=True)




    option_table = st.selectbox(
        'Please select a City/Municipality',
        ('Bontoc', 'Libagon', 'Liloan', 'Limasawa', 'Maasin',
            'Macrohon', 'Malitbog', 'Padre Burgos', 'Sogod', 'Tomas Oppus'),
            key='selectbox_3'
    )

    
    if option_table == 'Bontoc':
                    
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_1'
        )

       
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Bontoc',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Bontoc',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Bontoc',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Bontoc',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_2'
        )
        
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Libagon',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Libagon',:], x='Year', y='Percent TBA', template='seaborn',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Libagon',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Libagon',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_3'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Liloan',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Liloan',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Liloan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Liloan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_4'
        )
        
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Limasawa',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Limasawa',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Limasawa',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Limasawa',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_5'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Maasin',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Maasin',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Maasin',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Maasin',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_6'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Macrohon',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Macrohon',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Macrohon',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Macrohon',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_7'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Malitbog',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Malitbog',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Malitbog',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Malitbog',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        


        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_8'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Padre Burgos',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Padre Burgos',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Padre Burgos',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Padre Burgos',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_9'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Sogod',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Sogod',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Sogod',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Sogod',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_10'
        )
        
        if graph == 'SBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_graph_10_14 = px.scatter(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_graph_15_19 = px.scatter(maternal_15_19.loc[maternal_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
        fig_graph_10_14.update_traces(mode='lines')
        fig_graph_15_19.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14, use_container_width=True)
        st.plotly_chart(fig_graph_15_19, use_container_width=True)

        

        
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
            'Please select birth attendant type:',
            ('Percent SBA', 'Percent TBA', 'Percent Others', 'Percent Not Stated'),
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
                                        title='Adolescent Birth (10-14 years) by Birth Attendant in Southern Leyte Sites (2012-2021)')

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
                                        title='Adolescent Birth (15-19 years) by Birth Attendant in Southern Leyte Sites (2012-2021)')

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
        occurrence_all = pd.read_excel(data_link, sheet_name='SBA Occurrence All')
        occurrence_10_14_all = occurrence_all.loc[occurrence_all['Age Range']=='10 to 14', :]

        occurrence_15_19_all = occurrence_all.loc[occurrence_all['Age Range']=='15 to 19', :]

        fig_graph2_10_14_all = px.scatter(occurrence_10_14_all, x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in Southern Leyte Sites (2012-2021)')
        
        fig_graph2_15_19_all = px.scatter(occurrence_15_19_all, x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in Southern Leyte Sites (2012-2021)')
        

        fig_graph2_10_14_all.update_traces(mode='lines')
        fig_graph2_15_19_all.update_traces(mode='lines')
        st.plotly_chart(fig_graph2_10_14_all, use_container_width=True)
        st.plotly_chart(fig_graph2_15_19_all, use_container_width=True)



    option_occurrence = st.selectbox(
        'Please select a City/Municipality',
        ('Bontoc', 'Libagon', 'Liloan', 'Limasawa', 'Maasin',
            'Macrohon', 'Malitbog', 'Padre Burgos', 'Sogod', 'Tomas Oppus'),
            key='selectbox_5'
    )

    

    ### Bontoc

    if option_occurrence == 'Bontoc':
                    
        graph = st.radio(
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_21'
        )

        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Bontoc',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Bontoc',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Bontoc',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Bontoc',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        


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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_22'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Libagon',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Libagon',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Libagon',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Libagon',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_3'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Liloan',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Liloan',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Liloan',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Liloan',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Liloan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Liloan',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Liloan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Liloan',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_3'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Limasawa',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Limasawa',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Limasawa',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Limasawa',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Limasawa',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Limasawa',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Limasawa',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Limasawa',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_5'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Maasin',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Maasin',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Maasin',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Maasin',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Maasin',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Maasin',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Maasin',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Maasin',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_6'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Macrohon',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Macrohon',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Macrohon',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Macrohon',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Macrohon',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Macrohon',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Macrohon',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Macrohon',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_7'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Malitbog',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Malitbog',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Malitbog',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Malitbog',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Malitbog',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Malitbog',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Malitbog',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Malitbog',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_8'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Padre Burgos',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Padre Burgos',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Padre Burgos',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Padre Burgos',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Padre Burgos',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Padre Burgos',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Padre Burgos',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Padre Burgos',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_8'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Sogod',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Sogod',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Sogod',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Sogod',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Sogod',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Sogod',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Sogod',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Sogod',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
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
            'Birth attendant type:',
            ['SBA', 'TBA', 'Others', 'Not Stated'],
            captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                        'Traditional Birth Attendants (i.e., hilot, manaram)',
                        'Neither SBA nor TBA',
                        'Not reported'], key='radio_10'
        )
        
        if graph == 'SBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'TBA':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Percent TBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Others':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Percent Others', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        elif graph == 'Not Stated':
            fig_occ_10_14 = px.scatter(occurrence_10_14.loc[occurrence_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
            fig_occ_15_19 = px.scatter(occurrence_15_19.loc[occurrence_15_19['LGU']=='Tomas Oppus',:], x='Year', y='Percent Not Stated', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_table))
        
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
            'Please select birth attendant type:',
            ('Percent SBA', 'Percent TBA', 'Percent Others', 'Percent Not Stated'),
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




