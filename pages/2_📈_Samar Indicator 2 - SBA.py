import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwKvqsNtKWqBgIwhVv6TDzCJMMwpr4uvBR9hdkb57qHsnFtIsJI3l2kFs1oIa2LhsQePTGtYjLIj4U/pub?output=xlsx"
ind2a = pd.read_excel(data_link, sheet_name="SBA Maternal Residence")
ind2b = pd.read_excel(data_link, sheet_name="SBA Occurrence")

st.title('UN-KOICA Sites in Region VIII: Secondary Data for Select Indicators in UN-KOICA Sites in Samar')


st.header('Indicator 2:')
st.subheader('Number of adolescent births attended by skilled health personnel among adolescents aged 10-19 in UN-KOICA Sites in Samar')


############################################

# SBA Function


@st.cache_resource
def SBA_10_14(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent SBA', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (10-14 years) Performed by a<br>Skilled Birth Attendant (SBA) in {} (2012-2021)'.format(lgu))
    
    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 100],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))
    
    return st.plotly_chart(fig, use_container_width=True)



@st.cache_resource
def SBA_10_14_forecast(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent SBA', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (10-14 years) Performed by a<br>Skilled Birth Attendant (SBA) in {} (2012-2021)'.format(lgu))
    
      
    fig.update_traces(mode='lines')
    model = px.get_trendline_results(fig)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0] 
    slope = results.params[1] 
    xnew = [2022, 2023, 2024, 2025, 2026] 
    ynew = [slope*x+intercept for x in xnew] 
    ynew = [0 if y < 0 else y for y in ynew] 
    extrapolated1 = {'Year': xnew, 'Predicted ABR': ynew} 
    df_extrapolated1 = pd.DataFrame(extrapolated1)
    df_extrapolated1['Year'] = df_extrapolated1['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares (10-14 Years):')
    st.dataframe(df_extrapolated1, hide_index=True)
    df_extrapolated1['Year'] = df_extrapolated1['Year'].astype(int)

    fig.add_trace(go.Scatter(x=xnew, y=ynew,
                                                mode='markers',
                                                name='Predicted ABR'))
    
    fig.update_layout(legend=dict(orientation='h',
                                                yanchor='bottom',
                                                y=-.3))
    
    fig.update_yaxes(range=[0, 100],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))
    return st.plotly_chart(fig, use_container_width=True)



@st.cache_resource
def SBA_15_19(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent SBA', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (10-14 years) Performed by a<br>Skilled Birth Attendant (SBA) in {} (2012-2021)'.format(option_table))
    
    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 120],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))
    
    return st.plotly_chart(fig, use_container_width=True)



@st.cache_resource
def SBA_15_19_forecast(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent SBA', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (15-19 years) Performed by a<br>Skilled Birth Attendant (SBA) in {} (2012-2021)'.format(option_table))
    
    fig.update_traces(mode='lines')
    model = px.get_trendline_results(fig)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0] 
    slope = results.params[1] 
    xnew = [2022, 2023, 2024, 2025, 2026] 
    ynew = [slope*x+intercept for x in xnew] 
    ynew = [0 if y < 0 else y for y in ynew] 
    extrapolated1 = {'Year': xnew, 'Predicted ABR': ynew} 
    df_extrapolated1 = pd.DataFrame(extrapolated1)
    df_extrapolated1['Year'] = df_extrapolated1['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares (10-14 Years):')
    st.dataframe(df_extrapolated1, hide_index=True)
    df_extrapolated1['Year'] = df_extrapolated1['Year'].astype(int)

    fig.add_trace(go.Scatter(x=xnew, y=ynew,
                                                mode='markers',
                                                name='Predicted ABR'))
    
    fig.update_layout(legend=dict(orientation='h',
                                                yanchor='bottom',
                                                y=-.3))
    

    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 120],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))

    return st.plotly_chart(fig, use_container_width=True)




# TBA Function


@st.cache_resource
def TBA_10_14(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent TBA', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (10-14 years) Performed by a<br>Skilled Birth Attendant (SBA) in {} (2012-2021)'.format(lgu))
    
    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 100],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))
    
    return st.plotly_chart(fig, use_container_width=True)



@st.cache_resource
def TBA_10_14_forecast(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent TBA', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (10-14 years)) Performed by a<br>Traditional Birth Attendant (TBA) in {} (2012-2021)'.format(lgu))
     
    fig.update_traces(mode='lines')
    model = px.get_trendline_results(fig)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0] 
    slope = results.params[1] 
    xnew = [2022, 2023, 2024, 2025, 2026] 
    ynew = [slope*x+intercept for x in xnew] 
    ynew = [0 if y < 0 else y for y in ynew] 
    extrapolated1 = {'Year': xnew, 'Predicted ABR': ynew} 
    df_extrapolated1 = pd.DataFrame(extrapolated1)
    df_extrapolated1['Year'] = df_extrapolated1['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares (10-14 Years):')
    st.dataframe(df_extrapolated1, hide_index=True)
    df_extrapolated1['Year'] = df_extrapolated1['Year'].astype(int)



    fig.update_yaxes(range=[0, 100],
                     title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))

    return st.plotly_chart(fig, use_container_width=True)



@st.cache_resource
def TBA_15_19(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent TBA', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (15-19 years)) Performed by a<br>Traditional Birth Attendant (TBA) in {} (2012-2021)'.format(option_table))
    
    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 120],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))
    
    return st.plotly_chart(fig, use_container_width=True)



@st.cache_resource
def TBA_15_19_forecast(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent TBA', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (15-19 years)) Performed by a<br>Traditional Birth Attendant (TBA) in {} (2012-2021)'.format(option_table))
    
    fig.update_traces(mode='lines')
    model = px.get_trendline_results(fig)
    results =  model.iloc[0]["px_fit_results"]
    intercept = results.params[0] 
    slope = results.params[1] 
    xnew = [2022, 2023, 2024, 2025, 2026] 
    ynew = [slope*x+intercept for x in xnew] 
    ynew = [0 if y < 0 else y for y in ynew] 
    extrapolated1 = {'Year': xnew, 'Predicted ABR': ynew} 
    df_extrapolated1 = pd.DataFrame(extrapolated1)
    df_extrapolated1['Year'] = df_extrapolated1['Year'].astype(str)
    st.write('Predictions for 2022 to 2026 using Ordinary Least Squares (10-14 Years):')
    st.dataframe(df_extrapolated1, hide_index=True)
    df_extrapolated1['Year'] = df_extrapolated1['Year'].astype(int)


    fig.add_trace(go.Scatter(x=xnew, y=ynew,
                                                mode='markers',
                                                name='Predicted ABR'))
    
    fig.update_layout(legend=dict(orientation='h',
                                                yanchor='bottom',
                                                y=-.3))
    fig.update_yaxes(range=[0, 120],
                     title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))

    return st.plotly_chart(fig, use_container_width=True)




# Others Function


@st.cache_resource
def Others_10_14(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent Others', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (10-14 years) Performed Neither by an<br>SBA nor a TBA in {} (2012-2021)'.format(lgu))
    
    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 100],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))
    
    return st.plotly_chart(fig, use_container_width=True)


@st.cache_resource
def Others_15_19(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent Others', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (15-19 years) Performed Neither by an<br>SBA nor a TBA in {} (2012-2021)'.format(option_table))
    
    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 120],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))
    
    return st.plotly_chart(fig, use_container_width=True)




# Not Stated Function


@st.cache_resource
def Not_Stated_10_14(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent Not Stated', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (10-14 years) Not Classified as to<br>Who Performed the Delivery in {} (2012-2021)'.format(lgu))
    
    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 100],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))
    
    return st.plotly_chart(fig, use_container_width=True)


@st.cache_resource
def Not_Stated_15_19(df, lgu):
    fig = px.scatter(df.loc[df['LGU']==lgu,:], x='Year', y='Percent Not Stated', template='seaborn',
                                 trendline='ols', trendline_color_override='black',
                                 title='Adolescent Birth (15-19 years) Not Classified as to<br>Who Performed the Delivery in {} (2012-2021)'.format(lgu))
    
    fig.update_traces(mode='lines')
    fig.update_yaxes(range=[0, 120],
                    title_font=dict(size=20))
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_layout(title=dict(font=dict(size=18)))
    
    return st.plotly_chart(fig, use_container_width=True)




# Bar Graph Function

@st.cache_resource
def SBA_bar_10_19(df, lgu, yrange=[0, 120]):
    fig_bar = px.bar(df.loc[df['LGU']==lgu,:], x='Year', y='SBA', template='seaborn',
                 color='Age Range', barmode='group',
                 title='Adolescent Birth (10-19 years) Performed by a Skilled Birth Attendant (SBA) in {}<br>(2012-2021, Actual Count)'.format(lgu))
    
    fig_bar.update_yaxes(range=yrange,
                    title_font=dict(size=20))
    fig_bar.update_xaxes(title_font=dict(size=20))
    fig_bar.update_layout(title=dict(font=dict(size=18)))
    return st.plotly_chart(fig_bar, use_container_width=True)    

def SBA_pct_bar_10_19(df, lgu, yrange=[0, 100]):
    fig_bar = px.bar(df.loc[df['LGU']==lgu,:], x='Year', y='Percent SBA', template='seaborn',
                 color='Age Range', barmode='group',
                 title='Adolescent Birth (10-19 years) Performed by a Skilled Birth Attendant (SBA) in {}<br>(2012-2021, Percent)'.format(lgu))
    
    fig_bar.update_yaxes(range=yrange,
                    title_font=dict(size=20))
    fig_bar.update_xaxes(title_font=dict(size=20))
    fig_bar.update_layout(title=dict(font=dict(size=18)))
    return st.plotly_chart(fig_bar, use_container_width=True)

def TBA_bar_10_19(df, lgu, yrange=[0, 120]):
    fig_bar = px.bar(df.loc[df['LGU']==lgu,:], x='Year', y='TBA', template='seaborn',
                 color='Age Range', barmode='group',
                 title='Adolescent Birth (10-19 years) Performed by a Traditional Birth Attendant (TBA) in {}<br>(2012-2021, Actual Count)'.format(lgu))

    fig_bar.update_yaxes(range=yrange,
                    title_font=dict(size=20))
    fig_bar.update_xaxes(title_font=dict(size=20))
    fig_bar.update_layout(title=dict(font=dict(size=18)))
    return st.plotly_chart(fig_bar, use_container_width=True)

def TBA_pct_bar_10_19(df, lgu, yrange=[0, 100]):
    fig_bar = px.bar(df.loc[df['LGU']==lgu,:], x='Year', y='Percent TBA', template='seaborn',
                 color='Age Range', barmode='group',
                 title='Adolescent Birth (10-19 years) Performed by a Traditional Birth Attendant (TBA) in {}<br>(2012-2021, Percent)'.format(lgu))

    fig_bar.update_yaxes(range=yrange,
                    title_font=dict(size=20))
    fig_bar.update_xaxes(title_font=dict(size=20))
    fig_bar.update_layout(title=dict(font=dict(size=18)))
    return st.plotly_chart(fig_bar, use_container_width=True)


#############################################





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
                    title='Adolescent Birth (10-14 years) Done by a<br>Skilled Birth Attendant in Samar Sites (2012-2021, Percent)')
        
        fig_graph_15_19_all = px.scatter(maternal_15_19_all, x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) Done by a<br>Skilled Birth Attendant in Samar Sites (2012-2021, Percent)')
        fig_graph_10_19_all = px.bar(maternal_all, x='Year', y='Percent SBA', template='seaborn',
                                     color='Age Range',
                                     title='Adolescent Birth (10-19 years) Done by a<br>Skilled Birth Attendant in Samar Sites (2012-2021, Percent)')
        
        fig_graph_10_14_all.update_traces(mode='lines')
        fig_graph_15_19_all.update_traces(mode='lines')
        st.plotly_chart(fig_graph_10_14_all, use_container_width=True)
        st.plotly_chart(fig_graph_15_19_all, use_container_width=True)
        st.plotly_chart(fig_graph_10_19_all, use_container_width=True)



    option_table = st.selectbox(
        'Please select a City/Municipality',
        ('Basey', 'Calbayog', 'Calbiga', 'Catbalogan', 'Marabut',
            'Paranas', 'San Jose De Buan', 'San Sebastian', 'Santa Rita', 'Villareal'),
            key='selectbox_3'
    )

    graph = st.radio(
        'Birth attendant type:',
        ['SBA', 'TBA', 'Others', 'Not Stated'],
        captions=['Skilled Birth Attendants (i.e., doctor, nurse, midwife)',
                'Traditional Birth Attendants (i.e., hilot, manaram)',
                'Neither SBA nor TBA',
                'Not reported'], key='radio_1')
    
    
    if option_table == 'Basey':
                    
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_1')
            if predict_check:
                SBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                SBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                SBA_10_14(df=maternal_10_14, lgu=option_table)
                SBA_15_19(df=maternal_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2a, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2a, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_2')
            if predict_check:
                TBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                TBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                TBA_10_14(df=maternal_10_14, lgu=option_table)
                TBA_15_19(df=maternal_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2a, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2a, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=maternal_10_14, lgu=option_table)
            Others_15_19(df=maternal_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=maternal_10_14, lgu=option_table)
            Not_Stated_15_19(df=maternal_10_14, lgu=option_table)

        

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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_3')
            if predict_check:
                SBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                SBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                SBA_10_14(df=maternal_10_14, lgu=option_table)
                SBA_15_19(df=maternal_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2a, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2a, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_4')
            if predict_check:
                TBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                TBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                TBA_10_14(df=maternal_10_14, lgu=option_table)
                TBA_15_19(df=maternal_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2a, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2a, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=maternal_10_14, lgu=option_table)
            Others_15_19(df=maternal_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=maternal_10_14, lgu=option_table)
            Not_Stated_15_19(df=maternal_10_14, lgu=option_table)

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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_5')
            if predict_check:
                SBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                SBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                SBA_10_14(df=maternal_10_14, lgu=option_table)
                SBA_15_19(df=maternal_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2a, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2a, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_6')
            if predict_check:
                TBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                TBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                TBA_10_14(df=maternal_10_14, lgu=option_table)
                TBA_15_19(df=maternal_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2a, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2a, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=maternal_10_14, lgu=option_table)
            Others_15_19(df=maternal_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=maternal_10_14, lgu=option_table)
            Not_Stated_15_19(df=maternal_10_14, lgu=option_table)
        
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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_7')
            if predict_check:
                SBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                SBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                SBA_10_14(df=maternal_10_14, lgu=option_table)
                SBA_15_19(df=maternal_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2a, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2a, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_8')
            if predict_check:
                TBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                TBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                TBA_10_14(df=maternal_10_14, lgu=option_table)
                TBA_15_19(df=maternal_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2a, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2a, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=maternal_10_14, lgu=option_table)
            Others_15_19(df=maternal_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=maternal_10_14, lgu=option_table)
            Not_Stated_15_19(df=maternal_10_14, lgu=option_table)
        

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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_9')
            if predict_check:
                SBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                SBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                SBA_10_14(df=maternal_10_14, lgu=option_table)
                SBA_15_19(df=maternal_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2a, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2a, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_10')
            if predict_check:
                TBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                TBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                TBA_10_14(df=maternal_10_14, lgu=option_table)
                TBA_15_19(df=maternal_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2a, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2a, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=maternal_10_14, lgu=option_table)
            Others_15_19(df=maternal_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=maternal_10_14, lgu=option_table)
            Not_Stated_15_19(df=maternal_10_14, lgu=option_table)

        
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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_11')
            if predict_check:
                SBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                SBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                SBA_10_14(df=maternal_10_14, lgu=option_table)
                SBA_15_19(df=maternal_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2a, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2a, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_12')
            if predict_check:
                TBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                TBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                TBA_10_14(df=maternal_10_14, lgu=option_table)
                TBA_15_19(df=maternal_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2a, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2a, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=maternal_10_14, lgu=option_table)
            Others_15_19(df=maternal_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=maternal_10_14, lgu=option_table)
            Not_Stated_15_19(df=maternal_10_14, lgu=option_table)

        
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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_13')
            if predict_check:
                SBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                SBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                SBA_10_14(df=maternal_10_14, lgu=option_table)
                SBA_15_19(df=maternal_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2a, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2a, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_14')
            if predict_check:
                TBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                TBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                TBA_10_14(df=maternal_10_14, lgu=option_table)
                TBA_15_19(df=maternal_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2a, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2a, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=maternal_10_14, lgu=option_table)
            Others_15_19(df=maternal_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=maternal_10_14, lgu=option_table)
            Not_Stated_15_19(df=maternal_10_14, lgu=option_table)

        
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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_15')
            if predict_check:
                SBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                SBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                SBA_10_14(df=maternal_10_14, lgu=option_table)
                SBA_15_19(df=maternal_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2a, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2a, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_16')
            if predict_check:
                TBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                TBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                TBA_10_14(df=maternal_10_14, lgu=option_table)
                TBA_15_19(df=maternal_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2a, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2a, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=maternal_10_14, lgu=option_table)
            Others_15_19(df=maternal_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=maternal_10_14, lgu=option_table)
            Not_Stated_15_19(df=maternal_10_14, lgu=option_table)

        
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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_17')
            if predict_check:
                SBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                SBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                SBA_10_14(df=maternal_10_14, lgu=option_table)
                SBA_15_19(df=maternal_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2a, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2a, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_18')
            if predict_check:
                TBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                TBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                TBA_10_14(df=maternal_10_14, lgu=option_table)
                TBA_15_19(df=maternal_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2a, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2a, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=maternal_10_14, lgu=option_table)
            Others_15_19(df=maternal_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=maternal_10_14, lgu=option_table)
            Not_Stated_15_19(df=maternal_10_14, lgu=option_table)

        
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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_19')
            if predict_check:
                SBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                SBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                SBA_10_14(df=maternal_10_14, lgu=option_table)
                SBA_15_19(df=maternal_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2a, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2a, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_20')
            if predict_check:
                TBA_10_14_forecast(df=maternal_10_14, lgu=option_table)
                TBA_15_19_forecast(df=maternal_10_14, lgu=option_table)
            else:
                TBA_10_14(df=maternal_10_14, lgu=option_table)
                TBA_15_19(df=maternal_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2a, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2a, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=maternal_10_14, lgu=option_table)
            Others_15_19(df=maternal_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=maternal_10_14, lgu=option_table)
            Not_Stated_15_19(df=maternal_10_14, lgu=option_table)

        
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
                                        color='LGU', facet_col='LGU', facet_col_wrap=5,
                                        facet_col_spacing=0.09, template='seaborn', height=1200,
                                        trendline='ols', trendline_color_override='black',
                                        title='Adolescent Birth (10-14 years) by Birth Attendant in Samar Sites (2012-2021)')

            fig_maternal_10_14.update_layout(showlegend=False, font=dict(size=18),
                                title=dict(font=dict(size=18)))
            fig_maternal_10_14.update_traces(mode='lines')
            st.plotly_chart(fig_maternal_10_14, use_container_width=True)

        

        elif age_picker == '15-19 Years':
            

            fig_maternal_15_19 = px.scatter(maternal_15_19, x='Year',
                                        y=option_maternal_10_19,
                                        color='LGU', facet_col='LGU', facet_col_wrap=5,
                                        facet_col_spacing=0.09, template='seaborn', height=1200,
                                        trendline='ols', trendline_color_override='black',
                                        title='Adolescent Birth (15-19 years) by Birth Attendant in Samar Sites (2012-2021)')

            fig_maternal_15_19.update_layout(showlegend=False, font=dict(size=18),
                                title=dict(font=dict(size=18)))
            fig_maternal_15_19.update_traces(mode='lines')
            fig_maternal_15_19.update_yaxes(title_font=dict(size=20))
            fig_maternal_15_19.update_xaxes(title_font=dict(size=20))
            

            st.plotly_chart(fig_maternal_15_19, use_container_width=True)



#### Combined Age Group

SBA_bar_10_19(df=maternal_all, lgu='Samar', yrange=[0, 1200])
SBA_pct_bar_10_19(df=maternal_all, lgu='Samar')
TBA_bar_10_19(df=maternal_all, lgu='Samar', yrange=[0, 1200])
TBA_pct_bar_10_19(df=maternal_all, lgu='Samar')





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


occurrence_10_14 = ind2b.loc[ind2b['Age Range']=='10 to 14',:]


occurrence_15_19 = ind2b.loc[ind2b['Age Range']=='15 to 19',:]


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
                    title='Adolescent Birth (10-14 years) by Birth Attendant in Samar Sites (2012-2021)')
        
        fig_graph2_15_19_all = px.scatter(occurrence_15_19_all, x='Year', y='Percent SBA', template='seaborn',
                    trendline='ols', trendline_color_override='black',
                    title='Adolescent Birth (15-19 years) by Birth Attendant in Samar Sites (2012-2021)')
        

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
                    
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_21')
            if predict_check:
                SBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                SBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                SBA_10_14(df=occurrence_10_14, lgu=option_table)
                SBA_15_19(df=occurrence_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2b, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2b, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_22')
            if predict_check:
                TBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                TBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                TBA_10_14(df=occurrence_10_14, lgu=option_table)
                TBA_15_19(df=occurrence_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2b, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2b, lgu=option_table)
                
                
        elif graph == 'Others':
            Others_10_14(df=occurrence_10_14, lgu=option_table)
            Others_15_19(df=occurrence_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=occurrence_10_14, lgu=option_table)
            Not_Stated_15_19(df=occurrence_10_14, lgu=option_table)

        
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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_23')
            if predict_check:
                SBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                SBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                SBA_10_14(df=occurrence_10_14, lgu=option_table)
                SBA_15_19(df=occurrence_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2b, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2b, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_24')
            if predict_check:
                TBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                TBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                TBA_10_14(df=occurrence_10_14, lgu=option_table)
                TBA_15_19(df=occurrence_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2b, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2b, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=occurrence_10_14, lgu=option_table)
            Others_15_19(df=occurrence_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=occurrence_10_14, lgu=option_table)
            Not_Stated_15_19(df=occurrence_10_14, lgu=option_table)

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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_25')
            if predict_check:
                SBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                SBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                SBA_10_14(df=occurrence_10_14, lgu=option_table)
                SBA_15_19(df=occurrence_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2b, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2b, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_26')
            if predict_check:
                TBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                TBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                TBA_10_14(df=occurrence_10_14, lgu=option_table)
                TBA_15_19(df=occurrence_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2b, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2b, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=occurrence_10_14, lgu=option_table)
            Others_15_19(df=occurrence_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=occurrence_10_14, lgu=option_table)
            Not_Stated_15_19(df=occurrence_10_14, lgu=option_table)


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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_27')
            if predict_check:
                SBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                SBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                SBA_10_14(df=occurrence_10_14, lgu=option_table)
                SBA_15_19(df=occurrence_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2b, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2b, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_28')
            if predict_check:
                TBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                TBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                TBA_10_14(df=occurrence_10_14, lgu=option_table)
                TBA_15_19(df=occurrence_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2b, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2b, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=occurrence_10_14, lgu=option_table)
            Others_15_19(df=occurrence_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=occurrence_10_14, lgu=option_table)
            Not_Stated_15_19(df=occurrence_10_14, lgu=option_table)

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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_29')
            if predict_check:
                SBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                SBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                SBA_10_14(df=occurrence_10_14, lgu=option_table)
                SBA_15_19(df=occurrence_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2b, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2b, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_30')
            if predict_check:
                TBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                TBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                TBA_10_14(df=occurrence_10_14, lgu=option_table)
                TBA_15_19(df=occurrence_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2b, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2b, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=occurrence_10_14, lgu=option_table)
            Others_15_19(df=occurrence_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=occurrence_10_14, lgu=option_table)
            Not_Stated_15_19(df=occurrence_10_14, lgu=option_table)

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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_31')
            if predict_check:
                SBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                SBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                SBA_10_14(df=occurrence_10_14, lgu=option_table)
                SBA_15_19(df=occurrence_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2b, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2b, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_32')
            if predict_check:
                TBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                TBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                TBA_10_14(df=occurrence_10_14, lgu=option_table)
                TBA_15_19(df=occurrence_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2b, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2b, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=occurrence_10_14, lgu=option_table)
            Others_15_19(df=occurrence_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=occurrence_10_14, lgu=option_table)
            Not_Stated_15_19(df=occurrence_10_14, lgu=option_table)

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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_33')
            if predict_check:
                SBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                SBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                SBA_10_14(df=occurrence_10_14, lgu=option_table)
                SBA_15_19(df=occurrence_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2b, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2b, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_34')
            if predict_check:
                TBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                TBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                TBA_10_14(df=occurrence_10_14, lgu=option_table)
                TBA_15_19(df=occurrence_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2b, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2b, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=occurrence_10_14, lgu=option_table)
            Others_15_19(df=occurrence_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=occurrence_10_14, lgu=option_table)
            Not_Stated_15_19(df=occurrence_10_14, lgu=option_table)

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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_35')
            if predict_check:
                SBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                SBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                SBA_10_14(df=occurrence_10_14, lgu=option_table)
                SBA_15_19(df=occurrence_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2b, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2b, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_36')
            if predict_check:
                TBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                TBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                TBA_10_14(df=occurrence_10_14, lgu=option_table)
                TBA_15_19(df=occurrence_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2b, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2b, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=occurrence_10_14, lgu=option_table)
            Others_15_19(df=occurrence_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=occurrence_10_14, lgu=option_table)
            Not_Stated_15_19(df=occurrence_10_14, lgu=option_table)

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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_37')
            if predict_check:
                SBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                SBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                SBA_10_14(df=occurrence_10_14, lgu=option_table)
                SBA_15_19(df=occurrence_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2b, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2b, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_38')
            if predict_check:
                TBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                TBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                TBA_10_14(df=occurrence_10_14, lgu=option_table)
                TBA_15_19(df=occurrence_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2b, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2b, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=occurrence_10_14, lgu=option_table)
            Others_15_19(df=occurrence_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=occurrence_10_14, lgu=option_table)
            Not_Stated_15_19(df=occurrence_10_14, lgu=option_table)

        
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
        if graph == 'SBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_39')
            if predict_check:
                SBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                SBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                SBA_10_14(df=occurrence_10_14, lgu=option_table)
                SBA_15_19(df=occurrence_15_19, lgu=option_table)
                SBA_bar_10_19(df=ind2b, lgu=option_table)
                SBA_pct_bar_10_19(df=ind2b, lgu=option_table)

        elif graph == 'TBA':
            predict_check = st.checkbox('Click to see forecast up to 2026', key='checkbox_40')
            if predict_check:
                TBA_10_14_forecast(df=occurrence_10_14, lgu=option_table)
                TBA_15_19_forecast(df=occurrence_10_14, lgu=option_table)
            else:
                TBA_10_14(df=occurrence_10_14, lgu=option_table)
                TBA_15_19(df=occurrence_10_14, lgu=option_table)
                TBA_bar_10_19(df=ind2b, lgu=option_table)
                TBA_pct_bar_10_19(df=ind2b, lgu=option_table)
                
        elif graph == 'Others':
            Others_10_14(df=occurrence_10_14, lgu=option_table)
            Others_15_19(df=occurrence_10_14, lgu=option_table)

        elif graph == 'Not Stated':
            Not_Stated_10_14(df=occurrence_10_14, lgu=option_table)
            Not_Stated_15_19(df=occurrence_10_14, lgu=option_table)


        
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
                                        color='LGU', facet_col='LGU', facet_col_wrap=5,
                                        facet_col_spacing=0.09, template='seaborn', height=1200,
                                        trendline='ols', trendline_color_override='black',
                                        title='Adolescent Birth (10-14 years) by Place of Occurrence in UN-KOICA Sites (2012-2021)')

                
            fig_occurrence_10_14.update_layout(showlegend=False, font=dict(size=18),
                                title=dict(font=dict(size=18)))
            fig_occurrence_10_14.update_traces(mode='lines')
           
            st.plotly_chart(fig_occurrence_10_14, use_container_width=True)
        


        elif age_picker_occ == '15-19 Years':


            fig_occurrence_15_19 = px.scatter(occurrence_15_19, x='Year',
                                        y=option_occurrence_10_19,
                                        color='LGU', facet_col='LGU', facet_col_wrap=5,
                                        facet_col_spacing=0.09, template='seaborn', height=1200,
                                        trendline='ols', trendline_color_override='black',
                                        title='Adolescent Birth (15_19 years) by Place of Occurrence in UN-KOICA Sites (2012-2021)')

                
            fig_occurrence_15_19.update_layout(showlegend=False, font=dict(size=18),
                                title=dict(font=dict(size=18)))
            fig_occurrence_15_19.update_traces(mode='lines')
            fig_occurrence_15_19.update_yaxes(title_font=dict(size=20))
            fig_occurrence_15_19.update_xaxes(title_font=dict(size=20))
            
            st.plotly_chart(fig_occurrence_15_19, use_container_width=True)




#### Combined Age Group

SBA_bar_10_19(df=occurrence_all, lgu='Samar', yrange=[0, 1200])
SBA_pct_bar_10_19(df=occurrence_all, lgu='Samar')
TBA_bar_10_19(df=occurrence_all, lgu='Samar', yrange=[0, 1200])
TBA_pct_bar_10_19(df=occurrence_all, lgu='Samar')

