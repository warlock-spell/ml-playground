# @Project:     LearnML
# @Filename:    page_layout.py
# @Author:      Daksh
# @Time:        10-12-2022 02:52 am

from dash import Dash, html
import dash_bootstrap_components as dbc


def create_page_layout() -> dbc.Container:
    learn_tab = html.Div("Learn Tab")

    play_tab = html.Div("Play Tab")

    tabs = dbc.Tabs(
        [
            dbc.Tab(learn_tab, label="Learn"),
            dbc.Tab(play_tab, label="Play"),
            dbc.Tab(
                "open for extension", label="extend", disabled=True
            ),
        ]
    )

    return dbc.Container([tabs])
