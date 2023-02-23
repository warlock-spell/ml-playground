# @Project:     LearnML
# @Filename:    home.py
# @Author:      Daksh
# @Time:        10-12-2022 12:24 am

import dash
from dash import dcc, html
from src.component.page_order import page_order
from src.content.home import content
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=page_order["home"])

layout = html.Div(dbc.Container([dcc.Markdown(content, dangerously_allow_html=True, mathjax=True)]))
