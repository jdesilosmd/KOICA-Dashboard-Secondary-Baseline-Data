import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Data Source
# sheet_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQDeIKjVIpn1FVfL6_APP_esmRpqisgz5k9d65CfBFJf7metRutyKrdZloWJyC50fXXpvHcgj2lBW6i/pub?output=xlsx"
projected_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRuOM0mbpu6ThzB3HLRcKkXk3LCwE-0n-nAptaowFoNLQekgFX7FqU3IClSjl5rlX85bi-7REtyqEJt/pub?output=xlsx"
data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRp2M0ySSYySdadzJmA93oPOYsoF_0bH_dweGzqrtYn_xS3ugEtZQnIamGXuZIxxQP6TRqcuhcPrnSO/pub?output=xlsx"

projected_10_14 = pd.read_excel(projected_link, '10-14 Women')
projected_15_19 = pd.read_excel(projected_link, '15-19 Women')
ind1 = pd.read_excel(data_link, sheet_name=0)
ind2a = pd.read_excel(data_link, sheet_name=1)
ind2b = pd.read_excel(data_link, sheet_name=2)


### DASHBOARD CODE STARTS HERE ###
# Title
st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Southern Leyte')

#Sidebar (containing the radio button for indicators)
st.sidebar.subheader('Select an Indicator:')
indicator = st.sidebar.radio(
    'Pick one (1) indicator below:',
    ['***Indicator 1***', '***Indicator 2***', '***Indicator 3***', '***Indicator 4***',
     '***Indicator 5***', '***Indicator 6***', '***Indicator 7***', '***Indicator 8***',
     '***Indicator 9***', '***Indicator 10***', '***Indicator 11***'],
    captions=['Adolescent Birth Rate',
              'Birth attended by a skilled birth attendant (SBA)',
              'Facility-based delivery',
              'mCPR',
              'Adolescents who have informed decisions on ASRH',
              'LGU budget on ASRH',
              'No. of Adolescent-Friendly Health Facilities (AFHF)',
              'No. of educators trained in Comprehensive Sexuality Education (CSE)',
              'No. of adolescents participated in Reproductive Health and Gender Equality campaign or education sessions',
              'No. of Performance Accountability System (PAS)-compliant LGUs',
              'No of LGUs with prevention initiatives on Child, early and forced marriage or Adolescent Pregnancy']
)

# Indicator 1 is selected
if indicator == '***Indicator 1***':

    tab1, tab2 = st.tabs(['10-14 years', '15-19 years'])

    with tab1:
        st.header('Indicator 1:')
        st.subheader('Adolescent Birth Rate (10-14 years of age)')

        
        ind1a = ind1.merge(projected_10_14, on='LGU')
        births_10_14 = ind1a.loc[:,
                                ['LGU',
                                 '2012_Births_Women_10-14',	
                                 '2013_Births_Women_10-14',
                                 '2014_Births_Women_10-14',
                                 '2015_Births_Women_10-14',
                                 '2016_Births_Women_10-14',
                                 '2017_Births_Women_10-14',
                                 '2018_Births_Women_10-14',
                                 '2019_Births_Women_10-14',
                                 '2020_Births_Women_10-14',
                                 '2021_Births_Women_10-14',
                                 'yr2012',
                                 'yr2013',
                                 'yr2014',
                                 'yr2015',
                                 'yr2016',
                                 'yr2017',
                                 'yr2018',
                                 'yr2019',
                                 'yr2020',
                                 'yr2021']]
        
              
        births_10_14['abr2012'] = births_10_14['2012_Births_Women_10-14']/births_10_14['yr2012']
        births_10_14['abr2013'] = births_10_14['2013_Births_Women_10-14']/births_10_14['yr2013']
        births_10_14['abr2014'] = births_10_14['2014_Births_Women_10-14']/births_10_14['yr2014']
        births_10_14['abr2015'] = births_10_14['2015_Births_Women_10-14']/births_10_14['yr2015']
        births_10_14['abr2016'] = births_10_14['2016_Births_Women_10-14']/births_10_14['yr2016']
        births_10_14['abr2017'] = births_10_14['2017_Births_Women_10-14']/births_10_14['yr2017']
        births_10_14['abr2018'] = births_10_14['2018_Births_Women_10-14']/births_10_14['yr2018']
        births_10_14['abr2019'] = births_10_14['2019_Births_Women_10-14']/births_10_14['yr2019']
        births_10_14['abr2020'] = births_10_14['2020_Births_Women_10-14']/births_10_14['yr2020']
        births_10_14['abr2021'] = births_10_14['2021_Births_Women_10-14']/births_10_14['yr2021']
        

        
        abr_10_14 = births_10_14.loc[:, ['LGU',
                                         'abr2012',
                                         'abr2013',
                                         'abr2014',
                                         'abr2015',
                                         'abr2016',
                                         'abr2017',
                                         'abr2018',
                                         'abr2019',
                                         'abr2020',
                                         'abr2020',
                                         'abr2021']]
        
        abr_10_14.rename(columns={
            'abr2012': '2012',
            'abr2013': '2013',
            'abr2014': '2014',
            'abr2015': '2015',
            'abr2016': '2016',
            'abr2017': '2017',
            'abr2018': '2018',
            'abr2019': '2019',
            'abr2020': '2020',
            'abr2021': '2021'
        }, inplace=True)


        abr_10_14_melt = abr_10_14.melt(id_vars='LGU', var_name='Year', value_name='ABR')

        option_abr_10_14_table = st.selectbox(
            'Please select a City/Municipality',
            ('Bontoc', 'Libagon', 'Liloan', 'Limasawa', 'Maasin',
             'Macrohon', 'Malitbog', 'Padre Burgos', 'Sogod', 'Tomas Oppus'),
             key='selectbox_1'
        )


# ABR 10-14 Chart per LGU
        
        if option_abr_10_14_table == 'Bontoc':
            
            fig_abr_10_14_lgu = px.line(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Bontoc',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
            st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
        
        
        elif option_abr_10_14_table == 'Libagon':
            fig_abr_10_14_lgu = px.line(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Libagon',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
            st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
        
        elif option_abr_10_14_table == 'Liloan':
            fig_abr_10_14_lgu = px.line(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Liloan',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
            st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)

        elif option_abr_10_14_table == 'Limasawa':
            fig_abr_10_14_lgu = px.line(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Limasawa',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
            st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
        
        elif option_abr_10_14_table == 'Maasin':
            fig_abr_10_14_lgu = px.line(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Maasin',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
            st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
        
        elif option_abr_10_14_table == 'Macrohon':
            fig_abr_10_14_lgu = px.line(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Macrohon',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
            st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
        
        elif option_abr_10_14_table == 'Malitbog':
            fig_abr_10_14_lgu = px.line(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Malitbog',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
            st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
        
        elif option_abr_10_14_table == 'Padre Burgos':
            fig_abr_10_14_lgu = px.line(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Padre Burgos',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
            st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
        
        elif option_abr_10_14_table == 'Sogod':
            fig_abr_10_14_lgu = px.line(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Sogod',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
            st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)
        
        elif option_abr_10_14_table == 'Tomas Oppus':
            fig_abr_10_14_lgu = px.line(abr_10_14_melt.loc[abr_10_14_melt['LGU']=='Tomas Oppus',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(option_abr_10_14_table))
            st.plotly_chart(fig_abr_10_14_lgu, use_container_width=True)


        

# Summary Chart for ABR (10-14)
        fig_abr_10_14 = px.line(abr_10_14_melt, x='Year', y='ABR',color='LGU', facet_col='LGU', facet_col_wrap=2,
                                facet_col_spacing=0.09, template='seaborn', height=1200,
                                title='Adolescent Birth Rate (10-14 years) in KOICA Sites (2012-2021)')
       

        fig_abr_10_14.update_layout(showlegend=False)

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
        
        ind1b = ind1.merge(projected_15_19, on='LGU')
        births_15_19 = ind1b.loc[:,
                                ['LGU',
                                 '2012_Births_Women_15-19',	
                                 '2013_Births_Women_15-19',
                                 '2014_Births_Women_15-19',
                                 '2015_Births_Women_15-19',
                                 '2016_Births_Women_15-19',
                                 '2017_Births_Women_15-19',
                                 '2018_Births_Women_15-19',
                                 '2019_Births_Women_15-19',
                                 '2020_Births_Women_15-19',
                                 '2021_Births_Women_15-19',
                                 'yr2012',
                                 'yr2013',
                                 'yr2014',
                                 'yr2015',
                                 'yr2016',
                                 'yr2017',
                                 'yr2018',
                                 'yr2019',
                                 'yr2020',
                                 'yr2021']]
        
              
        births_15_19['abr2012'] = births_15_19['2012_Births_Women_15-19']/births_15_19['yr2012']
        births_15_19['abr2013'] = births_15_19['2013_Births_Women_15-19']/births_15_19['yr2013']
        births_15_19['abr2014'] = births_15_19['2014_Births_Women_15-19']/births_15_19['yr2014']
        births_15_19['abr2015'] = births_15_19['2015_Births_Women_15-19']/births_15_19['yr2015']
        births_15_19['abr2016'] = births_15_19['2016_Births_Women_15-19']/births_15_19['yr2016']
        births_15_19['abr2017'] = births_15_19['2017_Births_Women_15-19']/births_15_19['yr2017']
        births_15_19['abr2018'] = births_15_19['2018_Births_Women_15-19']/births_15_19['yr2018']
        births_15_19['abr2019'] = births_15_19['2019_Births_Women_15-19']/births_15_19['yr2019']
        births_15_19['abr2020'] = births_15_19['2020_Births_Women_15-19']/births_15_19['yr2020']
        births_15_19['abr2021'] = births_15_19['2021_Births_Women_15-19']/births_15_19['yr2021']



        abr_15_19 = births_15_19.loc[:, ['LGU',
                                         'abr2012',
                                         'abr2013',
                                         'abr2014',
                                         'abr2015',
                                         'abr2016',
                                         'abr2017',
                                         'abr2018',
                                         'abr2019',
                                         'abr2020',
                                         'abr2020',
                                         'abr2021']]
        
        abr_15_19.rename(columns={
            'abr2012': '2012',
            'abr2013': '2013',
            'abr2014': '2014',
            'abr2015': '2015',
            'abr2016': '2016',
            'abr2017': '2017',
            'abr2018': '2018',
            'abr2019': '2019',
            'abr2020': '2020',
            'abr2021': '2021'
        }, inplace=True)
        
        
        abr_15_19_melt = abr_15_19.melt(id_vars='LGU', var_name='Year', value_name='ABR')


        option_abr_15_19_table = st.selectbox(
            'Please select a City/Municipality',
            ('Bontoc', 'Libagon', 'Liloan', 'Limasawa', 'Maasin',
             'Macrohon', 'Malitbog', 'Padre Burgos', 'Sogod', 'Tomas Oppus'),
             key='selectbox_2'
        )


# ABR 15-19 Chart per LGU
        
        if option_abr_15_19_table == 'Bontoc':
            
            fig_abr_15_19_lgu = px.line(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Bontoc',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
            st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
        
        
        elif option_abr_15_19_table == 'Libagon':
            fig_abr_15_19_lgu = px.line(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Libagon',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
            st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
        
        elif option_abr_15_19_table == 'Liloan':
            fig_abr_15_19_lgu = px.line(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Liloan',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
            st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)

        elif option_abr_15_19_table == 'Limasawa':
            fig_abr_15_19_lgu = px.line(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Limasawa',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
            st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
        
        elif option_abr_15_19_table == 'Maasin':
            fig_abr_15_19_lgu = px.line(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Maasin',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
            st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
        
        elif option_abr_15_19_table == 'Macrohon':
            fig_abr_15_19_lgu = px.line(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Macrohon',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
            st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
        
        elif option_abr_15_19_table == 'Malitbog':
            fig_abr_15_19_lgu = px.line(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Malitbog',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
            st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
        
        elif option_abr_15_19_table == 'Padre Burgos':
            fig_abr_15_19_lgu = px.line(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Padre Burgos',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
            st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
        
        elif option_abr_15_19_table == 'Sogod':
            fig_abr_15_19_lgu = px.line(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Sogod',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
            st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)
        
        elif option_abr_15_19_table == 'Tomas Oppus':
            fig_abr_15_19_lgu = px.line(abr_15_19_melt.loc[abr_15_19_melt['LGU']=='Tomas Oppus',:], x='Year', y='ABR', template='seaborn',
                                        title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(option_abr_15_19_table))
            st.plotly_chart(fig_abr_15_19_lgu, use_container_width=True)

        fig_abr_15_19 = px.line(abr_15_19_melt, x='Year', y='ABR',color='LGU', facet_col='LGU', facet_col_wrap=2,
                                facet_col_spacing=0.09, template='seaborn', height=1200,
                                title='Adolescent Birth Rate (15-19 years) in Southern Leyte Sites (2012-2021)')
        
        fig_abr_15_19.update_layout(showlegend=False)
        
        fig_abr_15_19.update_xaxes(matches=None)
        fig_abr_15_19.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
        fig_abr_15_19.update_yaxes(matches=None)
        fig_abr_15_19.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))


        with st.expander('Click to see data table'):
            st.markdown('###### Adolescent Birth Rate in KOICA Sites from 2012 to 2021')
            st.dataframe(abr_15_19_melt, use_container_width=True, hide_index=True)
        

        with st.expander('Click to see summary chart'):
            st.plotly_chart(fig_abr_15_19, use_container_width=True)

#####










#####

# Indicator 2 is selected

elif indicator == '***Indicator 2***':
    st.header('Indicator 2:')
    st.subheader('Number of adolescent births attended by skilled health personnel among adolescents aged 10-19 in Southern Leyte project sites')

    ind2_tab1, ind2_tab2 = st.tabs(["By Mother's Residence",
                                    'By Place of Occurrence'])


# By Mother's Residence
    
    with ind2_tab1:      
        maternal_10_14 = ind2a.loc[ind2a['Age Range']=='10 to 14',
                                       ['LGU',
                                        'Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']]
        
        # Show Table

        maternal_10_14['Year'] = maternal_10_14['Year'].astype(str)

        option_maternal_10_14_table = st.selectbox(
            'Please select a City/Municipality',
            ('Bontoc', 'Libagon', 'Liloan', 'Limasawa', 'Maasin',
             'Macrohon', 'Malitbog', 'Padre Burgos', 'Sogod', 'Tomas Oppus'),
             key='selectbox_3'
        )

        
        if option_maternal_10_14_table == 'Bontoc':
                        
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_1'
            )

            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Bontoc',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                


        elif option_maternal_10_14_table == 'Libagon':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_2'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Libagon',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

        
        elif option_maternal_10_14_table == 'Liloan':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_3'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

        
        elif option_maternal_10_14_table == 'Limasawa':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_4'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

        
        elif option_maternal_10_14_table == 'Maasin':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_5'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

            
        elif option_maternal_10_14_table == 'Macrohon':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_6'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

            
        elif option_maternal_10_14_table == 'Malitbog':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_7'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

            
        
        elif option_maternal_10_14_table == 'Padre Burgos':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_8'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

            
        
        elif option_maternal_10_14_table == 'Sogod':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_9'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

            
        
        elif option_maternal_10_14_table == 'Tomas Oppus':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_10'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

        
        maternal_10_14['Year'] = maternal_10_14['Year'].astype('int')
        


        # Facet Grid
        with st.expander('Click to see summary chart'):
            option_maternal_10_14 = st.selectbox(
                'Please select birth attendant type:',
                ('Total', 'SBA', 'TBA', 'Others', 'Not Stated'),
                key='selectbox_4'
            )

            fig_maternal_10_14 = px.line(maternal_10_14, x='Year',
                                        y=option_maternal_10_14,
                                        color='LGU', facet_col='LGU', facet_col_wrap=2,
                                        facet_col_spacing=0.09, template='seaborn', height=1200,
                                        title='Adolescent Birth (10-14 years) by Birth Attendant in Southern Leyte Sites (2012-2021)')

            fig_maternal_10_14.update_layout(showlegend=False)
            fig_maternal_10_14.update_xaxes(matches=None)
            fig_maternal_10_14.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
            fig_maternal_10_14.update_yaxes(matches=None)
            fig_maternal_10_14.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))

            st.plotly_chart(fig_maternal_10_14, use_container_width=True)







# By Place of Occurrence


    with ind2_tab2:      
        occurrence_10_14 = ind2b.loc[ind2a['Age Range']=='10 to 14',
                                       ['LGU',
                                        'Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']]
        
        # Show Table

        occurrence_10_14['Year'] = occurrence_10_14['Year'].astype(str)

        option_occurrence_10_14_table = st.selectbox(
            'Please select a City/Municipality',
            ('Bontoc', 'Libagon', 'Liloan', 'Limasawa', 'Maasin',
             'Macrohon', 'Malitbog', 'Padre Burgos', 'Sogod', 'Tomas Oppus'),
             key='selectbox_5'
        )

        
        if option_occurrence_10_14_table == 'Bontoc':
                        
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_21'
            )

            if graph == 'Total':
                fig_graph = px.line(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_occurrence_10_14_table))
                st.dataframe(
                    occurrence_10_14.loc[occurrence_10_14['LGU']=='Bontoc',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                


        elif option_occurrence_10_14_table == 'Libagon':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_22'
            )
           
            if graph == 'Total':
                fig_graph = px.line(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_occurrence_10_14_table))
                st.dataframe(
                    occurrence_10_14.loc[occurrence_10_14['LGU']=='Libagon',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

        
        elif option_maternal_10_14_table == 'Liloan':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_3'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Liloan',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

        
        elif option_maternal_10_14_table == 'Limasawa':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_4'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Limasawa',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

        
        elif option_maternal_10_14_table == 'Maasin':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_5'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Maasin',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

            
        elif option_maternal_10_14_table == 'Macrohon':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_6'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Macrohon',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

            
        elif option_maternal_10_14_table == 'Malitbog':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_7'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Malitbog',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

            
        
        elif option_maternal_10_14_table == 'Padre Burgos':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_8'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Padre Burgos',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

            
        
        elif option_maternal_10_14_table == 'Sogod':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_9'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Sogod',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

            
        
        elif option_maternal_10_14_table == 'Tomas Oppus':
            graph = st.radio(
                'Birth attendant type:',
                ['Total', 'SBA', 'TBA', 'Others', 'Not Stated'],
                captions=['All birth attendants',
                          'Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                          'Traditional Birth Attendants (i.e., hilot, manaram)',
                          'Neither SBA nor TBA',
                          'Not reported'], key='radio_10'
            )
           
            if graph == 'Total':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Total', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'SBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='SBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'TBA':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='TBA', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Others':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Others', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            elif graph == 'Not Stated':
                fig_graph = px.line(maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',:], x='Year', y='Not Stated', template='seaborn',
                        title='Adolescent Birth (10-14 years) by Birth Attendant in {} (2012-2021)'.format(option_maternal_10_14_table))
            st.plotly_chart(fig_graph, use_container_width=True)

            
            with st.expander('Click to see data table'):

                st.markdown('###### City/ Municipality = {}'.format(option_maternal_10_14_table))
                st.dataframe(
                    maternal_10_14.loc[maternal_10_14['LGU']=='Tomas Oppus',
                                    ['Year',
                                        'Total',
                                        'SBA',
                                        'TBA',
                                        'Others',
                                        'Not Stated']], hide_index=True)
                

            
        
        
        maternal_10_14['Year'] = maternal_10_14['Year'].astype('int')
        


        # Facet Grid
        with st.expander('Click to see summary chart'):
            option_occurrence_10_14 = st.selectbox(
                'Please select birth attendant type:',
                ('Total', 'SBA', 'TBA', 'Others', 'Not Stated'),
                key='selectbox_6'
            )

            fig_occurrence_10_14 = px.line(occurrence_10_14, x='Year',
                                        y=option_occurrence_10_14,
                                        color='LGU', facet_col='LGU', facet_col_wrap=2,
                                        facet_col_spacing=0.09, template='seaborn', height=1200,
                                        title='Adolescent Birth (10-14 years) by Birth Attendant in KOICA Sites (2012-2021)')

            fig_maternal_10_14.update_layout(showlegend=False)
            fig_maternal_10_14.update_xaxes(matches=None)
            fig_maternal_10_14.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
            fig_maternal_10_14.update_yaxes(matches=None)
            fig_maternal_10_14.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))

            st.plotly_chart(fig_occurrence_10_14, use_container_width=True)












elif indicator == '***Indicator 3***':
    st.write('Under Construction')
elif indicator == '***Indicator 4***':
    st.write('Under Construction')
elif indicator == '***Indicator 5***':
    st.write('Under Construction')
elif indicator == '***Indicator 6***':
    st.write('Under Construction')
elif indicator == '***Indicator 7***':
    st.write('Under Construction')
elif indicator == '***Indicator 8***':
    st.write('Under Construction')
elif indicator == '***Indicator 9***':
    st.write('Under Construction')
elif indicator == '***Indicator 10***':
    st.write('Under Construction')
elif indicator == '***Indicator 11***':
    st.write('Under Construction')
