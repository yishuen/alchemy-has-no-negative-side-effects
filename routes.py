from flask import render_template

from dash_package.listing import Listing
from dash_package import server

@server.route('/')
def render_apartments():
    pass
