# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
# Imports from this application:
from app import app
#Imports from Google Cloud & Firebase:
import firebase_admin
from firebase_admin import credentials

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            #### **ARCHLIFE LOGIN**
            """
        ),
        dcc.Link(dbc.Button("LOGIN (COMING SOON)  ➡️", color='primary'), href='/browsing_history'),
        html.Br(),
        html.Br(),

        #cred = credentials.Certificate("path/to/serviceAccountKey.json")
        #firebase_admin.initialize_app(cred)
    ],
    md=6
)

column2 = dbc.Col(
    [
        #dcc.Graph(figure=fig)
        html.Img(src='assets/Archlife-Intro-App-Logo-Dark.png', className='img-fluid', height=200, width=200)
    ],
    md=6
)

layout = dbc.Row([column2, column1])
