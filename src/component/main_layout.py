# @Project:     LearnML
# @Filename:    main_layout.py
# @Author:      Daksh
# @Time:        09-12-2022 04:43 pm

import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from src.component.offcanvas_about_me import render_offcanvas
from src.component.nav_sidebar import render_sidebar
from src.component import ids

# figure templates
template_theme1 = "sketchy"
template_theme2 = "cyborg"

# themes
url_theme1 = dbc.themes.SKETCHY
url_theme2 = dbc.themes.DARKLY


def create_layout(app: dash.Dash) -> dbc.Container:
    return dbc.Container([
        dbc.Row([
            dbc.Col([render_offcanvas(app)], align="end", width=1),
            dbc.Col([
                dash.html.Div("Learn ML in an interactive way",
                              style={'fontSize': 50, 'textAlign': 'center'}),
            ], align="center"),
            dbc.Col([ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2])], align="end", width=1),

        ], justify="evenly"),

        dash.html.Hr(),

        dbc.Row(
            [
                dbc.Col(
                    [
                        render_sidebar(app)
                    ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

                dbc.Col(
                    [
                        dash.page_container
                    ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
            ]
        )
    ], fluid=True)
