# @Project:     LearnML
# @Filename:    knn_page.py
# @Author:      Daksh
# @Time:        10-12-2022 12:19 am

import dash
from src.component.page_layout import create_page_layout
import dash_bootstrap_components as dbc
from src.component.page_order import order

dash.register_page(__name__, order=order["knn_page"])
learn = dbc.Container("Hello")
play = dbc.Container("play")

layout = create_page_layout(learn_tab=learn, play_tab=play)
