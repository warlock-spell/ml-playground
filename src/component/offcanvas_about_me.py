# @Project:     LearnML
# @Filename:    offcanvas_about_me.py
# @Author:      Daksh
# @Time:        10-12-2022 12:30 pm

from dash import html, Dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from src.component import ids


def render_offcanvas(app: Dash) -> html.Div:
    offcanvas = html.Div(
            [
                dbc.Button(
                    "About Me",
                    id=ids.ABOUT_ME,
                    n_clicks=0,
                ),
                dbc.Offcanvas(
                    html.P("The contents on the main page are now scrollable."),
                    id=ids.OFFCANVAS_SCROLLABLE,
                    scrollable=True,
                    title="About Me",
                    is_open=False,
                ),
            ]
        )

    @app.callback(
        Output(ids.OFFCANVAS_SCROLLABLE, "is_open"),
        Input(ids.ABOUT_ME, "n_clicks"),
        State(ids.OFFCANVAS_SCROLLABLE, "is_open"),
    )
    def toggle_offcanvas_scrollable(n1, is_open):
        if n1:
            return not is_open
        return is_open

    return offcanvas

