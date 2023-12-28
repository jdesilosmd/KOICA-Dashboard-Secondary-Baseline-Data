import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from sklearn.linear_model import LinearRegression


projected_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRuOM0mbpu6ThzB3HLRcKkXk3LCwE-0n-nAptaowFoNLQekgFX7FqU3IClSjl5rlX85bi-7REtyqEJt/pub?output=xlsx"
data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRp2M0ySSYySdadzJmA93oPOYsoF_0bH_dweGzqrtYn_xS3ugEtZQnIamGXuZIxxQP6TRqcuhcPrnSO/pub?output=xlsx"

projected_10_14 = pd.read_excel(projected_link, '10-14 Women')
projected_15_19 = pd.read_excel(projected_link, '15-19 Women')
ind1 = pd.read_excel(data_link, sheet_name=0)

st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Southern Leyte')


#################################################

# Define chart function for ABR (10-14):


@st.cache_resource
def ABR_10_14(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='ABR', template='seaborn',
                                    trendline='ols', trendline_color_override='gray',
                                    title='Adolescent Birth Rate (10-14 years) in {} (2012-2021)'.format(lgu))
    fig.update_traces(mode='lines')
    model = px.get_trendline_results(fig)
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

    fig.update_layout(legend=dict(orientation='h',
                                                yanchor='bottom',
                                                y=-.3))
    fig.update_yaxes(range=[0, 5],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))
    
    return st.plotly_chart(fig, use_container_width=True)





# Define chart function for ABR (10-14):


@st.cache_resource
def ABR_15_19(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='ABR', template='seaborn',
                                       trendline='ols', trendline_color_override='gray',
                                       title='Adolescent Birth Rate (15-19 years) in {} (2012-2021)'.format(lgu))
    fig.update_traces(mode='lines')
    model = px.get_trendline_results(fig)
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

    fig.update_layout(legend=dict(orientation='h',
                                                yanchor='bottom',
                                                y=-.3))
    fig.update_yaxes(range=[0, 120],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))
    return st.plotly_chart(fig, use_container_width=True)



#################################################



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

    fig_abr_10_14_lgu_all = px.line(abr_10_14_melt, x='Year', y='ABR', template='seaborn',
                                    color='LGU',
                                    title='Adolescent Birth Rate (10-14 years) in All Southern Leyte Sites (2012-2021)')
    
    fig_abr_10_14_lgu_all.update_layout(legend=dict(orientation='h'))
    st.plotly_chart(fig_abr_10_14_lgu_all, use_container_width=True)



    option_abr_10_14_table = st.selectbox(
        'Please select a City/Municipality',
        ('Bontoc', 'Libagon', 'Liloan', 'Limasawa', 'Maasin',
            'Macrohon', 'Malitbog', 'Padre Burgos', 'Sogod', 'Tomas Oppus'),
            key='selectbox_1'
    )


# ABR 10-14 Chart per LGU
    
    if option_abr_10_14_table == 'Bontoc':
        ABR_10_14(df=abr_10_14_melt, lgu=option_abr_10_14_table)  

    elif option_abr_10_14_table == 'Libagon':
        ABR_10_14(df=abr_10_14_melt, lgu=option_abr_10_14_table)  
    
    elif option_abr_10_14_table == 'Liloan':
        ABR_10_14(df=abr_10_14_melt, lgu=option_abr_10_14_table)  

    elif option_abr_10_14_table == 'Limasawa':
        ABR_10_14(df=abr_10_14_melt, lgu=option_abr_10_14_table)  

    elif option_abr_10_14_table == 'Maasin':
        ABR_10_14(df=abr_10_14_melt, lgu=option_abr_10_14_table)  
    
    elif option_abr_10_14_table == 'Macrohon':
        ABR_10_14(df=abr_10_14_melt, lgu=option_abr_10_14_table)  
    
    elif option_abr_10_14_table == 'Malitbog':
        ABR_10_14(df=abr_10_14_melt, lgu=option_abr_10_14_table)  
    
    elif option_abr_10_14_table == 'Padre Burgos':
        ABR_10_14(df=abr_10_14_melt, lgu=option_abr_10_14_table)  
    
    elif option_abr_10_14_table == 'Sogod':
        ABR_10_14(df=abr_10_14_melt, lgu=option_abr_10_14_table)  
    
    elif option_abr_10_14_table == 'Tomas Oppus':
        ABR_10_14(df=abr_10_14_melt, lgu=option_abr_10_14_table)  

# Summary Chart for ABR (10-14)
    fig_abr_10_14 = px.scatter(abr_10_14_melt, x='Year', y='ABR',color='LGU', facet_col='LGU', facet_col_wrap=2,
                               facet_col_spacing=0.09, template='streamlit', height=1200,
                               trendline='ols', trendline_color_override='black',
                               title='Adolescent Birth Rate (10-14 years) in KOICA Sites (2012-2021)')
    

    fig_abr_10_14.update_layout(showlegend=False, title=dict(font=dict(size=18)))
    fig_abr_10_14.update_traces(mode='lines')
    fig_abr_10_14.update_yaxes(range=[0, 5])
    fig_abr_10_14.update_yaxes(title_font=dict(size=20))
    fig_abr_10_14.update_xaxes(title_font=dict(size=20))


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

    fig_abr_15_19_lgu_all = px.line(abr_15_19_melt, x='Year', y='ABR', template='seaborn',
                                    color='LGU',
                                    title='Adolescent Birth Rate (15-19 years) in All Samar Sites (2012-2021)')
    
    fig_abr_15_19_lgu_all.update_layout(legend=dict(orientation='h'))
    st.plotly_chart(fig_abr_15_19_lgu_all, use_container_width=True)


    option_abr_15_19_table = st.selectbox(
        'Please select a City/Municipality',
        ('Bontoc', 'Libagon', 'Liloan', 'Limasawa', 'Maasin',
            'Macrohon', 'Malitbog', 'Padre Burgos', 'Sogod', 'Tomas Oppus'),
            key='selectbox_2'
    )


# ABR 15-19 Chart per LGU
    
    if option_abr_15_19_table == 'Bontoc':
        ABR_15_19(df=abr_15_19_melt, lgu=option_abr_15_19_table)  
    
    elif option_abr_15_19_table == 'Libagon':
        ABR_15_19(df=abr_15_19_melt, lgu=option_abr_15_19_table)  
    
    elif option_abr_15_19_table == 'Liloan':
        ABR_15_19(df=abr_15_19_melt, lgu=option_abr_15_19_table)  

    elif option_abr_15_19_table == 'Limasawa':
        ABR_15_19(df=abr_15_19_melt, lgu=option_abr_15_19_table)  
    
    elif option_abr_15_19_table == 'Maasin':
        ABR_15_19(df=abr_15_19_melt, lgu=option_abr_15_19_table)  

    elif option_abr_15_19_table == 'Macrohon':
        ABR_15_19(df=abr_15_19_melt, lgu=option_abr_15_19_table)  
    
    elif option_abr_15_19_table == 'Malitbog':
        ABR_15_19(df=abr_15_19_melt, lgu=option_abr_15_19_table)  
    
    elif option_abr_15_19_table == 'Padre Burgos':
        ABR_15_19(df=abr_15_19_melt, lgu=option_abr_15_19_table)  
    
    elif option_abr_15_19_table == 'Sogod':
        ABR_15_19(df=abr_15_19_melt, lgu=option_abr_15_19_table)  
    
    elif option_abr_15_19_table == 'Tomas Oppus':
        ABR_15_19(df=abr_15_19_melt, lgu=option_abr_15_19_table)  



# Summary graph for 15-19
    fig_abr_15_19 = px.scatter(abr_15_19_melt, x='Year', y='ABR',color='LGU', facet_col='LGU', facet_col_wrap=2,
                               facet_col_spacing=0.09, template='seaborn', height=1200,
                               trendline='ols', trendline_color_override='black',
                               title='Adolescent Birth Rate (15-19 years) in Southern Leyte Sites (2012-2021)')
    
    fig_abr_15_19.update_layout(showlegend=False, title=dict(font=dict(size=18)))
    fig_abr_15_19.update_traces(mode='lines')
    fig_abr_15_19.update_yaxes(range=[0, 120])
    fig_abr_15_19.update_yaxes(title_font=dict(size=20))
    fig_abr_15_19.update_xaxes(title_font=dict(size=20))

    with st.expander('Click to see data table'):
        st.markdown('###### Adolescent Birth Rate in KOICA Sites from 2012 to 2021')
        abr_15_19_melt['Year'] = abr_15_19_melt['Year'].astype(str)
        st.dataframe(abr_15_19_melt, use_container_width=True, hide_index=True)
        abr_15_19_melt['Year'] = abr_15_19_melt['Year'].astype(int)
    

    with st.expander('Click to see summary chart'):
        st.plotly_chart(fig_abr_15_19, use_container_width=True)
