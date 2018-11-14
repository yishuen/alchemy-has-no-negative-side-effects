from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dash

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///weed.db'
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
server.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(server)

app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')

from dash_package.chart_data import *
from dash_package.models import Strain, Flavor, Effect, Country, StrainFlavor, StrainEffects, StrainCountry
from dash_package.routes import *
from dash_package.dashboard import *
