import pandas as pd
import json
import dash
from dash import dcc,html, callback
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
import numpy as np


dash.register_page(__name__, path = '/', name="Home")

## Données 


with open("./donnees/base_finale_lat_long.txt",'r') as file:
    dico_produits = json.load(file)

Base_produits = pd.DataFrame.from_dict(dico_produits)


fig = px.scatter_mapbox(Base_produits, lat="Latitude", lon="Longitude",zoom=4)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig.show()

nb_villes = len(pd.unique(Base_produits["Ville"]))
nb_produits = len(pd.unique(Base_produits["Nom_produit"]))
nb_magasins = len(pd.unique(Base_produits["Adresse"]))


# page 0

alerte1 = dbc.Alert([
    html.H3(str(nb_magasins), style={"color":"#ffffff"}),
    html.H5("Magasins enregistés", style={"color":"#ffffff"})
],color="#1560bd")

alerte2 = dbc.Alert([
    html.H3(str(nb_villes), style={"color":"#ffffff"}),
    html.H5("Communes", style={"color":"#ffffff"})
],color="#00cccb")

alerte3 = dbc.Alert([
    html.H3(str(nb_produits), style={"color":"#ffffff"}),
    html.H5("Produits analysés", style={"color":"#ffffff"})
],color="#17657d")


layout = html.Div([
    dbc.Row([
        dbc.Col([alerte1],style={"textAlign":"center"}),
        dbc.Col([alerte2],style={"textAlign":"center"}),
        dbc.Col([alerte3],style={"textAlign":"center"})
    ], style = {"padding":"1rem 1rem"}),
    dbc.Row([
        dcc.Graph(
            id = "graphe_carrefours_france",
            figure = fig,
            style={"width":"58rem","margin-left":"1rem"}
        )
    ])
])

@callback(
    Output("graphe2","figure"),
    Input("produit2","children")
)

def afficher_p2(produit2):
    return None