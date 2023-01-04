# @Project:     LearnML
# @Filename:    home.py
# @Author:      Daksh
# @Time:        10-12-2022 12:24 am

import dash
from dash import dcc, html
from src.component.page_order import page_order

dash.register_page(__name__, path='/', order=page_order["home"])

layout = html.Div("Home")
