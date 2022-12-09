# @Project:     LearnML
# @Filename:    main_layout.py
# @Author:      Daksh
# @Time:        09-12-2022 04:43 pm

import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from src.component import ids

# figure templates
template_theme1 = "sketchy"
template_theme2 = "cyborg"

# themes
url_theme1 = dbc.themes.SKETCHY
url_theme2 = dbc.themes.DARKLY


def create_layout(app: dash.Dash) -> dbc.Container:
    sidebar = dbc.Nav(
        [
            dbc.NavLink(
                [
                    dash.html.Div(page["name"], className="ms-2"),
                ],
                href=page["path"],
                # "exact" to automatically set the active property when the current pathname matches the href
                active="exact",
            )
            for page in dash.page_registry.values()
        ],
        vertical=True,
        pills=True,

        class_name="bg-light",
    )

    offcanvas = dash.html.Div(
        [
            dbc.Button(
                "About Me",
                id=ids.ABOUT_ME,
                n_clicks=0,
            ),
            dbc.Offcanvas(
                dash.html.P("The contents on the main page are now scrollable."),
                id="offcanvas-scrollable",
                scrollable=True,
                title="About Me",
                is_open=False,
            ),
        ]
    )

    @app.callback(
        dash.Output("offcanvas-scrollable", "is_open"),
        dash.Input(ids.ABOUT_ME, "n_clicks"),
        dash.State("offcanvas-scrollable", "is_open"),
    )
    def toggle_offcanvas_scrollable(n1, is_open):
        if n1:
            return not is_open
        return is_open

    return dbc.Container([
        dbc.Row([
            dbc.Col([offcanvas], align="end"),
            dbc.Col([
                     dash.html.Div("Learn ML in an interactive way",
                                   style={'fontSize': 50, 'textAlign': 'center'}),
                     ], align="center"),
            dbc.Col([ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2])], align="end"),

        ], justify="evenly"),

        dash.html.Hr(),

        dbc.Row(
            [
                dbc.Col(
                    [
                        sidebar
                    ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

                dbc.Col(
                    [
                        dash.page_container
                    ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
            ]
        )
    ], fluid=True)
