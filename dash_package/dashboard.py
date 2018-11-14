import dash
import dash_core_components as dcc
import dash_html_components as html

from dash_package import app

from dash.dependencies import Input, Output, State
from dash_package.chart_data import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#003300',
    'text': '#77B300'
}

def generate_piecharts(value):
    data = [{'values': value['y'], 'labels': value['x'], 'type': 'pie'}]
    return html.Div([dcc.Graph(
        id='graph',
        figure={
            'data': data,
            'layout': {
                'margin': {'l': 10,'r': 10,'b': 30,'t': 30},
                'legend': {'x': 1, 'y': 1}
            }})])


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1('Alchemy Has No Negative Side Effects!!!!', style={'textAlign': 'center', 'color': colors['text']}),

    html.H6('a data science project!!!', style={'color': '#003300', 'backgroundColor': '#ffffff', 'textAlign': 'center'}),

    html.H3('Cannabis Races by Country', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='races-by-countries',
        figure={
            'data':[
                {'x': country_race_composition['countries'], 'y': country_race_composition['sativas'], 'type': 'bar', 'name': 'sativas'},
                {'x': country_race_composition['countries'], 'y': country_race_composition['indicas'], 'type': 'bar', 'name': 'indicas'},
                {'x': country_race_composition['countries'], 'y': country_race_composition['hybrids'], 'type': 'bar', 'name': 'hybrids'}
            ],
            'layout': [{
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }]
        }
    ),

    html.H3('Pie Charts: Race Composition of Cannabis Strains by Country', style={'textAlign': 'center', 'color': colors['text']}),

    html.Div([
        dcc.Dropdown(
            id='races-by-country',
            options=list(map(lambda c: {'label': c, 'value': race_count_by_country(c)}, countries())),
            value=race_count_by_country('Afghanistan')
        ),
        html.Div(id='output-races')
    ]),


    html.H3('Pie Charts of Cannabis Flavors by Country', style={'textAlign': 'center','color': colors['text']
    }),

    html.Div([
        dcc.Dropdown(
            id='flavors-by-country',
            options=list(map(lambda c: {'label': c, 'value': Countries.flavor_count_by_country(c)}, Countries.countries())),
            value=Countries.flavor_count_by_country('Afghanistan')
        ),
        html.Div(id='output-flavors')
    ]),

    html.H3('Pie Charts of Cannabis Effects by Country', style={'textAlign': 'center','color': colors['text']
    }),

    html.Div([
        dcc.Dropdown(
            id='effects-by-country',
            options=list(map(lambda c: {'label': c, 'value': Countries.effect_count_by_country(c)}, Countries.countries())),
            value=Countries.effect_count_by_country('Afghanistan')
        ),
        html.Div(id='output-effects')
    ])


    #NEW GRAPH HERE!!!!
])



@app.callback(Output('output-races', 'children'),
              [Input('races-by-country', 'value')])
def display_race_content(value):
    return generate_piecharts(value)

# @app.callback(Output('output-flavors', 'children'),
#               [Input('flavors-by-country', 'value')])
# def display_flavor_content(value):
#     return generate_piecharts(value)
#
# @app.callback(Output('output-effects', 'children'),
#               [Input('effects-by-country', 'value')])
# def display_effect_content(value):
#     return generate_piecharts(value)
