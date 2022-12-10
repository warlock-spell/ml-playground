# @Project:     LearnML
# @Filename:    nav_sidebar.py
# @Author:      Daksh
# @Time:        10-12-2022 12:47 pm

import dash_bootstrap_components as dbc
from dash import html, page_registry, Dash


def render_sidebar(app: Dash):
    sidebar = dbc.Nav(
        [
            dbc.NavLink(
                [
                    html.Div(page["name"], className="ms-2"),
                ],
                href=page["path"],
                # "exact" to automatically set the active property when the current pathname matches the href
                active="exact",
            )
            for page in page_registry.values()

        ],
        vertical=True,
        pills=True,

        class_name="bg-light",
    )

    return sidebar
