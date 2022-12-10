# @Project:     LearnML
# @Filename:    page_layout.py
# @Author:      Daksh
# @Time:        10-12-2022 02:52 am

from dash import Dash, html
import dash_bootstrap_components as dbc


def create_page_layout(learn_tab: dbc.Container, play_tab: dbc.Container) -> dbc.Container:

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
