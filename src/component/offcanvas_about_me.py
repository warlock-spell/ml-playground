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
                "About Daksh",
                id=ids.ABOUT_ME,
                n_clicks=0,
            ),
            dbc.Offcanvas(
                [html.P(
                    "Meet Daksh - the jack of all trades and master of many. Armed with a Bachelor of Engineering in Computer Science and a Masters of Science in Data Science, he's got the brains and brawn to tackle any real-world problem. Teaching hundreds of students the ins and outs of data science has been a rewarding experience, but his real passion lies in creating content. Daksh is always on the lookout for new creative endeavors to sink his teeth into, and he's not afraid to get his hands dirty. When he's not busy slaying data dragons, you can find him tinkering with code, cooking up a storm in the kitchen, conjuring up imaginative solutions, or honing his critical thinking skills."),

                html.P(
                    "You can check out some of Daksh's cool projects on his Github page at @warlock-spell. Don't be shy, go say hi!"),],
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
