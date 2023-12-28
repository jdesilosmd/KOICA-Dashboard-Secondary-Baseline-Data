import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from sklearn.linear_model import LinearRegression


data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHbsYRXGNuiH9Zk7krIQHVRnhb3J1Vd4SiV5MQ0eehmEq4ZUVbasqdfzEoD7ZADoup5XUw-uaw81i/pub?output=xlsx"


surigao_dn_birth = pd.read_excel(data_link, sheet_name=2)
surigao_ds_birth = pd.read_excel(data_link, sheet_name=5)

surigao_dn_census = pd.read_excel(data_link, sheet_name=6)
surigao_ds_census = pd.read_excel(data_link, sheet_name=7)


st.title('Surigao Del Norte and Surigao Del Sur ABR Data')


# Projection function

@st.cache_resource
def projection_population(df):
    X = df[['Census Year']]
    X_reshaped = X.values.reshape(-1, 1)
    y = df['Population']
    model = LinearRegression()
    model.fit(X_reshaped, y)

    predicted = model.predict(X_reshaped)
    future_years = [2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019, 2021, 2022, 2023, 2024, 2025, 2026]
    future_X = pd.DataFrame({'Census Year': future_years})
    predicted_population = model.predict(future_X)
    df_predicted = pd.DataFrame({'Census Year': future_years,
                                 'Population': predicted_population})
                                 
    
    df_combined = pd.concat([df, df_predicted], axis=0)
    df_combined = df_combined.sort_values(by='Census Year')

    df_combined.reset_index(drop=True, inplace=True)
    df_combined.rename(columns={'Census Year': 'Year'}, inplace=True)
    df_combined['Population'] = df_combined['Population'].astype(int)

    return df_combined



# Individual chart function (10-14)
### Without projection
@st.cache_resource
def chart_10_14_noproj(df, lgu):
    fig = px.scatter(df, x='Year', y='ABR', template='seaborn',
                            trendline='ols', trendline_color_override='black',
                            title='Adolescent Birth Rate, {}'.format(lgu))
    
    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 5])

    return st.plotly_chart(fig, use_container_width=True)

### With projection
@st.cache_resource
def chart_10_14(df, lgu):
    fig = px.scatter(df, x='Year', y='ABR', template='seaborn',
                            trendline='ols', trendline_color_override='black',
                            title='Adolescent Birth Rate, {}, with Projections'.format(lgu))
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

    fig.add_trace(go.Scatter(x=xnew, y=ynew,
                                            mode='markers',
                                            name='Predicted ABR'))
    fig.update_layout(legend=dict(orientation='h',
                                                yanchor='bottom',
                                                y=-.3))
    fig.update_yaxes(range=[0, 5])
    

    return st.plotly_chart(fig, use_container_width=True)


# Individual chart function (15-19)

### Without projection

def chart_15_19_noproj(df, lgu):
    fig = px.scatter(df, x='Year', y='ABR', template='seaborn',
                            trendline='ols', trendline_color_override='black',
                            title='Adolescent Birth Rate, {}'.format(lgu))
    
    fig.update_traces(mode='lines')    
    fig.update_yaxes(range=[0, 120])

    return st.plotly_chart(fig, use_container_width=True)


### With projection
@st.cache_resource
def chart_15_19(df, lgu):
    fig = px.scatter(df, x='Year', y='ABR', template='seaborn',
                            trendline='ols', trendline_color_override='black',
                            title='Adolescent Birth Rate, {}, with Projections'.format(lgu))
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

    fig.add_trace(go.Scatter(x=xnew, y=ynew,
                                            mode='markers',
                                            name='Predicted ABR'))
    fig.update_layout(legend=dict(orientation='h',
                                                yanchor='bottom',
                                                y=-.3))
    fig.update_yaxes(range=[0, 120])

    return st.plotly_chart(fig, use_container_width=True)



# Individual chart function (10-14)

@st.cache_resource
def chart_all_10_14(df, province):
    fig = px.line(df, x='Year', y='ABR', template='seaborn',
                                    color='LGU',
                                    title='Adolescent Birth Rate (10-14 years) in {} (2015-2021)'.format(province))
    
    fig.update_layout(legend=dict(orientation='h'))
    fig.update_yaxes(range=[0, 5])
    
    st.plotly_chart(fig, use_container_width=True)


# Individual chart function (15-19)

@st.cache_resource
def chart_all_15_19(df, province):
    fig = px.line(df, x='Year', y='ABR', template='seaborn',
                                    color='LGU',
                                    title='Adolescent Birth Rate (15-19 years) in {} (2015-2021)'.format(province))
    
    fig.update_layout(legend=dict(orientation='h'))
    fig.update_yaxes(range=[0, 120])
    st.plotly_chart(fig, use_container_width=True)



# Facet chart function

@st.cache_resource
def facet_chart_10_14(df, province):
    fig = px.scatter(df, x='Year', y='ABR',color='LGU', facet_col='LGU', facet_col_wrap=3,
                    facet_col_spacing=0.09, template='streamlit', height=1200,
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth Rate (10-14 years) in {} (2015-2021)'.format(province))
    fig.update_layout(showlegend=False)
    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 5])
    return st.plotly_chart(fig, use_container_width=True)


@st.cache_resource
def facet_chart_15_19(df, province):
    fig = px.scatter(df, x='Year', y='ABR',color='LGU', facet_col='LGU', facet_col_wrap=3,
                    facet_col_spacing=0.09, template='streamlit', height=1200,
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth Rate (15-19 years) in {} (2015-2021)'.format(province))
    fig.update_layout(showlegend=False)
    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 150])
    return st.plotly_chart(fig, use_container_width=True)
    





# Merge population and birth datasets

tab1,  tab2 = st.tabs(['Surigao Del Norte', 'Surigao Del Sur'])


with tab1:
    ### Surigao Del Norte
    #### 10-14
    surigao_dn_census_10_14 = surigao_dn_census.loc[:, ['LGU',
                                                            '2010 10-14',
                                                            '2015 10-14',
                                                            '2020 10-14']]

    surigao_dn_census_10_14.rename(columns={'2010 10-14': 2010,
                                            '2015 10-14': 2015,
                                            '2020 10-14': 2020},
                                            inplace=True)

    surigao_dn_census_10_14_melt = surigao_dn_census_10_14.melt(id_vars='LGU', var_name='Census Year', value_name='Population')

    ### Projection
    df_Alegria_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Alegria', ['Census Year', 'Population']]
    df_Tubod_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Tubod', ['Census Year', 'Population']]
    df_Taganaan_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Tagana-an', ['Census Year', 'Population']]
    df_Surigao_City_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='City of Surigao (Capital)', ['Census Year', 'Population']]
    df_Socorro_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Socorro', ['Census Year', 'Population']]
    df_Santa_Monica_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Santa Monica (Sapao)', ['Census Year', 'Population']]
    df_San_Isidro_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='San Isidro', ['Census Year', 'Population']]
    df_San_Francisco_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='San Francisco (Anao-Aon)', ['Census Year', 'Population']]
    df_San_Benito_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='San Benito', ['Census Year', 'Population']]
    df_Placer_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Placer', ['Census Year', 'Population']]
    df_Sison_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Sison', ['Census Year', 'Population']]
    df_Malimono_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Malimono', ['Census Year', 'Population']]
    df_Mainit_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Mainit', ['Census Year', 'Population']]
    df_Gigaquit_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Gigaquit', ['Census Year', 'Population']]
    df_General_Luna_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='General Luna', ['Census Year', 'Population']]
    df_Del_Carmen_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Del Carmen', ['Census Year', 'Population']]
    df_Dapa_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Dapa', ['Census Year', 'Population']]
    df_Claver_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Claver', ['Census Year', 'Population']]
    df_Burgos_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Burgos', ['Census Year', 'Population']]
    df_Bacuag_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Bacuag', ['Census Year', 'Population']]
    df_Pilar_10_14 = surigao_dn_census_10_14_melt.loc[surigao_dn_census_10_14_melt['LGU']=='Pilar', ['Census Year', 'Population']]
    

    df_Alegria_10_14_projection = projection_population(df=df_Alegria_10_14)
    df_Alegria_10_14_projection['LGU'] = 'Alegria'
    df_Tubod_10_14_projection = projection_population(df=df_Tubod_10_14)
    df_Tubod_10_14_projection['LGU'] = 'Tubod'
    df_Taganaan_10_14_projection = projection_population(df=df_Taganaan_10_14)
    df_Taganaan_10_14_projection['LGU'] = 'Tagana-an'
    df_Surigao_City_10_14_projection = projection_population(df=df_Surigao_City_10_14)
    df_Surigao_City_10_14_projection['LGU'] = 'City of Surigao (Capital)'
    df_Socorro_10_14_projection = projection_population(df=df_Socorro_10_14)
    df_Socorro_10_14_projection['LGU'] = 'Socorro'
    df_Santa_Monica_10_14_projection = projection_population(df=df_Santa_Monica_10_14)
    df_Santa_Monica_10_14_projection['LGU'] = 'Santa Monica (Sapao)'
    df_San_Isidro_10_14_projection = projection_population(df=df_San_Isidro_10_14)
    df_San_Isidro_10_14_projection['LGU'] = 'San Isidro'
    df_San_Francisco_10_14_projection = projection_population(df=df_San_Francisco_10_14)
    df_San_Francisco_10_14_projection['LGU'] = 'San Francisco (Anao-Aon)'
    df_San_Benito_10_14_projection = projection_population(df=df_San_Benito_10_14)
    df_San_Benito_10_14_projection['LGU'] = 'San Benito'
    df_Placer_10_14_projection = projection_population(df=df_Placer_10_14)
    df_Placer_10_14_projection['LGU'] = 'Placer'
    df_Sison_10_14_projection = projection_population(df=df_Sison_10_14)
    df_Sison_10_14_projection['LGU'] = 'Sison'
    df_Malimono_10_14_projection = projection_population(df=df_Malimono_10_14)
    df_Malimono_10_14_projection['LGU'] = 'Malimono'
    df_Mainit_10_14_projection = projection_population(df=df_Mainit_10_14)
    df_Mainit_10_14_projection['LGU'] = 'Mainit'
    df_Gigaquit_10_14_projection = projection_population(df=df_Gigaquit_10_14)
    df_Gigaquit_10_14_projection['LGU'] = 'Gigaquit'
    df_General_Luna_10_14_projection = projection_population(df=df_General_Luna_10_14)
    df_General_Luna_10_14_projection['LGU'] = 'General Luna'
    df_Del_Carmen_10_14_projection = projection_population(df=df_Del_Carmen_10_14)
    df_Del_Carmen_10_14_projection['LGU'] = 'Del Carmen'
    df_Dapa_10_14_projection = projection_population(df=df_Dapa_10_14)
    df_Dapa_10_14_projection['LGU'] = 'Dapa'
    df_Claver_10_14_projection = projection_population(df=df_Claver_10_14)
    df_Claver_10_14_projection['LGU'] = 'Claver'
    df_Burgos_10_14_projection = projection_population(df=df_Burgos_10_14)
    df_Burgos_10_14_projection['LGU'] = 'Burgos'
    df_Bacuag_10_14_projection = projection_population(df=df_Bacuag_10_14)
    df_Bacuag_10_14_projection['LGU'] = 'Bacuag'
    df_Pilar_10_14_projection = projection_population(df=df_Pilar_10_14)
    df_Pilar_10_14_projection['LGU'] = 'Pilar'


    frames = [df_Alegria_10_14_projection,
              df_Tubod_10_14_projection,
              df_Taganaan_10_14_projection,
              df_Surigao_City_10_14_projection,
              df_Socorro_10_14_projection,
              df_Santa_Monica_10_14_projection,
              df_San_Isidro_10_14_projection,
              df_San_Francisco_10_14_projection,
              df_San_Benito_10_14_projection,
              df_Placer_10_14_projection,
              df_Sison_10_14_projection,
              df_Malimono_10_14_projection,
              df_Mainit_10_14_projection,
              df_Gigaquit_10_14_projection,
              df_General_Luna_10_14_projection,
              df_Del_Carmen_10_14_projection,
              df_Dapa_10_14_projection,
              df_Claver_10_14_projection,
              df_Burgos_10_14_projection,
              df_Bacuag_10_14_projection,
              df_Pilar_10_14_projection]
    


    surigao_dn_projected_10_14 = pd.concat(frames)


    ### ABR
    surigao_dn_birth_10_14 = surigao_dn_birth.loc[:, ['LGU',
                                                    '2015_Births_Women_10-14',
                                                    '2016_Births_Women_10-14',
                                                    '2017_Births_Women_10-14',
                                                    '2018_Births_Women_10-14',
                                                    '2019_Births_Women_10-14',
                                                    '2020_Births_Women_10-14',
                                                    '2021_Births_Women_10-14']]

    surigao_dn_birth_10_14.rename(columns={'2015_Births_Women_10-14': 2015,
                                        '2016_Births_Women_10-14': 2016,
                                        '2017_Births_Women_10-14': 2017,
                                        '2018_Births_Women_10-14': 2018,
                                        '2019_Births_Women_10-14': 2019,
                                        '2020_Births_Women_10-14': 2020,
                                        '2021_Births_Women_10-14': 2021}, inplace=True)
    



    surigao_dn_birth_10_14_melt = surigao_dn_birth_10_14.melt(id_vars='LGU', var_name='Year', value_name='Births')
    surigao_dn_10_14_merge = surigao_dn_projected_10_14.merge(surigao_dn_birth_10_14_melt, on=['LGU', 'Year'])

    surigao_dn_10_14_merge['ABR'] = (surigao_dn_10_14_merge['Births']/surigao_dn_10_14_merge['Population'])*1000
    surigao_dn_10_14_merge = surigao_dn_10_14_merge[['LGU', 'Year', 'Population', 'Births', 'ABR']]

    ### Pivot table
    surigao_dn_pivot_10_14 = pd.pivot_table(surigao_dn_10_14_merge, index='Year', values=['Population', 'Births'])
    surigao_dn_pivot_10_14['ABR'] = (surigao_dn_pivot_10_14['Births']/surigao_dn_pivot_10_14['Population'])*1000
    surigao_dn_pivot_10_14.reset_index(inplace=True)

    


    #### 15-19
    surigao_dn_census_15_19 = surigao_dn_census.loc[:, ['LGU',
                                                            '2010 15-19',
                                                            '2015 15-19',
                                                            '2020 15-19']]

    surigao_dn_census_15_19.rename(columns={'2010 15-19': 2010,
                                            '2015 15-19': 2015,
                                            '2020 15-19': 2020},
                                            inplace=True)


    surigao_dn_census_15_19_melt = surigao_dn_census_15_19.melt(id_vars='LGU', var_name='Census Year', value_name='Population')

    ### Projection
    df_Alegria_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Alegria', ['Census Year', 'Population']]
    df_Tubod_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Tubod', ['Census Year', 'Population']]
    df_Taganaan_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Tagana-an', ['Census Year', 'Population']]
    df_Surigao_City_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='City of Surigao (Capital)', ['Census Year', 'Population']]
    df_Socorro_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Socorro', ['Census Year', 'Population']]
    df_Santa_Monica_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Santa Monica (Sapao)', ['Census Year', 'Population']]
    df_San_Isidro_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='San Isidro', ['Census Year', 'Population']]
    df_San_Francisco_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='San Francisco (Anao-Aon)', ['Census Year', 'Population']]
    df_San_Benito_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='San Benito', ['Census Year', 'Population']]
    df_Placer_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Placer', ['Census Year', 'Population']]
    df_Sison_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Sison', ['Census Year', 'Population']]
    df_Malimono_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Malimono', ['Census Year', 'Population']]
    df_Mainit_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Mainit', ['Census Year', 'Population']]
    df_Gigaquit_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Gigaquit', ['Census Year', 'Population']]
    df_General_Luna_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='General Luna', ['Census Year', 'Population']]
    df_Del_Carmen_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Del Carmen', ['Census Year', 'Population']]
    df_Dapa_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Dapa', ['Census Year', 'Population']]
    df_Claver_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Claver', ['Census Year', 'Population']]
    df_Burgos_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Burgos', ['Census Year', 'Population']]
    df_Bacuag_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Bacuag', ['Census Year', 'Population']]
    df_Pilar_15_19 = surigao_dn_census_15_19_melt.loc[surigao_dn_census_15_19_melt['LGU']=='Pilar', ['Census Year', 'Population']]


    df_Alegria_15_19_projection = projection_population(df=df_Alegria_15_19)
    df_Alegria_15_19_projection['LGU'] = 'Alegria'
    df_Tubod_15_19_projection = projection_population(df=df_Tubod_15_19)
    df_Tubod_15_19_projection['LGU'] = 'Tubod'
    df_Taganaan_15_19_projection = projection_population(df=df_Taganaan_15_19)
    df_Taganaan_15_19_projection['LGU'] = 'Tagana-an'
    df_Surigao_City_15_19_projection = projection_population(df=df_Surigao_City_15_19)
    df_Surigao_City_15_19_projection['LGU'] = 'City of Surigao (Capital)'
    df_Socorro_15_19_projection = projection_population(df=df_Socorro_15_19)
    df_Socorro_15_19_projection['LGU'] = 'Socorro'
    df_Santa_Monica_15_19_projection = projection_population(df=df_Santa_Monica_15_19)
    df_Santa_Monica_15_19_projection['LGU'] = 'Santa Monica (Sapao)'
    df_San_Isidro_15_19_projection = projection_population(df=df_San_Isidro_15_19)
    df_San_Isidro_15_19_projection['LGU'] = 'San Isidro'
    df_San_Francisco_15_19_projection = projection_population(df=df_San_Francisco_15_19)
    df_San_Francisco_15_19_projection['LGU'] = 'San Francisco (Anao-Aon)'
    df_San_Benito_15_19_projection = projection_population(df=df_San_Benito_15_19)
    df_San_Benito_15_19_projection['LGU'] = 'San Benito'
    df_Placer_15_19_projection = projection_population(df=df_Placer_15_19)
    df_Placer_15_19_projection['LGU'] = 'Placer'
    df_Sison_15_19_projection = projection_population(df=df_Sison_15_19)
    df_Sison_15_19_projection['LGU'] = 'Sison'
    df_Malimono_15_19_projection = projection_population(df=df_Malimono_15_19)
    df_Malimono_15_19_projection['LGU'] = 'Malimono'
    df_Mainit_15_19_projection = projection_population(df=df_Mainit_15_19)
    df_Mainit_15_19_projection['LGU'] = 'Mainit'
    df_Gigaquit_15_19_projection = projection_population(df=df_Gigaquit_15_19)
    df_Gigaquit_15_19_projection['LGU'] = 'Gigaquit'
    df_General_Luna_15_19_projection = projection_population(df=df_General_Luna_15_19)
    df_General_Luna_15_19_projection['LGU'] = 'General Luna'
    df_Del_Carmen_15_19_projection = projection_population(df=df_Del_Carmen_15_19)
    df_Del_Carmen_15_19_projection['LGU'] = 'Del Carmen'
    df_Dapa_15_19_projection = projection_population(df=df_Dapa_15_19)
    df_Dapa_15_19_projection['LGU'] = 'Dapa'
    df_Claver_15_19_projection = projection_population(df=df_Claver_15_19)
    df_Claver_15_19_projection['LGU'] = 'Claver'
    df_Burgos_15_19_projection = projection_population(df=df_Burgos_15_19)
    df_Burgos_15_19_projection['LGU'] = 'Burgos'
    df_Bacuag_15_19_projection = projection_population(df=df_Bacuag_15_19)
    df_Bacuag_15_19_projection['LGU'] = 'Bacuag'
    df_Pilar_15_19_projection = projection_population(df=df_Pilar_15_19)
    df_Pilar_15_19_projection['LGU'] = 'Pilar'


    frames = [df_Alegria_15_19_projection,
              df_Tubod_15_19_projection,
              df_Taganaan_15_19_projection,
              df_Surigao_City_15_19_projection,
              df_Socorro_15_19_projection,
              df_Santa_Monica_15_19_projection,
              df_San_Isidro_15_19_projection,
              df_San_Francisco_15_19_projection,
              df_San_Benito_15_19_projection,
              df_Placer_15_19_projection,
              df_Sison_15_19_projection,
              df_Malimono_15_19_projection,
              df_Mainit_15_19_projection,
              df_Gigaquit_15_19_projection,
              df_General_Luna_15_19_projection,
              df_Del_Carmen_15_19_projection,
              df_Dapa_15_19_projection,
              df_Claver_15_19_projection,
              df_Burgos_15_19_projection,
              df_Bacuag_15_19_projection,
              df_Pilar_15_19_projection]
    


    surigao_dn_projected_15_19 = pd.concat(frames)


    ### ABR
    surigao_dn_birth_15_19 = surigao_dn_birth.loc[:, ['LGU',
                                                    '2015_Births_Women_15-19',
                                                    '2016_Births_Women_15-19',
                                                    '2017_Births_Women_15-19',
                                                    '2018_Births_Women_15-19',
                                                    '2019_Births_Women_15-19',
                                                    '2020_Births_Women_15-19',
                                                    '2021_Births_Women_15-19']]

    surigao_dn_birth_15_19.rename(columns={'2015_Births_Women_15-19': 2015,
                                        '2016_Births_Women_15-19': 2016,
                                        '2017_Births_Women_15-19': 2017,
                                        '2018_Births_Women_15-19': 2018,
                                        '2019_Births_Women_15-19': 2019,
                                        '2020_Births_Women_15-19': 2020,
                                        '2021_Births_Women_15-19': 2021}, inplace=True)

    surigao_dn_birth_15_19_melt = surigao_dn_birth_15_19.melt(id_vars='LGU', var_name='Year', value_name='Births')
    surigao_dn_15_19_merge = surigao_dn_projected_15_19.merge(surigao_dn_birth_15_19_melt, on=['LGU', 'Year'])

    surigao_dn_15_19_merge['ABR'] = (surigao_dn_15_19_merge['Births']/surigao_dn_15_19_merge['Population'])*1000
    surigao_dn_15_19_merge = surigao_dn_15_19_merge[['LGU', 'Year', 'Population', 'Births', 'ABR']]


    st.markdown('#### Surigao Del Norte ABR Among 10-14-Year-Old Adolescents')

    st.dataframe(surigao_dn_10_14_merge, hide_index=True)
    facet_chart_10_14(df=surigao_dn_10_14_merge, province='Surigao Del Norte')

    st.write('Adolescent Birth Rate (10-14 Years), Surigao Del Norte')
    st.dataframe(surigao_dn_pivot_10_14)
   
    chart_10_14_noproj(df=surigao_dn_pivot_10_14, lgu='Surigao Del Norte')

    chart_10_14(df=surigao_dn_pivot_10_14, lgu='Surigao Del Norte')

    st.markdown('#### Surigao Del Norte ABR Among 15-19-Year-Old Adolescents')

    ### Pivot table
    surigao_dn_pivot_15_19 = pd.pivot_table(surigao_dn_15_19_merge, index='Year', values=['Population', 'Births'])
    surigao_dn_pivot_15_19['ABR'] = (surigao_dn_pivot_15_19['Births']/surigao_dn_pivot_15_19['Population'])*1000
    surigao_dn_pivot_15_19.reset_index(inplace=True)

    st.dataframe(surigao_dn_15_19_merge, hide_index=True)
    facet_chart_15_19(df=surigao_dn_15_19_merge, province='Surigao Del Sur')

    st.write('Adolescent Birth Rate (15-19 Years), Surigao Del Norte')
    st.dataframe(surigao_dn_pivot_15_19)
    

    chart_15_19_noproj(df=surigao_dn_pivot_15_19, lgu='Surigao Del Norte')

    chart_15_19(df=surigao_dn_pivot_15_19, lgu='Surigao Del Norte')



    #####
    #####
    #####
    #####
    #####
    #####

    #####
    #####
    #####
    #####
    #####
    #####

    #####
    #####
    #####
    #####
    #####
    #####

    #####
    #####
    #####
    #####
    #####
    #####

    #####
    #####
    #####
    #####
    #####
    #####



with tab2:
    ### Surigao Del Sur
    #### 10-14
    surigao_ds_census_10_14 = surigao_ds_census.loc[:, ['LGU',
                                                            '2010 10-14',
                                                            '2015 10-14',
                                                            '2020 10-14']]

    surigao_ds_census_10_14.rename(columns={'2010 10-14': 2010,
                                            '2015 10-14': 2015,
                                            '2020 10-14': 2020},
                                            inplace=True)

    surigao_ds_census_10_14_melt = surigao_ds_census_10_14.melt(id_vars='LGU', var_name='Census Year', value_name='Population')

    ### Projection
    df_Barobo_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Barobo', ['Census Year', 'Population']]
    df_Bayabas_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Bayabas', ['Census Year', 'Population']]
    df_Bislig_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='City of Bislig', ['Census Year', 'Population']]
    df_Cagwait_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Cagwait', ['Census Year', 'Population']]
    df_Cantilan_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Cantilan', ['Census Year', 'Population']]
    df_Carmen_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Carmen', ['Census Year', 'Population']]
    df_Carrascal_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Carrascal', ['Census Year', 'Population']]
    df_Cortes_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Cortes', ['Census Year', 'Population']]
    df_Hinatuan_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Hinatuan', ['Census Year', 'Population']]
    df_Lanuza_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Lanuza', ['Census Year', 'Population']]
    df_Lianga_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Lianga', ['Census Year', 'Population']]
    df_Lingig_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Lingig', ['Census Year', 'Population']]
    df_Madrid_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Madrid', ['Census Year', 'Population']]
    df_Marihatag_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Marihatag', ['Census Year', 'Population']]
    df_San_Agustin_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='San Agustin', ['Census Year', 'Population']]
    df_Tagbina_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Tagbina', ['Census Year', 'Population']]
    df_Tago_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='Tago', ['Census Year', 'Population']]
    df_Tandag_10_14 = surigao_ds_census_10_14_melt.loc[surigao_ds_census_10_14_melt['LGU']=='City of Tandag (Capital)', ['Census Year', 'Population']]
    
    

    df_Barobo_10_14_projection = projection_population(df=df_Barobo_10_14)
    df_Barobo_10_14_projection['LGU'] = 'Barobo'
    df_Bayabas_10_14_projection = projection_population(df=df_Bayabas_10_14)
    df_Bayabas_10_14_projection['LGU'] = 'Bayabas'
    df_Bislig_10_14_projection = projection_population(df=df_Bislig_10_14)
    df_Bislig_10_14_projection['LGU'] = 'City of Bislig'
    df_Cagwait_10_14_projection = projection_population(df=df_Cagwait_10_14)
    df_Cagwait_10_14_projection['LGU'] = 'Cagwait'
    df_Cantilan_10_14_projection = projection_population(df=df_Cantilan_10_14)
    df_Cantilan_10_14_projection['LGU'] = 'Cantilan'
    df_Carmen_10_14_projection = projection_population(df=df_Carmen_10_14)
    df_Carmen_10_14_projection['LGU'] = 'Carmen'
    df_Carrascal_10_14_projection = projection_population(df=df_Carrascal_10_14)
    df_Carrascal_10_14_projection['LGU'] = 'Carrascal'
    df_Cortes_10_14_projection = projection_population(df=df_Cortes_10_14)
    df_Cortes_10_14_projection['LGU'] = 'Cortes'
    df_Hinatuan_10_14_projection = projection_population(df=df_Hinatuan_10_14)
    df_Hinatuan_10_14_projection['LGU'] = 'Hinatuan'
    df_Lanuza_10_14_projection = projection_population(df=df_Lanuza_10_14)
    df_Lanuza_10_14_projection['LGU'] = 'Lanuza'
    df_Lianga_10_14_projection = projection_population(df=df_Lianga_10_14)
    df_Lianga_10_14_projection['LGU'] = 'Lianga'
    df_Lingig_10_14_projection = projection_population(df=df_Lingig_10_14)
    df_Lingig_10_14_projection['LGU'] = 'Lingig'
    df_Madrid_10_14_projection = projection_population(df=df_Madrid_10_14)
    df_Madrid_10_14_projection['LGU'] = 'Madrid'
    df_Marihatag_10_14_projection = projection_population(df=df_Marihatag_10_14)
    df_Marihatag_10_14_projection['LGU'] = 'Marihatag'
    df_San_Agustin_10_14_projection = projection_population(df=df_San_Agustin_10_14)
    df_San_Agustin_10_14_projection['LGU'] = 'San Agustin'
    df_Tagbina_10_14_projection = projection_population(df=df_Tagbina_10_14)
    df_Tagbina_10_14_projection['LGU'] = 'Tagbina'
    df_Tago_10_14_projection = projection_population(df=df_Tago_10_14)
    df_Tago_10_14_projection['LGU'] = 'Tago'
    df_Tandag_10_14_projection = projection_population(df=df_Tandag_10_14)
    df_Tandag_10_14_projection['LGU'] = 'City of Tandag (Capital)'
    


    frames = [df_Barobo_10_14_projection,
              df_Bayabas_10_14_projection,
              df_Bislig_10_14_projection,
              df_Cagwait_10_14_projection,
              df_Cantilan_10_14_projection,
              df_Carmen_10_14_projection,
              df_Carrascal_10_14_projection,
              df_Cortes_10_14_projection,
              df_Hinatuan_10_14_projection,
              df_Lanuza_10_14_projection,
              df_Lianga_10_14_projection,
              df_Lingig_10_14_projection,
              df_Madrid_10_14_projection,
              df_Marihatag_10_14_projection,
              df_San_Agustin_10_14_projection,
              df_Tagbina_10_14_projection,
              df_Tago_10_14_projection,
              df_Tandag_10_14_projection]
    


    surigao_ds_projected_10_14 = pd.concat(frames)


    ### ABR
    surigao_ds_birth_10_14 = surigao_ds_birth.loc[:, ['LGU',
                                                    '2015_Births_Women_10-14',
                                                    '2016_Births_Women_10-14',
                                                    '2017_Births_Women_10-14',
                                                    '2018_Births_Women_10-14',
                                                    '2019_Births_Women_10-14',
                                                    '2020_Births_Women_10-14',
                                                    '2021_Births_Women_10-14']]

    surigao_ds_birth_10_14.rename(columns={'2015_Births_Women_10-14': 2015,
                                        '2016_Births_Women_10-14': 2016,
                                        '2017_Births_Women_10-14': 2017,
                                        '2018_Births_Women_10-14': 2018,
                                        '2019_Births_Women_10-14': 2019,
                                        '2020_Births_Women_10-14': 2020,
                                        '2021_Births_Women_10-14': 2021}, inplace=True)
    

    surigao_ds_birth_10_14_melt = surigao_ds_birth_10_14.melt(id_vars='LGU', var_name='Year', value_name='Births')
    surigao_ds_10_14_merge = surigao_ds_projected_10_14.merge(surigao_ds_birth_10_14_melt, on=['LGU', 'Year'])

    ### Pivot table
    surigao_ds_pivot_10_14 = pd.pivot_table(surigao_ds_10_14_merge, index='Year', values=['Population', 'Births'])
    surigao_ds_pivot_10_14['ABR'] = (surigao_ds_pivot_10_14['Births']/surigao_ds_pivot_10_14['Population'])*1000
    surigao_ds_pivot_10_14.reset_index(inplace=True)
    



    surigao_ds_birth_10_14_melt = surigao_ds_birth_10_14.melt(id_vars='LGU', var_name='Year', value_name='Births')
    surigao_ds_10_14_merge = surigao_ds_projected_10_14.merge(surigao_ds_birth_10_14_melt, on=['LGU', 'Year'])

    surigao_ds_10_14_merge['ABR'] = (surigao_ds_10_14_merge['Births']/surigao_ds_10_14_merge['Population'])*1000
    surigao_ds_10_14_merge = surigao_ds_10_14_merge[['LGU', 'Year', 'Population', 'Births', 'ABR']]


    #### 15-19
    surigao_ds_census_15_19 = surigao_ds_census.loc[:, ['LGU',
                                                            '2010 15-19',
                                                            '2015 15-19',
                                                            '2020 15-19']]

    surigao_ds_census_15_19.rename(columns={'2010 15-19': 2010,
                                            '2015 15-19': 2015,
                                            '2020 15-19': 2020},
                                            inplace=True)


    surigao_ds_census_15_19_melt = surigao_ds_census_15_19.melt(id_vars='LGU', var_name='Census Year', value_name='Population')

    ### Projection
    df_Barobo_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Barobo', ['Census Year', 'Population']]
    df_Bayabas_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Bayabas', ['Census Year', 'Population']]
    df_Bislig_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='City of Bislig', ['Census Year', 'Population']]
    df_Cagwait_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Cagwait', ['Census Year', 'Population']]
    df_Cantilan_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Cantilan', ['Census Year', 'Population']]
    df_Carmen_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Carmen', ['Census Year', 'Population']]
    df_Carrascal_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Carrascal', ['Census Year', 'Population']]
    df_Cortes_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Cortes', ['Census Year', 'Population']]
    df_Hinatuan_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Hinatuan', ['Census Year', 'Population']]
    df_Lanuza_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Lanuza', ['Census Year', 'Population']]
    df_Lianga_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Lianga', ['Census Year', 'Population']]
    df_Lingig_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Lingig', ['Census Year', 'Population']]
    df_Madrid_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Madrid', ['Census Year', 'Population']]
    df_Marihatag_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Marihatag', ['Census Year', 'Population']]
    df_San_Agustin_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='San Agustin', ['Census Year', 'Population']]
    df_Tagbina_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Tagbina', ['Census Year', 'Population']]
    df_Tago_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='Tago', ['Census Year', 'Population']]
    df_Tandag_15_19 = surigao_ds_census_15_19_melt.loc[surigao_ds_census_15_19_melt['LGU']=='City of Tandag (Capital)', ['Census Year', 'Population']]



    df_Barobo_15_19_projection = projection_population(df=df_Barobo_15_19)
    df_Barobo_15_19_projection['LGU'] = 'Barobo'
    df_Bayabas_15_19_projection = projection_population(df=df_Bayabas_15_19)
    df_Bayabas_15_19_projection['LGU'] = 'Bayabas'
    df_Bislig_15_19_projection = projection_population(df=df_Bislig_15_19)
    df_Bislig_15_19_projection['LGU'] = 'City of Bislig'
    df_Cagwait_15_19_projection = projection_population(df=df_Cagwait_15_19)
    df_Cagwait_15_19_projection['LGU'] = 'Cagwait'
    df_Cantilan_15_19_projection = projection_population(df=df_Cantilan_15_19)
    df_Cantilan_15_19_projection['LGU'] = 'Cantilan'
    df_Carmen_15_19_projection = projection_population(df=df_Carmen_15_19)
    df_Carmen_15_19_projection['LGU'] = 'Carmen'
    df_Carrascal_15_19_projection = projection_population(df=df_Carrascal_15_19)
    df_Carrascal_15_19_projection['LGU'] = 'Carrascal'
    df_Cortes_15_19_projection = projection_population(df=df_Cortes_15_19)
    df_Cortes_15_19_projection['LGU'] = 'Cortes'
    df_Hinatuan_15_19_projection = projection_population(df=df_Hinatuan_15_19)
    df_Hinatuan_15_19_projection['LGU'] = 'Hinatuan'
    df_Lanuza_15_19_projection = projection_population(df=df_Lanuza_15_19)
    df_Lanuza_15_19_projection['LGU'] = 'Lanuza'
    df_Lianga_15_19_projection = projection_population(df=df_Lianga_15_19)
    df_Lianga_15_19_projection['LGU'] = 'Lianga'
    df_Lingig_15_19_projection = projection_population(df=df_Lingig_15_19)
    df_Lingig_15_19_projection['LGU'] = 'Lingig'
    df_Madrid_15_19_projection = projection_population(df=df_Madrid_15_19)
    df_Madrid_15_19_projection['LGU'] = 'Madrid'
    df_Marihatag_15_19_projection = projection_population(df=df_Marihatag_15_19)
    df_Marihatag_15_19_projection['LGU'] = 'Marihatag'
    df_San_Agustin_15_19_projection = projection_population(df=df_San_Agustin_15_19)
    df_San_Agustin_15_19_projection['LGU'] = 'San Agustin'
    df_Tagbina_15_19_projection = projection_population(df=df_Tagbina_15_19)
    df_Tagbina_15_19_projection['LGU'] = 'Tagbina'
    df_Tago_15_19_projection = projection_population(df=df_Tago_15_19)
    df_Tago_15_19_projection['LGU'] = 'Tago'
    df_Tandag_15_19_projection = projection_population(df=df_Tandag_15_19)
    df_Tandag_15_19_projection['LGU'] = 'City of Tandag (Capital)'



    frames = [df_Barobo_15_19_projection,
              df_Bayabas_15_19_projection,
              df_Bislig_15_19_projection,
              df_Cagwait_15_19_projection,
              df_Cantilan_15_19_projection,
              df_Carmen_15_19_projection,
              df_Carrascal_15_19_projection,
              df_Cortes_15_19_projection,
              df_Hinatuan_15_19_projection,
              df_Lanuza_15_19_projection,
              df_Lianga_15_19_projection,
              df_Lingig_15_19_projection,
              df_Madrid_15_19_projection,
              df_Marihatag_15_19_projection,
              df_San_Agustin_15_19_projection,
              df_Tagbina_15_19_projection,
              df_Tago_15_19_projection,
              df_Tandag_15_19_projection]
    


    surigao_ds_projected_15_19 = pd.concat(frames)


    ### ABR
    surigao_ds_birth_15_19 = surigao_ds_birth.loc[:, ['LGU',
                                                    '2015_Births_Women_15-19',
                                                    '2016_Births_Women_15-19',
                                                    '2017_Births_Women_15-19',
                                                    '2018_Births_Women_15-19',
                                                    '2019_Births_Women_15-19',
                                                    '2020_Births_Women_15-19',
                                                    '2021_Births_Women_15-19']]

    surigao_ds_birth_15_19.rename(columns={'2015_Births_Women_15-19': 2015,
                                        '2016_Births_Women_15-19': 2016,
                                        '2017_Births_Women_15-19': 2017,
                                        '2018_Births_Women_15-19': 2018,
                                        '2019_Births_Women_15-19': 2019,
                                        '2020_Births_Women_15-19': 2020,
                                        '2021_Births_Women_15-19': 2021}, inplace=True)

    surigao_ds_birth_15_19_melt = surigao_ds_birth_15_19.melt(id_vars='LGU', var_name='Year', value_name='Births')
    surigao_ds_15_19_merge = surigao_ds_projected_15_19.merge(surigao_ds_birth_15_19_melt, on=['LGU', 'Year'])

    surigao_ds_15_19_merge['ABR'] = (surigao_ds_15_19_merge['Births']/surigao_ds_15_19_merge['Population'])*1000
    surigao_ds_15_19_merge = surigao_ds_15_19_merge[['LGU', 'Year', 'Population', 'Births', 'ABR']]



    ### Pivot table
    surigao_ds_pivot_15_19 = pd.pivot_table(surigao_ds_15_19_merge, index='Year', values=['Population', 'Births'])
    surigao_ds_pivot_15_19['ABR'] = (surigao_ds_pivot_15_19['Births']/surigao_ds_pivot_15_19['Population'])*1000
    surigao_ds_pivot_15_19.reset_index(inplace=True)




    st.markdown('#### Surigao Del Sur ABR Among 10-14-Year-Old Adolescents')

    st.dataframe(surigao_ds_10_14_merge, hide_index=True)
    facet_chart_10_14(df=surigao_ds_10_14_merge, province='Surigao Del Sur')

    st.write('Adolescent Birth Rate (10-14 Years), Surigao Del Sur')
    st.dataframe(surigao_ds_pivot_10_14)

    chart_10_14_noproj(df=surigao_ds_pivot_10_14, lgu='Surigao Del Sur')

    chart_10_14(df=surigao_ds_pivot_10_14, lgu='Surigao Del Sur')

    st.markdown('#### Surigao Del Sur ABR Among 15-19-Year-Old Adolescents')

    st.dataframe(surigao_ds_15_19_merge, hide_index=True)
    facet_chart_15_19(df=surigao_ds_15_19_merge, province='Surigao Del Sur')

    st.write('Adolescent Birth Rate (15-19 Years), Surigao Del Sur')
    st.dataframe(surigao_ds_pivot_15_19)

    chart_15_19_noproj(df=surigao_ds_pivot_15_19, lgu='Surigao Del Sur')

    chart_15_19(df=surigao_ds_pivot_15_19, lgu='Surigao Del Sur')





