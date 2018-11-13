import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from queries import *


app = dash.Dash(__name__)
app.layout = html.Div([
dcc.Dropdown(
    id = 'races-by-country',
    options=
        list(map(lambda c: {'label': c, 'value': race_count_by_country(c)}, countries())),
    value='pick a country!!!'),
    html.Div(id='output-container')
])

@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('races-by-country', 'value')])
def update_output(value):
    data = [
        {
            'values': [[10,90],[5, 95],[15,85],[20,80]],
            'type': 'pie',
        },
    ]

    return html.Div([
        dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            }
        )
    ])
