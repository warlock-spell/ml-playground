# @Project:     LearnML
# @Filename:    linear_regression_page.py
# @Author:      Daksh
# @Time:        09-12-2022 11:52 pm

import dash
from src.component.page_layout import create_page_layout
import dash_bootstrap_components as dbc

dash.register_page(__name__)

learn=dbc.Container("Hello")
play=dbc.Container("play")

layout = create_page_layout(learn_tab=learn, play_tab=play)