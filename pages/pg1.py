import pandas as pd
import json
import dash
from dash import dcc,html, callback
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc


dash.register_page(__name__, name = "Table")

# page 1

layout = html.Div([
    html.H1("Titre page 1",style = {"textAlign":"center"}),
    dcc.Dropdown(id = 'produit1',options = [{'label':'crocro','value':'crocro'}], value = 'crocro',placeholder="Choisir un produit", style = {'color': '#003366'}),
    dcc.Graph(id = "graphe1")
])

@callback(
    Output("graphe1","figure"),
    Input("produit1","children")
)

def afficher_p1(produit1):
    return None