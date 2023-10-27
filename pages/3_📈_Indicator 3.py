import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


projected_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRuOM0mbpu6ThzB3HLRcKkXk3LCwE-0n-nAptaowFoNLQekgFX7FqU3IClSjl5rlX85bi-7REtyqEJt/pub?output=xlsx"
data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRp2M0ySSYySdadzJmA93oPOYsoF_0bH_dweGzqrtYn_xS3ugEtZQnIamGXuZIxxQP6TRqcuhcPrnSO/pub?output=xlsx"
ind3 = pd.read_excel(data_link, sheet_name='mCPR')
#ind3['Year'] = ind3['Year'].astype('Int64')
ind3['Year'] = ind3['Year'].astype(str)

st.title('KOICA Sites in Region VIII: Secondary Data for Select Indicators in Southern Leyte')




st.header('Indicator 3:')
st.subheader('Modern Contraceptive Prevalence Rate (mCPR) in KOICA Sites')    
st.write('Indicator 3 looks at the number and proportion of adolescent girls of reproductive age (aged 15-19 years) \
            who have their need for family planning satisfied with modern methods. It is measured by looking at the \
            modern Contraceptive Prevalence Rate (mCPR), which serves as a proxy measure of access to reproductive health services.')


option_mcpr = st.selectbox(
        'Please select a City/Municipality',
        ('Bontoc', 'Libagon', 'Liloan', 'Limasawa', 'Maasin',
            'Macrohon', 'Malitbog', 'Padre Burgos', 'Sogod', 'Tomas Oppus'),
            key='selectbox_7')

if option_mcpr == 'Bontoc':
    fig_mcpr = px.line(ind3.loc[ind3['LGU']=='Bontoc', :], x='Year', y='mCPR', template='seaborn',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Libagon':
    fig_mcpr = px.line(ind3.loc[ind3['LGU']=='Libagon', :], x='Year', y='mCPR', template='seaborn',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Liloan':
    fig_mcpr = px.line(ind3.loc[ind3['LGU']=='Liloan', :], x='Year', y='mCPR', template='seaborn',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Limasawa':
    fig_mcpr = px.line(ind3.loc[ind3['LGU']=='Limasawa', :], x='Year', y='mCPR', template='seaborn',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Maasin':
    fig_mcpr = px.line(ind3.loc[ind3['LGU']=='Maasin', :], x='Year', y='mCPR', template='seaborn',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Macrohon':
    fig_mcpr = px.line(ind3.loc[ind3['LGU']=='Macrohon', :], x='Year', y='mCPR', template='seaborn',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Malitbog':
    fig_mcpr = px.line(ind3.loc[ind3['LGU']=='Malitbog', :], x='Year', y='mCPR', template='seaborn',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Padre Burgos':
    fig_mcpr = px.line(ind3.loc[ind3['LGU']=='Padre Burgos', :], x='Year', y='mCPR', template='seaborn',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Sogod':
    fig_mcpr = px.line(ind3.loc[ind3['LGU']=='Sogod', :], x='Year', y='mCPR', template='seaborn',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    st.plotly_chart(fig_mcpr, use_container_width=True)

elif option_mcpr == 'Tomas Oppus':
    fig_mcpr = px.line(ind3.loc[ind3['LGU']=='Tomas Oppus', :], x='Year', y='mCPR', template='seaborn',
                      title='Modern Contraceptive Prevalence Rate (mCPR) in {} (2019-2022)'.format(option_mcpr)
                      )
    st.plotly_chart(fig_mcpr, use_container_width=True)



# Dataframe

with st.expander('Click to see data table'):
    st.markdown('###### Modern Contraceptive Prevalence Rate (mCPR), 15-19 Females in KOICA Sites (2019-2022)')
    st.dataframe(ind3, use_container_width=True, hide_index=True)



# Summary Chart

with st.expander('Click to see summary chart'):
    fig_mcpr_all = px.line(ind3, x='Year', y='mCPR',
                        color='LGU', facet_col='LGU', facet_col_wrap=2,
                        facet_col_spacing=0.09, template='seaborn', height=1200,
                        title='Modern Contraceptive Prevalence Rate (mCPR), 15-19 Females in KOICA Sites (2019-2022)'
                      )
    
    fig_mcpr_all.update_layout(showlegend=False)
    fig_mcpr_all.update_xaxes(matches=None)
    fig_mcpr_all.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))
    fig_mcpr_all.update_yaxes(matches=None)
    fig_mcpr_all.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))

    st.plotly_chart(fig_mcpr_all, use_container_width=True)