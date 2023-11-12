import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.linear_model import LinearRegression

samar_10_14 = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vSAy5ZA79y4SWzw8OgytvTM-Oq0sTREP3Gi6EO74x6dbcwmFNaFD2sA-Td-lpGeWuv7dWjsaM_ZW74O/pub?output=xlsx', sheet_name='Samar 10-14')
samar_15_19 = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vSAy5ZA79y4SWzw8OgytvTM-Oq0sTREP3Gi6EO74x6dbcwmFNaFD2sA-Td-lpGeWuv7dWjsaM_ZW74O/pub?output=xlsx', sheet_name='Samar 15-19')
samar_all =   pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vSAy5ZA79y4SWzw8OgytvTM-Oq0sTREP3Gi6EO74x6dbcwmFNaFD2sA-Td-lpGeWuv7dWjsaM_ZW74O/pub?output=xlsx', sheet_name='Samar all')

sleyte_10_14 = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vSAy5ZA79y4SWzw8OgytvTM-Oq0sTREP3Gi6EO74x6dbcwmFNaFD2sA-Td-lpGeWuv7dWjsaM_ZW74O/pub?output=xlsx', sheet_name='SLeyte 10-14')
sleyte_15_19 = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vSAy5ZA79y4SWzw8OgytvTM-Oq0sTREP3Gi6EO74x6dbcwmFNaFD2sA-Td-lpGeWuv7dWjsaM_ZW74O/pub?output=xlsx', sheet_name='SLeyte 15-19')
sleyte_all =   pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vSAy5ZA79y4SWzw8OgytvTM-Oq0sTREP3Gi6EO74x6dbcwmFNaFD2sA-Td-lpGeWuv7dWjsaM_ZW74O/pub?output=xlsx', sheet_name='SLeyte all')

st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Southern Leyte')
st.header('Indicator 8: Number of educators trained on Comprehensive Sexuality Education (CSE) in KOICA Sites')


# Population of Samar
df_total_samar = samar_all.loc[samar_all['LGU']=='Total', ['Census Year', 'Population']]
df_total_samar['Census Year'] = df_total_samar['Census Year'].astype(str)
st.write('Population of Samar Province in 2010, 2015, and 2020.')
st.dataframe(df_total_samar, hide_index=True)

df_total_samar['Census Year'] = df_total_samar['Census Year'].astype(int)


# Population of Southern Leyte
df_total_sleyte = sleyte_all.loc[sleyte_all['LGU']=='Total', ['Census Year', 'Population']]
df_total_sleyte['Census Year'] = df_total_sleyte['Census Year'].astype(str)
st.write('Population of Southern Leyte Province in 2010, 2015, and 2020.')
st.dataframe(df_total_sleyte, hide_index=True)

df_total_sleyte['Census Year'] = df_total_sleyte['Census Year'].astype(int)

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

df_all_samar = projection_population(df=df_total_samar)
df_all_sleyte = projection_population(df=df_total_sleyte)


st.markdown('#### Population Projection of Samar and Southern Leyte')
col1, col2 = st.columns(2)
with col1:
    st.write('Samar Population Projection (2010-2026)')
    df_all_samar['Year'] = df_all_samar['Year'].astype(str)
    st.dataframe(df_all_samar, hide_index=True)

with col2:
    st.write('Southern Leyte Population Projection (2010-2026)')
    df_all_sleyte['Year'] = df_all_sleyte['Year'].astype(str)
    st.dataframe(df_all_sleyte, hide_index=True)


st.markdown('#### Population Projection of Each Samar Sites (2010-2026)')

tab1, tab2a, tab2b= st.tabs(['10-14 Years', '15-19 Years', 'All Age Groups'])

with tab1:

# Samar Sites

    df_samar_10_14 = pd.DataFrame(samar_10_14)

    df_basey_10_14 = df_samar_10_14.loc[df_samar_10_14['LGU']=='Basey', ['Census Year', 'Population']]
    df_calbayog_10_14 = df_samar_10_14.loc[df_samar_10_14['LGU']=='calbayog', ['Census Year', 'Population']]
    df_calbiga_10_14 = df_samar_10_14.loc[df_samar_10_14['LGU']=='Calbiga', ['Census Year', 'Population']]
    df_catbalogan_10_14 = df_samar_10_14.loc[df_samar_10_14['LGU']=='Catbalogan', ['Census Year', 'Population']]
    df_marabut_10_14 = df_samar_10_14.loc[df_samar_10_14['LGU']=='Marabut', ['Census Year', 'Population']]
    df_paranas_10_14 = df_samar_10_14.loc[df_samar_10_14['LGU']=='Paranas', ['Census Year', 'Population']]
    df_sjdbuan_10_14 = df_samar_10_14.loc[df_samar_10_14['LGU']=='San Jose De Buan', ['Census Year', 'Population']]
    df_ssebastian_10_14 = df_samar_10_14.loc[df_samar_10_14['LGU']=='San Sebastian', ['Census Year', 'Population']]
    df_srita_10_14 = df_samar_10_14.loc[df_samar_10_14['LGU']=='Santa Rita', ['Census Year', 'Population']]
    df_villareal_10_14 = df_samar_10_14.loc[df_samar_10_14['LGU']=='Villareal', ['Census Year', 'Population']]

    with st.expander('Click to see Samar sites'):
        col3, col4 = st.columns([2, 3])
        samar_sites = ['Basey',
                        'Calbayog',
                        'Calbiga',
                        'Catbalogan',
                        'Marabut',
                        'Paranas',
                        'San Jose De Buan',
                        'San Sebastian',
                        'Santa Rita',
                        'Villareal']
        with col3:
            options_samar = st.selectbox('Select a site:', samar_sites, key=1)
        
        with col4:
            if options_samar == 'Basey':
                st.write('{} Population Projection'.format('Basey'))
                basey_projection_10_14 = projection_population(df=df_basey_10_14)
                basey_projection_10_14['Year'] = basey_projection_10_14['Year'].astype(str)
                st.dataframe(basey_projection_10_14, hide_index=True)
            
            if options_samar == 'Calbayog':
                st.write('{} Population Projection'.format('Calbayog'))
                calbayog_projection_10_14 = projection_population(df=df_calbayog_10_14)
                calbayog_projection_10_14['Year'] = calbayog_projection_10_14['Year'].astype(str)
                st.dataframe(calbayog_projection_10_14, hide_index=True)

            if options_samar == 'Calbiga':
                st.write('{} Population Projection'.format('Calbiga'))
                calbiga_projection_10_14 = projection_population(df=df_calbiga_10_14)
                calbiga_projection_10_14['Year'] = calbiga_projection_10_14['Year'].astype(str)
                st.dataframe(calbiga_projection_10_14, hide_index=True)

            if options_samar == 'Catbalogan':
                st.write('{} Population Projection'.format('Catbalogan'))
                catbalogan_projection_10_14 = projection_population(df=df_catbalogan_10_14)
                catbalogan_projection_10_14['Year'] = catbalogan_projection_10_14['Year'].astype(str)
                st.dataframe(catbalogan_projection_10_14, hide_index=True)

            if options_samar == 'Marabut':
                st.write('{} Population Projection'.format('Marabut'))
                marabut_projection_10_14 = projection_population(df=df_marabut_10_14)
                marabut_projection_10_14['Year'] = marabut_projection_10_14['Year'].astype(str)
                st.dataframe(marabut_projection_10_14, hide_index=True)

            if options_samar == 'Paranas':
                st.write('{} Population Projection'.format('Paranas'))
                paranas_projection_10_14 = projection_population(df=df_paranas_10_14)
                paranas_projection_10_14['Year'] = paranas_projection_10_14['Year'].astype(str)
                st.dataframe(paranas_projection_10_14, hide_index=True)

            if options_samar == 'San Jose De Buan':
                st.write('{} Population Projection'.format('San Jose De Buan'))
                sjdbuan_projection_10_14 = projection_population(df=df_sjdbuan_10_14)
                sjdbuan_projection_10_14['Year'] = sjdbuan_projection_10_14['Year'].astype(str)
                st.dataframe(sjdbuan_projection_10_14, hide_index=True)

            if options_samar == 'San Sebastian':
                st.write('{} Population Projection'.format('San Sebastian'))
                ssebastian_projection_10_14 = projection_population(df=df_ssebastian_10_14)
                ssebastian_projection_10_14['Year'] = ssebastian_projection_10_14['Year'].astype(str)
                st.dataframe(ssebastian_projection_10_14, hide_index=True)

            if options_samar == 'Santa Rita':
                st.write('{} Population Projection'.format('Santa Rita'))
                srita_projection_10_14 = projection_population(df=df_srita_10_14)
                srita_projection_10_14['Year'] = srita_projection_10_14['Year'].astype(str)
                st.dataframe(srita_projection_10_14, hide_index=True)

            if options_samar == 'Villareal':
                st.write('{} Population Projection'.format('Villareal'))
                villareal_projection_10_14 = projection_population(df=df_villareal_10_14)
                villareal_projection_10_14['Year'] = villareal_projection_10_14['Year'].astype(str)
                st.dataframe(villareal_projection_10_14, hide_index=True)




with tab2a:

# Samar Sites

    df_samar_15_19 = pd.DataFrame(samar_15_19)

    df_basey_15_19 = df_samar_15_19.loc[df_samar_15_19['LGU']=='Basey', ['Census Year', 'Population']]
    df_calbayog_15_19 = df_samar_15_19.loc[df_samar_15_19['LGU']=='Calbayog', ['Census Year', 'Population']]
    df_calbiga_15_19 = df_samar_15_19.loc[df_samar_15_19['LGU']=='Calbiga', ['Census Year', 'Population']]
    df_catbalogan_15_19 = df_samar_15_19.loc[df_samar_15_19['LGU']=='Catbalogan', ['Census Year', 'Population']]
    df_marabut_15_19 = df_samar_15_19.loc[df_samar_15_19['LGU']=='Marabut', ['Census Year', 'Population']]
    df_paranas_15_19 = df_samar_15_19.loc[df_samar_15_19['LGU']=='Paranas', ['Census Year', 'Population']]
    df_sjdbuan_15_19 = df_samar_15_19.loc[df_samar_15_19['LGU']=='San Jose De Buan', ['Census Year', 'Population']]
    df_ssebastian_15_19 = df_samar_15_19.loc[df_samar_15_19['LGU']=='San Sebastian', ['Census Year', 'Population']]
    df_srita_15_19 = df_samar_15_19.loc[df_samar_15_19['LGU']=='Santa Rita', ['Census Year', 'Population']]
    df_villareal_15_19 = df_samar_15_19.loc[df_samar_15_19['LGU']=='Villareal', ['Census Year', 'Population']]


    with st.expander('Click to see Samar sites'):
        col5, col6 = st.columns([2, 3])
        samar_sites = ['Basey',
                        'Calbayog',
                        'Calbiga',
                        'Catbalogan',
                        'Marabut',
                        'Paranas',
                        'San Jose De Buan',
                        'San Sebastian',
                        'Santa Rita',
                        'Villareal']
        with col5:
            options_samar = st.selectbox('Select a site:', samar_sites, key=2)
        
        with col6:
            if options_samar == 'Basey':
                st.write('{} Population Projection'.format('Basey'))
                basey_projection_15_19 = projection_population(df=df_basey_15_19)
                basey_projection_15_19['Year'] = basey_projection_15_19['Year'].astype(str)
                st.dataframe(basey_projection_15_19, hide_index=True)
            
            if options_samar == 'Calbayog':
                st.write('{} Population Projection'.format('Calbayog'))
                calbayog_projection_15_19 = projection_population(df=df_calbayog_15_19)
                calbayog_projection_15_19['Year'] = calbayog_projection_15_19['Year'].astype(str)
                st.dataframe(calbayog_projection_15_19, hide_index=True)

            if options_samar == 'Calbiga':
                st.write('{} Population Projection'.format('Calbiga'))
                calbiga_projection_15_19 = projection_population(df=df_calbiga_15_19)
                calbiga_projection_15_19['Year'] = calbiga_projection_15_19['Year'].astype(str)
                st.dataframe(calbiga_projection_15_19, hide_index=True)

            if options_samar == 'Catbalogan':
                st.write('{} Population Projection'.format('Catbalogan'))
                catbalogan_projection_15_19 = projection_population(df=df_catbalogan_15_19)
                catbalogan_projection_15_19['Year'] = catbalogan_projection_15_19['Year'].astype(str)
                st.dataframe(catbalogan_projection_15_19, hide_index=True)

            if options_samar == 'Marabut':
                st.write('{} Population Projection'.format('Marabut'))
                marabut_projection_15_19 = projection_population(df=df_marabut_15_19)
                marabut_projection_15_19['Year'] = marabut_projection_15_19['Year'].astype(str)
                st.dataframe(marabut_projection_15_19, hide_index=True)

            if options_samar == 'Paranas':
                st.write('{} Population Projection'.format('Paranas'))
                paranas_projection_15_19 = projection_population(df=df_paranas_15_19)
                paranas_projection_15_19['Year'] = paranas_projection_15_19['Year'].astype(str)
                st.dataframe(paranas_projection_15_19, hide_index=True)

            if options_samar == 'San Jose De Buan':
                st.write('{} Population Projection'.format('San Jose De Buan'))
                sjdbuan_projection_15_19 = projection_population(df=df_sjdbuan_15_19)
                sjdbuan_projection_15_19['Year'] = sjdbuan_projection_15_19['Year'].astype(str)
                st.dataframe(sjdbuan_projection_15_19, hide_index=True)

            if options_samar == 'San Sebastian':
                st.write('{} Population Projection'.format('San Sebastian'))
                ssebastian_projection_15_19 = projection_population(df=df_ssebastian_15_19)
                ssebastian_projection_15_19['Year'] = ssebastian_projection_15_19['Year'].astype(str)
                st.dataframe(ssebastian_projection_15_19, hide_index=True)

            if options_samar == 'Santa Rita':
                st.write('{} Population Projection'.format('Santa Rita'))
                srita_projection_15_19 = projection_population(df=df_srita_15_19)
                srita_projection_15_19['Year'] = srita_projection_15_19['Year'].astype(str)
                st.dataframe(srita_projection_15_19, hide_index=True)

            if options_samar == 'Villareal':
                st.write('{} Population Projection'.format('Villareal'))
                villareal_projection_15_19 = projection_population(df=df_villareal_15_19)
                villareal_projection_15_19['Year'] = villareal_projection_15_19['Year'].astype(str)
                st.dataframe(villareal_projection_15_19, hide_index=True)



with tab2b:

# Samar Sites

    df_samar_all_ages = pd.DataFrame(samar_all)
    #df_samar_all_ages = df_samar_all_ages.loc[df_samar_all_ages['LGU']!='Total', ['Census Year', 'Population']]

    df_basey_all_ages = df_samar_all_ages.loc[df_samar_all_ages['LGU']=='Basey', ['Census Year', 'Population']]
    df_calbayog_all_ages = df_samar_all_ages.loc[df_samar_all_ages['LGU']=='Calbayog', ['Census Year', 'Population']]
    df_calbiga_all_ages = df_samar_all_ages.loc[df_samar_all_ages['LGU']=='Calbiga', ['Census Year', 'Population']]
    df_catbalogan_all_ages = df_samar_all_ages.loc[df_samar_all_ages['LGU']=='Catbalogan', ['Census Year', 'Population']]
    df_marabut_all_ages = df_samar_all_ages.loc[df_samar_all_ages['LGU']=='Marabut', ['Census Year', 'Population']]
    df_paranas_all_ages = df_samar_all_ages.loc[df_samar_all_ages['LGU']=='Paranas', ['Census Year', 'Population']]
    df_sjdbuan_all_ages = df_samar_all_ages.loc[df_samar_all_ages['LGU']=='San Jose De Buan', ['Census Year', 'Population']]
    df_ssebastian_all_ages = df_samar_all_ages.loc[df_samar_all_ages['LGU']=='San Sebastian', ['Census Year', 'Population']]
    df_srita_all_ages = df_samar_all_ages.loc[df_samar_all_ages['LGU']=='Santa Rita', ['Census Year', 'Population']]
    df_villareal_all_ages = df_samar_all_ages.loc[df_samar_all_ages['LGU']=='Villareal', ['Census Year', 'Population']]


    with st.expander('Click to see Samar sites'):
        col500, col600 = st.columns([2, 3])
        samar_sites = ['Basey',
                        'Calbayog',
                        'Calbiga',
                        'Catbalogan',
                        'Marabut',
                        'Paranas',
                        'San Jose De Buan',
                        'San Sebastian',
                        'Santa Rita',
                        'Villareal']
        with col500:
            options_samar = st.selectbox('Select a site:', samar_sites, key=200)
        
        with col600:
            if options_samar == 'Basey':
                st.write('{} Population Projection'.format('Basey'))
                basey_projection_all_ages = projection_population(df=df_basey_all_ages)
                basey_projection_all_ages['Year'] = basey_projection_all_ages['Year'].astype(str)
                st.dataframe(basey_projection_all_ages, hide_index=True)
            
            if options_samar == 'Calbayog':
                st.write('{} Population Projection'.format('Calbayog'))
                calbayog_projection_all_ages = projection_population(df=df_calbayog_all_ages)
                calbayog_projection_all_ages['Year'] = calbayog_projection_all_ages['Year'].astype(str)
                st.dataframe(calbayog_projection_all_ages, hide_index=True)

            if options_samar == 'Calbiga':
                st.write('{} Population Projection'.format('Calbiga'))
                calbiga_projection_all_ages = projection_population(df=df_calbiga_all_ages)
                calbiga_projection_all_ages['Year'] = calbiga_projection_all_ages['Year'].astype(str)
                st.dataframe(calbiga_projection_all_ages, hide_index=True)

            if options_samar == 'Catbalogan':
                st.write('{} Population Projection'.format('Catbalogan'))
                catbalogan_projection_all_ages = projection_population(df=df_catbalogan_all_ages)
                catbalogan_projection_all_ages['Year'] = catbalogan_projection_all_ages['Year'].astype(str)
                st.dataframe(catbalogan_projection_all_ages, hide_index=True)

            if options_samar == 'Marabut':
                st.write('{} Population Projection'.format('Marabut'))
                marabut_projection_all_ages = projection_population(df=df_marabut_all_ages)
                marabut_projection_all_ages['Year'] = marabut_projection_all_ages['Year'].astype(str)
                st.dataframe(marabut_projection_all_ages, hide_index=True)

            if options_samar == 'Paranas':
                st.write('{} Population Projection'.format('Paranas'))
                paranas_projection_all_ages = projection_population(df=df_paranas_all_ages)
                paranas_projection_all_ages['Year'] = paranas_projection_all_ages['Year'].astype(str)
                st.dataframe(paranas_projection_all_ages, hide_index=True)

            if options_samar == 'San Jose De Buan':
                st.write('{} Population Projection'.format('San Jose De Buan'))
                sjdbuan_projection_all_ages = projection_population(df=df_sjdbuan_all_ages)
                sjdbuan_projection_all_ages['Year'] = sjdbuan_projection_all_ages['Year'].astype(str)
                st.dataframe(sjdbuan_projection_all_ages, hide_index=True)

            if options_samar == 'San Sebastian':
                st.write('{} Population Projection'.format('San Sebastian'))
                ssebastian_projection_all_ages = projection_population(df=df_ssebastian_all_ages)
                ssebastian_projection_all_ages['Year'] = ssebastian_projection_all_ages['Year'].astype(str)
                st.dataframe(ssebastian_projection_all_ages, hide_index=True)

            if options_samar == 'Santa Rita':
                st.write('{} Population Projection'.format('Santa Rita'))
                srita_projection_all_ages = projection_population(df=df_srita_all_ages)
                srita_projection_all_ages['Year'] = srita_projection_all_ages['Year'].astype(str)
                st.dataframe(srita_projection_all_ages, hide_index=True)

            if options_samar == 'Villareal':
                st.write('{} Population Projection'.format('Villareal'))
                villareal_projection_all_ages = projection_population(df=df_villareal_all_ages)
                villareal_projection_all_ages['Year'] = villareal_projection_all_ages['Year'].astype(str)
                st.dataframe(villareal_projection_all_ages, hide_index=True)






# Southern Leyte

st.markdown('#### Population Projection of Each Southern Leyte Sites (2010-2026)')

tab3, tab4a, tab4b = st.tabs(['10-14 Years', '15-19 Years', 'All Age Groups'])

with tab3:

# Southern Leyte Sites

    df_sleyte_10_14 = pd.DataFrame(sleyte_10_14)

    df_bontoc_10_14 = df_sleyte_10_14.loc[df_sleyte_10_14['LGU']=='Bontoc', ['Census Year', 'Population']]
    df_libagon_10_14 = df_sleyte_10_14.loc[df_sleyte_10_14['LGU']=='Libagon', ['Census Year', 'Population']]
    df_liloan_10_14 = df_sleyte_10_14.loc[df_sleyte_10_14['LGU']=='Liloan', ['Census Year', 'Population']]
    df_limasawa_10_14 = df_sleyte_10_14.loc[df_sleyte_10_14['LGU']=='Limasawa', ['Census Year', 'Population']]
    df_maasin_10_14 = df_sleyte_10_14.loc[df_sleyte_10_14['LGU']=='Maasin', ['Census Year', 'Population']]
    df_macrohon_10_14 = df_sleyte_10_14.loc[df_sleyte_10_14['LGU']=='Macrohon', ['Census Year', 'Population']]
    df_malitbog_10_14 = df_sleyte_10_14.loc[df_sleyte_10_14['LGU']=='Malitbog', ['Census Year', 'Population']]
    df_pburgos_10_14 = df_sleyte_10_14.loc[df_sleyte_10_14['LGU']=='Padre Burgos', ['Census Year', 'Population']]
    df_sogod_10_14 = df_sleyte_10_14.loc[df_sleyte_10_14['LGU']=='Sogod', ['Census Year', 'Population']]
    df_toppus_10_14 = df_sleyte_10_14.loc[df_sleyte_10_14['LGU']=='Tomas Oppus', ['Census Year', 'Population']]

    with st.expander('Click to see Southern Leyte sites'):
        col7, col8 = st.columns([2, 3])
        sleyte_sites = ['Bontoc',
                        'Libagon',
                        'Liloan',
                        'Limasawa',
                        'Maasin',
                        'Macrohon',
                        'Malitbog',
                        'Padre Burgos',
                        'Sogod',
                        'Tomas Oppus']
        with col7:
            options_sleyte = st.selectbox('Select a site:', sleyte_sites, key=3)
        
        with col8:
            if options_sleyte == 'Bontoc':
                st.write('{} Population Projection'.format('Bontoc'))
                bontoc_projection_10_14 = projection_population(df=df_bontoc_10_14)
                bontoc_projection_10_14['Year'] = bontoc_projection_10_14['Year'].astype(str)
                st.dataframe(bontoc_projection_10_14, hide_index=True)
            
            if options_sleyte == 'Libagon':
                st.write('{} Population Projection'.format('Libagon'))
                libagon_projection_10_14 = projection_population(df=df_libagon_10_14)
                libagon_projection_10_14['Year'] = libagon_projection_10_14['Year'].astype(str)
                st.dataframe(libagon_projection_10_14, hide_index=True)

            if options_sleyte == 'Liloan':
                st.write('{} Population Projection'.format('Liloan'))
                liloan_projection_10_14 = projection_population(df=df_liloan_10_14)
                liloan_projection_10_14['Year'] = liloan_projection_10_14['Year'].astype(str)
                st.dataframe(liloan_projection_10_14, hide_index=True)

            if options_sleyte == 'Limasawa':
                st.write('{} Population Projection'.format('Limasawa'))
                limasawa_projection_10_14 = projection_population(df=df_limasawa_10_14)
                limasawa_projection_10_14['Year'] = limasawa_projection_10_14['Year'].astype(str)
                st.dataframe(limasawa_projection_10_14, hide_index=True)

            if options_sleyte == 'Maasin':
                st.write('{} Population Projection'.format('Maasin'))
                maasin_projection_10_14 = projection_population(df=df_maasin_10_14)
                maasin_projection_10_14['Year'] = maasin_projection_10_14['Year'].astype(str)
                st.dataframe(maasin_projection_10_14, hide_index=True)

            if options_sleyte == 'Macrohon':
                st.write('{} Population Projection'.format('Macrohon'))
                macrohon_projection_10_14 = projection_population(df=df_macrohon_10_14)
                macrohon_projection_10_14['Year'] = macrohon_projection_10_14['Year'].astype(str)
                st.dataframe(macrohon_projection_10_14, hide_index=True)

            if options_sleyte == 'Malitbog':
                st.write('{} Population Projection'.format('Malitbog'))
                malitbog_projection_10_14 = projection_population(df=df_malitbog_10_14)
                malitbog_projection_10_14['Year'] = malitbog_projection_10_14['Year'].astype(str)
                st.dataframe(malitbog_projection_10_14, hide_index=True)

            if options_sleyte == 'Padre Burgos':
                st.write('{} Population Projection'.format('Padre Burgos'))
                pburgos_projection_10_14 = projection_population(df=df_pburgos_10_14)
                pburgos_projection_10_14['Year'] = pburgos_projection_10_14['Year'].astype(str)
                st.dataframe(pburgos_projection_10_14, hide_index=True)

            if options_sleyte == 'Sogod':
                st.write('{} Population Projection'.format('Sogod'))
                sogod_projection_10_14 = projection_population(df=df_sogod_10_14)
                sogod_projection_10_14['Year'] = sogod_projection_10_14['Year'].astype(str)
                st.dataframe(sogod_projection_10_14, hide_index=True)

            if options_sleyte == 'Tomas Oppus':
                st.write('{} Population Projection'.format('Toppus'))
                toppus_projection_10_14 = projection_population(df=df_toppus_10_14)
                toppus_projection_10_14['Year'] = toppus_projection_10_14['Year'].astype(str)
                st.dataframe(toppus_projection_10_14, hide_index=True)




with tab4a:

# sleyte Sites

    df_sleyte_15_19 = pd.DataFrame(sleyte_15_19)

    df_bontoc_15_19 = df_sleyte_15_19.loc[df_sleyte_15_19['LGU']=='Bontoc', ['Census Year', 'Population']]
    df_libagon_15_19 = df_sleyte_15_19.loc[df_sleyte_15_19['LGU']=='Libagon', ['Census Year', 'Population']]
    df_liloan_15_19 = df_sleyte_15_19.loc[df_sleyte_15_19['LGU']=='Liloan', ['Census Year', 'Population']]
    df_limasawa_15_19 = df_sleyte_15_19.loc[df_sleyte_15_19['LGU']=='Limasawa', ['Census Year', 'Population']]
    df_maasin_15_19 = df_sleyte_15_19.loc[df_sleyte_15_19['LGU']=='Maasin', ['Census Year', 'Population']]
    df_macrohon_15_19 = df_sleyte_15_19.loc[df_sleyte_15_19['LGU']=='Macrohon', ['Census Year', 'Population']]
    df_malitbog_15_19 = df_sleyte_15_19.loc[df_sleyte_15_19['LGU']=='Malitbog', ['Census Year', 'Population']]
    df_pburgos_15_19 = df_sleyte_15_19.loc[df_sleyte_15_19['LGU']=='Padre Burgos', ['Census Year', 'Population']]
    df_sogod_15_19 = df_sleyte_15_19.loc[df_sleyte_15_19['LGU']=='Sogod', ['Census Year', 'Population']]
    df_toppus_15_19 = df_sleyte_15_19.loc[df_sleyte_15_19['LGU']=='Tomas Oppus', ['Census Year', 'Population']]


    with st.expander('Click to see Southern Leyte sites'):
        col9, col10 = st.columns([2, 3])
        sleyte_sites = ['Bontoc',
                        'Libagon',
                        'Liloan',
                        'Limasawa',
                        'Maasin',
                        'Macrohon',
                        'Malitbog',
                        'Padre Burgos',
                        'Sogod',
                        'Tomas Oppus']
        with col9:
            options_sleyte = st.selectbox('Select a site:', sleyte_sites, key=4)
        
        with col10:
            if options_sleyte == 'Bontoc':
                st.write('{} Population Projection'.format('Bontoc'))
                bontoc_projection_15_19 = projection_population(df=df_bontoc_15_19)
                bontoc_projection_15_19['Year'] = bontoc_projection_15_19['Year'].astype(str)
                st.dataframe(bontoc_projection_15_19, hide_index=True)
            
            if options_sleyte == 'Libagon':
                st.write('{} Population Projection'.format('Libagon'))
                libagon_projection_15_19 = projection_population(df=df_libagon_15_19)
                libagon_projection_15_19['Year'] = libagon_projection_15_19['Year'].astype(str)
                st.dataframe(libagon_projection_15_19, hide_index=True)

            if options_sleyte == 'Liloan':
                st.write('{} Population Projection'.format('Liloan'))
                liloan_projection_15_19 = projection_population(df=df_liloan_15_19)
                liloan_projection_15_19['Year'] = liloan_projection_15_19['Year'].astype(str)
                st.dataframe(liloan_projection_15_19, hide_index=True)

            if options_sleyte == 'Limasawa':
                st.write('{} Population Projection'.format('Limasawa'))
                limasawa_projection_15_19 = projection_population(df=df_limasawa_15_19)
                limasawa_projection_15_19['Year'] = limasawa_projection_15_19['Year'].astype(str)
                st.dataframe(limasawa_projection_15_19, hide_index=True)

            if options_sleyte == 'Maasin':
                st.write('{} Population Projection'.format('Maasin'))
                maasin_projection_15_19 = projection_population(df=df_maasin_15_19)
                maasin_projection_15_19['Year'] = maasin_projection_15_19['Year'].astype(str)
                st.dataframe(maasin_projection_15_19, hide_index=True)

            if options_sleyte == 'Macrohon':
                st.write('{} Population Projection'.format('Macrohon'))
                macrohon_projection_15_19 = projection_population(df=df_macrohon_15_19)
                macrohon_projection_15_19['Year'] = macrohon_projection_15_19['Year'].astype(str)
                st.dataframe(macrohon_projection_15_19, hide_index=True)

            if options_sleyte == 'Malitbog':
                st.write('{} Population Projection'.format('Malitbog'))
                malitbog_projection_15_19 = projection_population(df=df_malitbog_15_19)
                malitbog_projection_15_19['Year'] = malitbog_projection_15_19['Year'].astype(str)
                st.dataframe(malitbog_projection_15_19, hide_index=True)

            if options_sleyte == 'Padre Burgos':
                st.write('{} Population Projection'.format('Padre Burgos'))
                pburgos_projection_15_19 = projection_population(df=df_pburgos_15_19)
                pburgos_projection_15_19['Year'] = pburgos_projection_15_19['Year'].astype(str)
                st.dataframe(pburgos_projection_15_19, hide_index=True)

            if options_sleyte == 'Sogod':
                st.write('{} Population Projection'.format('Sogod'))
                sogod_projection_15_19 = projection_population(df=df_sogod_15_19)
                sogod_projection_15_19['Year'] = sogod_projection_15_19['Year'].astype(str)
                st.dataframe(sogod_projection_15_19, hide_index=True)

            if options_sleyte == 'Tomas Oppus':
                st.write('{} Population Projection'.format('Tomas Oppus'))
                toppus_projection_15_19 = projection_population(df=df_toppus_15_19)
                toppus_projection_15_19['Year'] = toppus_projection_15_19['Year'].astype(str)
                st.dataframe(toppus_projection_15_19, hide_index=True)



with tab4b:
    df_sleyte_all_ages = pd.DataFrame(sleyte_all)
    #df_sleyte_all_ages = df_sleyte_all_ages.loc[df_sleyte_all_ages['LGU']!='Total', :]


    df_bontoc_all_ages = df_sleyte_all_ages.loc[df_sleyte_all_ages['LGU']=='Bontoc', ['Census Year', 'Population']]
    df_libagon_all_ages = df_sleyte_all_ages.loc[df_sleyte_all_ages['LGU']=='Libagon', ['Census Year', 'Population']]
    df_liloan_all_ages = df_sleyte_all_ages.loc[df_sleyte_all_ages['LGU']=='Liloan', ['Census Year', 'Population']]
    df_limasawa_all_ages = df_sleyte_all_ages.loc[df_sleyte_all_ages['LGU']=='Limasawa', ['Census Year', 'Population']]
    df_maasin_all_ages = df_sleyte_all_ages.loc[df_sleyte_all_ages['LGU']=='Maasin', ['Census Year', 'Population']]
    df_macrohon_all_ages = df_sleyte_all_ages.loc[df_sleyte_all_ages['LGU']=='Macrohon', ['Census Year', 'Population']]
    df_malitbog_all_ages = df_sleyte_all_ages.loc[df_sleyte_all_ages['LGU']=='Malitbog', ['Census Year', 'Population']]
    df_pburgos_all_ages = df_sleyte_all_ages.loc[df_sleyte_all_ages['LGU']=='Padre Burgos', ['Census Year', 'Population']]
    df_sogod_all_ages = df_sleyte_all_ages.loc[df_sleyte_all_ages['LGU']=='Sogod', ['Census Year', 'Population']]
    df_toppus_all_ages = df_sleyte_all_ages.loc[df_sleyte_all_ages['LGU']=='Tomas Oppus', ['Census Year', 'Population']]


    with st.expander('Click to see Southern Leyte sites'):
        col900, col1000 = st.columns([2, 3])
        sleyte_sites = ['Bontoc',
                        'Libagon',
                        'Liloan',
                        'Limasawa',
                        'Maasin',
                        'Macrohon',
                        'Malitbog',
                        'Padre Burgos',
                        'Sogod',
                        'Tomas Oppus']
        with col900:
            options_sleyte = st.selectbox('Select a site:', sleyte_sites, key=400)
        
        with col1000:
            if options_sleyte == 'Bontoc':
                st.write('{} Population Projection'.format('Bontoc'))
                bontoc_projection_all_ages = projection_population(df=df_bontoc_all_ages)
                bontoc_projection_all_ages['Year'] = bontoc_projection_all_ages['Year'].astype(str)
                st.dataframe(bontoc_projection_all_ages, hide_index=True)
            
            if options_sleyte == 'Libagon':
                st.write('{} Population Projection'.format('Libagon'))
                libagon_projection_all_ages = projection_population(df=df_libagon_all_ages)
                libagon_projection_all_ages['Year'] = libagon_projection_all_ages['Year'].astype(str)
                st.dataframe(libagon_projection_all_ages, hide_index=True)

            if options_sleyte == 'Liloan':
                st.write('{} Population Projection'.format('Liloan'))
                liloan_projection_all_ages = projection_population(df=df_liloan_all_ages)
                liloan_projection_all_ages['Year'] = liloan_projection_all_ages['Year'].astype(str)
                st.dataframe(liloan_projection_all_ages, hide_index=True)

            if options_sleyte == 'Limasawa':
                st.write('{} Population Projection'.format('Limasawa'))
                limasawa_projection_all_ages = projection_population(df=df_limasawa_all_ages)
                limasawa_projection_all_ages['Year'] = limasawa_projection_all_ages['Year'].astype(str)
                st.dataframe(limasawa_projection_all_ages, hide_index=True)

            if options_sleyte == 'Maasin':
                st.write('{} Population Projection'.format('Maasin'))
                maasin_projection_all_ages = projection_population(df=df_maasin_all_ages)
                maasin_projection_all_ages['Year'] = maasin_projection_all_ages['Year'].astype(str)
                st.dataframe(maasin_projection_all_ages, hide_index=True)

            if options_sleyte == 'Macrohon':
                st.write('{} Population Projection'.format('Macrohon'))
                macrohon_projection_all_ages = projection_population(df=df_macrohon_all_ages)
                macrohon_projection_all_ages['Year'] = macrohon_projection_all_ages['Year'].astype(str)
                st.dataframe(macrohon_projection_all_ages, hide_index=True)

            if options_sleyte == 'Malitbog':
                st.write('{} Population Projection'.format('Malitbog'))
                malitbog_projection_all_ages = projection_population(df=df_malitbog_all_ages)
                malitbog_projection_all_ages['Year'] = malitbog_projection_all_ages['Year'].astype(str)
                st.dataframe(malitbog_projection_all_ages, hide_index=True)

            if options_sleyte == 'Padre Burgos':
                st.write('{} Population Projection'.format('Padre Burgos'))
                pburgos_projection_all_ages = projection_population(df=df_pburgos_all_ages)
                pburgos_projection_all_ages['Year'] = pburgos_projection_all_ages['Year'].astype(str)
                st.dataframe(pburgos_projection_all_ages, hide_index=True)

            if options_sleyte == 'Sogod':
                st.write('{} Population Projection'.format('Sogod'))
                sogod_projection_all_ages = projection_population(df=df_sogod_all_ages)
                sogod_projection_all_ages['Year'] = sogod_projection_all_ages['Year'].astype(str)
                st.dataframe(sogod_projection_all_ages, hide_index=True)

            if options_sleyte == 'Tomas Oppus':
                st.write('{} Population Projection'.format('Tomas Oppus'))
                toppus_projection_all_ages = projection_population(df=df_toppus_all_ages)
                toppus_projection_all_ages['Year'] = toppus_projection_all_ages['Year'].astype(str)
                st.dataframe(toppus_projection_all_ages, hide_index=True)

            
