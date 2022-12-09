# @Project:     LearnML
# @Filename:    home.py
# @Author:      Daksh
# @Time:        10-12-2022 12:24 am

import dash
from dash import dcc, html

dash.register_page(__name__, path='/')


layout = html.Div("Home")