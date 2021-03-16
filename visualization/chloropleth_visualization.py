import plotly.express as px
# Save a copy of the data frame. This will hold all values as ints
dataCopy = data.copy()

for col in data.columns:
    data[col] = data[col].astype(str)

def printVisualizations(data1,data2):
  print("Please enter the 2-letter code of the state you live in or 'Total' for all states: ")
  stateChoice1 = input()
  if (stateChoice1 == 'Total'):
    import plotly.graph_objects as go

    data1['text'] = ('State: ' + data1['State'] + '<br>' +
    "Electric Stations: " + data1['Electric stations'] + '<br>' +
    "Electric Charging Outlets: " + data1['Electric Charging Outlets'] + '<br>' +
    "Electric Total: " + data1['Electric Total'] + '<br>' +
    "Hydrogen Total: " + data1['Hydrogen Total'] + '<br>' +
    "Propane Total: " + data1['Propane Total'] + '<br>')



    fig = go.Figure(data=go.Choropleth(
        locations=data1['code'], # Spatial coordinates
        z = data1['Total'], # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'teal',
        marker_line_color='white',
        text=data1['text']

    ))

    fig.update_layout(title_text = 'Charging Stations By State (Hover for breakdown)',
                      geo = dict(
                          scope='usa',
                          showlakes=True
                      ))

    fig.show()

  else:
    stateTotal = data2.loc[data2['code'] == stateChoice1]['Total']

    fig = px.choropleth(locations=[stateChoice1],
                        locationmode="USA-states",
                        range_color = [100, 80000],
                        color=stateTotal,
                        labels = {'color': 'Total Stations', 'locations' : 'State'},
                        scope="usa",
                        color_continuous_scale = 'teal',
                        title="Total Charging Stations in " + stateChoice1
                        )
    fig.show()

printVisualizations(data,dataCopy)
