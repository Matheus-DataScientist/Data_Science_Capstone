# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                html.Div([
                                    dcc.Dropdown(
                                        id='site-dropdown',
                                        options=[
                                            {'label':'ALL' , 'value':'ALL'},
                                            {'label':'CCAFS LC-40' , 'value':'CCAFS LC-40'},
                                            {'label':'CCAFS SLC-40' , 'value':'CCAFS SLC-40'},
                                            {'label':'VAFB SLC-4E' , 'value':'VAFB SLC-4E'},
                                            {'label':'KSC LC-39A' , 'value':'KSC LC-39A'}
                                        ],
                                        value='ALL',
                                        placeholder='Select a site',
                                        searchable=True
                                    ),
                                ]),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                marks={0: '0', 2121: '2121', 3412.5: '3412.5', 5042.5: '5042.5',  9600: '9600', 10000: '10000'},
                                                value=[0, 9600])

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site=='ALL':
        filtered_df=spacex_df[['Launch Site','class']][spacex_df['class']==1]
        data=filtered_df.groupby('Launch Site')['class'].count().reset_index()
        fig1=px.pie(data,
                   values='class',
                   names='Launch Site',
                   title='Sucess launch by site')
        return fig1
    if entered_site == 'CCAFS LC-40':
        filtered_df=spacex_df[['Launch Site', 'class']][spacex_df['Launch Site']=='CCAFS LC-40']
        data=filtered_df.groupby('class')['Launch Site'].count().reset_index()
        fig2=px.pie(data,
                   values='Launch Site',
                   names='class',
                   title='Success Launch at CCAFS LC-40')
        return fig2
    if entered_site == 'CCAFS SLC-40':
        filtered_df=spacex_df[['Launch Site', 'class']][spacex_df['Launch Site']=='CCAFS SLC-40']
        data=filtered_df.groupby('class')['Launch Site'].count().reset_index()
        fig3=px.pie(data,
                   values='Launch Site',
                   names='class',
                   title='Success Launch at CCAFS SLC-40')
        return fig3
    if entered_site=='VAFB SLC-4E':
        filtered_df=spacex_df[['Launch Site','class']][spacex_df['Launch Site']=='VAFB SLC-4E']
        data=filtered_df.groupby('class')['Launch Site'].count().reset_index()
        fig4=px.pie(data,
                    values='Launch Site',
                    names='class',
                    title='Success Launch at VAFB SLC-4E')
        return fig4
    if entered_site=='KSC LC-39A':
        filtered_df=spacex_df[['Launch Site','class']][spacex_df['Launch Site']=='KSC LC-39A']
        data=filtered_df.groupby('class')['Launch Site'].count().reset_index()
        fig5=px.pie(data,
                    values='Launch Site',
                    names='class',
                    title='Success Launch at KSC LC-39A')
        return fig5

    

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'),
              Input(component_id='payload-slider', component_property='value'))
def get_scatter_chart(entered_site, entered_payload):
    print(entered_payload)
    filtered_df=spacex_df[['Launch Site','class','Payload Mass (kg)','Booster Version']]
    if entered_site=='ALL':
            data=filtered_df[(spacex_df['Payload Mass (kg)']>= entered_payload[0]) & (spacex_df['Payload Mass (kg)']<= entered_payload[1])]
            fig_all=px.scatter(data,
                   x='Payload Mass (kg)',
                   y='class',
                   color='Booster Version',
                   title='Sucess launch by site')
            return fig_all
#Seguir a lógica colocada acima, colocando o operador & o dataframe spacex_df e ficará [(condição do launch site)&(condição do entered_payload[0])&(condição do entered_payload[1])]
    if entered_site=='CCAFS LC-40':
            data=filtered_df[spacex_df['Launch Site']=='CCAFS LC-40']
            fig_all=px.scatter(data,
                   x='Payload Mass (kg)',
                   y='class',
                   color='Booster Version',
                   title='Sucess launch by site')
            return fig_all
    if entered_site=='CCAFS SLC-40':
            data=filtered_df[spacex_df['Launch Site']=='CCAFS SLC-40']
            fig_all=px.scatter(data,
                   x='Payload Mass (kg)',
                   y='class',
                   color='Booster Version',
                   title='Sucess launch by site')
            return fig_all
    if entered_site=='VAFB SLC-4E':
            data=filtered_df[spacex_df['Launch Site']=='VAFB SLC-4E']
            fig_all=px.scatter(data,
                   x='Payload Mass (kg)',
                   y='class',
                   color='Booster Version',
                   title='Sucess launch by site')
            return fig_all
    if entered_site=='KSC LC-39A':
            data=filtered_df[spacex_df['Launch Site']=='KSC LC-39A']
            fig_all=px.scatter(data,
                   x='Payload Mass (kg)',
                   y='class',
                   color='Booster Version',
                   title='Sucess launch by site')
            return fig_all

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
