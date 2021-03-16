import pandas as pd     #(version 1.0.0)
import plotly           #(version 4.5.4) pip install plotly==4.5.4
import plotly.express as px

import dash             #(version 1.9.1) pip install dash==1.9.1
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

#---------------------------------------------------------------
#Taken from https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases
#df = pd.read_excel("COVID-19-geographic-disbtribution-worldwide-2020-03-29.xlsx",engine='openpyxl')
dff = pd.read_csv('data/ev_brands_by_states.csv')
# dff = df.groupby('countriesAndTerritories', as_index=False)[['deaths','cases']].sum()
# print (dff[:5])
#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(id='linechart'),
        ]),
    ], className='row'),

    html.Div([
        html.Div([
            dcc.Dropdown(id='chosen_state',
                options=[ {'label': i, 'value': i} for i in dff.State.unique()
                ],
                value='States',
                multi=False,
                clearable=False
            ),
        ],className='six columns'),
        ]),

    html.Div([
        html.Div([
            dcc.Dropdown(id='chosen_brand_model',
                options=[ {'label': i, 'value': i} for i in dff['Brand and Model'].unique()
                ],
                value='Brand and Model of EV',
                multi=False,
                clearable=False
            ),
        ],className='six columns'),
        ]),



])


@app.callback(
    Output('linechart', 'figure'),
    [Input('chosen_brand_model', 'value'),
     Input('chosen_state', 'value')])

def update_data(chosen_brand_model,chosen_state):

    state_filter = dff[dff['State'] == chosen_state]
    brand_model_filter = state_filter[state_filter['Brand and Model'] == chosen_brand_model]


    line_chart = px.line(
            data_frame= brand_model_filter,
            x='year',
            y='Count',
            title = 'Changes in the number of <b>{} cars in {} Over Time'.format(chosen_brand_model,chosen_state)
            )

    line_chart.update_traces(mode='lines+markers')

    line_chart.update_xaxes(showgrid=False)

    #line_chart.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})



    return line_chart

def update_output(value):
    return 'You have selected "{}"'.format(value)

#------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True, port=9900)
