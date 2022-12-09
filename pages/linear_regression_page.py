# @Project:     LearnML
# @Filename:    linear_regression_page.py
# @Author:      Daksh
# @Time:        09-12-2022 11:52 pm

import dash
from dash import dcc, html
from src.component.page_layout import create_page_layout

dash.register_page(__name__)


layout = create_page_layout()