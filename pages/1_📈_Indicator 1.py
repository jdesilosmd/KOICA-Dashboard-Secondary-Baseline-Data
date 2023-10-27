import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


projected_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRuOM0mbpu6ThzB3HLRcKkXk3LCwE-0n-nAptaowFoNLQekgFX7FqU3IClSjl5rlX85bi-7REtyqEJt/pub?output=xlsx"
data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRp2M0ySSYySdadzJmA93oPOYsoF_0bH_dweGzqrtYn_xS3ugEtZQnIamGXuZIxxQP6TRqcuhcPrnSO/pub?output=xlsx"

projected_10_14 = pd.read_excel(projected_link, '10-14 Women')
projected_15_19 = pd.read_excel(projected_link, '15-19 Women')
ind1 = pd.read_excel(data_link, sheet_name=0)

st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Southern Leyte')


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
    
            
    births_10_14['abr2012'] = (births_10_14['2012_Births_Women_10-14']/births_10_14['yr2012'])*1000
    births_10_14['abr2013'] = (births_10_14['2013_Births_Women_10-14']/births_10_14['yr2013'])*1000
    births_10_14['abr2014'] = (births_10_14['2014_Births_Women_10-14']/births_10_14['yr2014'])*1000
    births_10_14['abr2015'] = (births_10_14['2015_Births_Women_10-14']/births_10_14['yr2015'])*1000
    births_10_14['abr2016'] = (births_10_14['2016_Births_Women_10-14']/births_10_14['yr2016'])*1000
    births_10_14['abr2017'] = (births_10_14['2017_Births_Women_10-14']/births_10_14['yr2017'])*1000
    births_10_14['abr2018'] = (births_10_14['2018_Births_Women_10-14']/births_10_14['yr2018'])*1000
    births_10_14['abr2019'] = (births_10_14['2019_Births_Women_10-14']/births_10_14['yr2019'])*1000
    births_10_14['abr2020'] = (births_10_14['2020_Births_Women_10-14']/births_10_14['yr2020'])*1000
    births_10_14['abr2021'] = (births_10_14['2021_Births_Women_10-14']/births_10_14['yr2021'])*1000
    

    
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
                            facet_col_spacing=0.09, template='streamlit', height=1200,
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
    
            
    births_15_19['abr2012'] = (births_15_19['2012_Births_Women_15-19']/births_15_19['yr2012'])*1000
    births_15_19['abr2013'] = (births_15_19['2013_Births_Women_15-19']/births_15_19['yr2013'])*1000
    births_15_19['abr2014'] = (births_15_19['2014_Births_Women_15-19']/births_15_19['yr2014'])*1000
    births_15_19['abr2015'] = (births_15_19['2015_Births_Women_15-19']/births_15_19['yr2015'])*1000
    births_15_19['abr2016'] = (births_15_19['2016_Births_Women_15-19']/births_15_19['yr2016'])*1000
    births_15_19['abr2017'] = (births_15_19['2017_Births_Women_15-19']/births_15_19['yr2017'])*1000
    births_15_19['abr2018'] = (births_15_19['2018_Births_Women_15-19']/births_15_19['yr2018'])*1000
    births_15_19['abr2019'] = (births_15_19['2019_Births_Women_15-19']/births_15_19['yr2019'])*1000
    births_15_19['abr2020'] = (births_15_19['2020_Births_Women_15-19']/births_15_19['yr2020'])*1000
    births_15_19['abr2021'] = (births_15_19['2021_Births_Women_15-19']/births_15_19['yr2021'])*1000



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
