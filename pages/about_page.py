# @Project:     LearnML
# @Filename:    about_page.py
# @Author:      Daksh
# @Time:        10-12-2022 12:10 am

import dash
from dash import dcc, html

dash.register_page(__name__)


layout = html.Div("About")