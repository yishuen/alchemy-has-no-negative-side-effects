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
