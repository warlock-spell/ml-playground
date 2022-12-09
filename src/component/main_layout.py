# @Project:     LearnML
# @Filename:    main_layout.py
# @Author:      Daksh
# @Time:        09-12-2022 04:43 pm

import dash
import dash_bootstrap_components as dbc


def create_layout(app: dash.Dash) -> dbc.Container:
    sidebar = dbc.Nav(
        [
            dbc.NavLink(
                [
                    dash.html.Div(page["name"], class_name="ms-2"),
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

    return dbc.Container([
        dbc.Row([
            dbc.Col(dash.html.Div("Learn ML in an interactive way",
                                  style={'fontSize': 50, 'textAlign': 'center'}))
        ]),

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
