import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import classification_model as c
from dash.dependencies import Input, Output
import plotly.express as px

# Step 1. Launch the application
app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

# Step 2. Import the dataset
filepath = 'data/cleanStationsByStates.csv'
data = pd.read_csv(filepath)

for col in data.columns:
    data[col] = data[col].astype(str)

data['text'] = ('State: ' + data['State'] + '<br>' +
                "Electric Stations: " + data['Electric stations'] + '<br>' +
                "Electric Charging Outlets: " + data['Electric Charging Outlets'] + '<br>' +
                "Electric Total: " + data['Electric Total'] + '<br>' +
                "Hydrogen Total: " + data['Hydrogen Total'] + '<br>' +
                "Propane Total: " + data['Propane Total'] + '<br>')

# Step 4. Create the trend line graph
df_states = pd.read_csv('data/df_states.csv')
df = pd.read_csv('data/df_trend.csv')
dff = pd.read_csv('data/ev_brands_by_states.csv')

# Questions
user_input = []

seats = dbc.FormGroup(
    [
        dbc.Label("How many seats do you prefer?"),
        dbc.RadioItems(
            options=[
                {"label": "2", "value": 2},
                {"label": "4", "value": 4},
                {"label": "5", "value": 5},
                {"label": "6", "value": 6},
                {"label": "7", "value": 7},
            ],
            # labelCheckedStyle={"color": "red"},
            value=2,
            id="Seats",
            inline=True
        ),
    ],
)

rapid_charge = dbc.FormGroup(
    [
        dbc.Label("Do you want rapid charge capabilities?"),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": 1},
                {"label": "No", "value": 0},
            ],
            value=1,
            id="rapidCharge",
            inline=True
        ),
    ],
)

driving_range = dbc.FormGroup(
    [
        dbc.Label("What is your preferred driving range?"),
        dbc.RadioItems(
            options=[
                {"label": "50-250", "value": 0},
                {"label": "250-450", "value": 1},
                {"label": "450-650", "value": 2},
            ],
            value=0,
            id="drivingRange",
            inline=False
        ),
    ],
)

budget_range = dbc.FormGroup(
    [
        dbc.Label("What is your preferred budget range?"),
        dbc.RadioItems(
            options=[
                {"label": "0-50000", "value": 0},
                {"label": "100000-150000", "value": 1},
                {"label": "150000-200000", "value": 2},
                {"label": "200000-250000", "value": 3},
                {"label": "300000-350000", "value": 4},
            ],
            value=0,
            id="budgetRange",
            inline=False
        ),
    ],
)

inputs = html.Div(
    [
        dbc.Form([seats, rapid_charge, driving_range, budget_range]),
        html.P(id="radioitems-checklist-output"),
    ]
)

# Layout Components

header = html.Div([html.H1(children="Electric Vehicles Analysis Tool", ),
                   html.H4(children="Project by Anant Rajeev, Leena Elamrawy and Krisha Mehta",
                           style={'font-size': '20px'}),
                   ],
                  style={'font-family': 'Helvetica, sans-serif',
                         'font-size': '30px',
                         'backgroundColor': '#3aaab2',
                         'text-align': 'center',
                         'border-radius': '10px',
                         'align': 'center',
                         'margin-left': '200px',
                         'margin-right': '200px',
                         'margin-top': '30px',
                         'padding': '30px'
                         }
                  )

# Content
introduction = html.Div([html.H3("Are you looking for an Electric Vehicle?",
                                 style={'text-align': 'center'}
                                 ),
                         html.P("We are here to help with our multifaceted EV analysis and recommendation tool.\
                             We want you to understand where your state stands with regards to charging mechanisms \
                             and, furthermore, which newly developed car model can be used for a customer using the interface.",
                                className="mb-0",
                                style={'padding': '20px',
                                       'font-size': '20px',
                                       'text-align': 'justify',
                                       'text-justify': 'inter-word'
                                       })
                         ], style={'backgroundColor': '#a5d9d8', 'margin': '10px', 'padding': '10px',
                                   'border-radius': '10px'})

ev_today = html.Div([html.H3("Hesitant buying an EV?", style={'text-align': 'center'}),
                     html.P(
                         "The number of publicly accessible "
                         "charging stations reached nearly 22,000 in 2019, offering about 55,000 outlets. "
                         "You'll never be without charging station info with handy apps such as PlugShare to find "
                         "nearby charging stations. "
                         "But if you're still on the fence about whether or not to buy an electric vehicle, "
                         "you are at the right place to make an informed decision.")],
                    style={'text-align': 'justify',
                           'text-justify': 'inter-word',
                           'padding-left': '35px',
                           'padding-right': '30px',
                           'font-size': '20px',
                           'backgroundColor': '#a5d9d8',
                           'margin': '10px',
                           'padding': '10px',
                           'border-radius': '10px'})

ques_before_buy = html.Div([html.H3("Questions you should ask before buying an EV!", style={'text-align': 'center'}),
                            html.P("Does the Car Have Enough Range? \n Can I Charge My Electric Vehicle at Home? \n "
                                   "Are There Public Charging Stations Nearby? \n What are the most commonly bought "
                                   "cars in your state?"),
                            html.P(
                                "Below are some graphs and a recommendation system that will answer these questions!")],
                           style={'text-align': 'justify',
                                  'text-justify': 'inter-word',
                                  'font-size': '20px',
                                  'padding-left': '35px',
                                  'padding-right': '30px',
                                  'backgroundColor': '#a5d9d8',
                                  'margin': '10px',
                                  'padding': '10px',
                                  'border-radius': '10px'},
                           )

rowbleh = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(introduction),
                dbc.Col(ev_today),
                dbc.Col(ques_before_buy),
            ]
        ),
    ]
)

why_recommend = html.H3("Let us help you in finding the perfect EV that will suit your requirements. "
                        "Select the specifications of your EV!",
                        style={'font-family': 'Helvetica, sans-serif',
                               'backgroundColor': '#3aaab2',
                               'text-align': 'center',
                               'border-radius': '10px',
                               'align': 'center',
                               'margin-left': '200px',
                               'margin-right': '200px',
                               'margin-top': '30px',
                               'padding': '30px'})

# graphs
line_graph = dcc.Graph(id="line_graph",
                       config={"displayModeBar": False},
                       figure={"data": [
                           {
                               "x": df["Year"],
                               "y": df["Number of Electric Vehicles"],
                               "type": "lines",
                               "hovertemplate": "%{y:.2f}",
                           },
                       ],
                           "layout": {
                               "title": {
                                   "text": "Changes in the Number of Electric Vehicles Over Time: 1999-2019",
                                   "x": 0.05,
                                   "xanchor": "left",
                               },
                               "xaxis": {"fixedrange": True},
                               "yaxis": {
                                   "fixedrange": True,
                               },
                               "colorway": ["#17B897"],
                           },
                       },
                       style={'width': '48%', 'display': 'inline-block'}
                       )

fig = go.Figure(data=go.Choropleth(
    locations=data['code'],  # Spatial coordinates
    z=data['Total'],  # Data to be color-coded
    locationmode='USA-states',  # set of locations match entries in `locations`
    colorscale='teal',
    marker_line_color='white',
    text=data['text']
))

fig = fig.update_layout(title_text='Charging Stations By State (Hover for breakdown)',
                        geo=dict(
                            scope='usa',
                            showlakes=False
                        ))

map_graph = dcc.Graph(id='plot2',
                      figure=fig,
                      style={'width': '48%', 'display': 'inline-block'}
                      )

fig3 = px.line(x="Year", y="Count", data_frame=df_states, color='State', title='Electric Vehicle Trend Per State')

line_graph_states = dcc.Graph(id='line_chart_states',
                              figure=fig3,
                              style={'width': '48%', 'display': 'inline-block', 'align': 'right'},
                              )

checklist_states = html.Div([
    dcc.Checklist(
        id="checklist",
        options=[
            {'label': 'Oregon', 'value': 'Oregon'},
            {'label': 'Virginia', 'value': 'Virginia'},
            {'label': 'Montana', 'value': 'Montana'},
            {'label': 'Vermont', 'value': 'Vermont'},
            {'label': 'Minnesota', 'value': 'Minnesota'},
            {'label': 'California', 'value': 'California'},
            {'label': 'Colorado', 'value': 'Colorado'},
            {'label': 'Washington', 'value': 'Washington'},
            {'label': 'Connecticut', 'value': 'Connecticut'},
            {'label': 'New York', 'value': 'New York'},
            {'label': 'Connecticut', 'value': 'Connecticut'},
            {'label': 'Michigan', 'value': 'Michigan'},
            {'label': 'New Jersey', 'value': 'New Jersey'},
            {'label': 'Florida', 'value': 'Florida'},
            {'label': 'Wisconson', 'value': 'Wisconson'},
        ],
        value=df_states[3:],

        labelStyle={'display': 'inline-block'},
    )
    ,
    dcc.Graph(id="line-chart")
    # line_graph_states
])

interactive_line_state_car = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(id='chosen_state',
                         options=[{'label': i, 'value': i} for i in dff.State.unique()
                                  ],
                         value='States',
                         multi=False,
                         clearable=False
                         ),
        ], className='six columns'),
    ], style={'width': '48%', 'display': 'inline-block', 'align': 'left'}),

    html.Div([
        html.Div([
            dcc.Dropdown(id='chosen_brand_model',
                         options=[{'label': i, 'value': i} for i in dff['Brand and Model'].unique()
                                  ],
                         value='Brand and Model of EV',
                         multi=False,
                         clearable=False
                         ),
        ]
            , className='six columns'),
    ], style={'width': '48%', 'display': 'inline-block', 'align': 'right'}),
    html.Div([
        html.Div([
            dcc.Graph(id='linechart'),
        ]),
    ], className='row'),
],
    style={'width': '48%', 'display': 'inline-block', 'align': 'right'}
)

# question-form
questions_form = dbc.Col([
    dbc.Row(inputs),
],
    style={
        'text-align': 'justify',
        'text-justify': 'inter-word',
        'padding': '30px',
        'border-radius': '10px',
        'font-size': '20px',
        'margin-left': '350px',
        'margin-right': '300px',
        'backgroundColor': '#d0eeea',
        'display': 'inline-block',
        'align': 'left',
        'width': '48%'}
)

# submit_button = html.Button('Submit', id='button')

# recommendation_form = html.Div([questions_form],
#                                style={
#
#                                })

app.layout = html.Div(children=[
    header,
    rowbleh,
    html.Div(children=[
        line_graph,
        line_graph_states,
        map_graph,
        interactive_line_state_car
    ]),
    why_recommend,
    questions_form
])


@app.callback(
    Output("radioitems-checklist-output", "children"),
    [
        Input("Seats", "value"),
        Input("rapidCharge", "value"),
        Input("drivingRange", "value"),
        Input("budgetRange", "value"),
        # Input('button', 'n_clicks'),
        # Input('chosen_brand_model', 'value'),
        # Input('chosen_state', 'value')
    ]
)
def on_form_change(seats_value, rapidCharge_value, drivingRange_value, budgetRange_value):
    results = [seats_value, rapidCharge_value, drivingRange_value, budgetRange_value]

    if len(results) == 4:
        predicted_EV = c.build_knn_model(results)
        EV = c.recommended_EV(predicted_EV)
        EV_stats = c.get_EV_stats(EV)
        a = str(EV_stats)
        final_ev_stats = ''.join(a)

    table_header = [
        html.Thead(html.Tr([html.Th("Your Recommended EV is:"), html.Th(EV)]))
    ]

    row1 = html.Tr([html.Td("Brand"), html.Td(EV_stats[1])])
    row2 = html.Tr([html.Td("Model"), html.Td(EV_stats[2])])
    row3 = html.Tr([html.Td("AccelSec"), html.Td(EV_stats[3])])
    row4 = html.Tr([html.Td("Efficiency_WhKm"), html.Td(EV_stats[4])])
    row5 = html.Tr([html.Td("FastCharge_KmH"), html.Td(EV_stats[5])])
    row6 = html.Tr([html.Td("RapidCharge"), html.Td(EV_stats[6])])
    row7 = html.Tr([html.Td("PowerTrain"), html.Td(EV_stats[7])])
    row8 = html.Tr([html.Td("PlugType"), html.Td(EV_stats[8])])
    row9 = html.Tr([html.Td("BodyStyle"), html.Td(EV_stats[9])])
    row10 = html.Tr([html.Td("Segment"), html.Td(EV_stats[10])])
    row11 = html.Tr([html.Td("Seats"), html.Td(EV_stats[11])])
    row12 = html.Tr([html.Td("TopSpeed_mph"), html.Td(EV_stats[13])])
    row13 = html.Tr([html.Td("Range_Mi"), html.Td(EV_stats[14])])
    row14 = html.Tr([html.Td("EV Price"), html.Td(EV_stats[15])])

    table_body = [
        html.Tbody([row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14])]

    table = dbc.Table(table_header + table_body,
                      style={'width': '650px', 'font-size': '14px', 'height': '20px'},
                      bordered=True,
                      # dark=True,
                      hover=True,
                      responsive=True,
                      striped=True)

    image = dbc.Card(
        [
            dbc.CardBody(html.P("Here is an image of your recommended EV!"), style={'backgroundColor': '#d0eeea'}),
            dbc.CardImg(src="assets/bmw-i4.png", bottom=True, style={"width": "650px"}, ),
        ]
    )

    recommendation = html.Div([table, image], style={'layout': 'inline-block', 'align': 'right'})
    return recommendation

    # if n_clicks:
    #     return table, image
    # else:
    #     return None


@app.callback(
    Output('linechart', 'figure'),
    [Input('chosen_brand_model', 'value'),
     Input('chosen_state', 'value')])
def update_data(chosen_brand_model, chosen_state):
    state_filter = dff[dff['State'] == chosen_state]
    brand_model_filter = state_filter[state_filter['Brand and Model'] == chosen_brand_model]

    line_chart = px.line(
        data_frame=brand_model_filter,
        x='year',
        y='Count',
        title='Changes in the number of <b>{} cars in {} Over Time'.format(chosen_brand_model, chosen_state)
    )

    line_chart.update_traces(mode='lines+markers')

    line_chart.update_xaxes(showgrid=False)

    # line_chart.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})

    return line_chart


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
