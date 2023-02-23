# @Project:     LearnML
# @Filename:    linear_regression_page.py
# @Author:      Daksh
# @Time:        09-12-2022 11:52 pm

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
from src.component.page_layout import create_page_layout
import dash_bootstrap_components as dbc
from src.component.page_order import page_order
from content.linear_regression import content

dash.register_page(__name__, title="Linear Regression", name="Linear Regression",
                   order=page_order["linear_regression_page"])
df = px.data.tips()
learn = dbc.Container([dcc.Markdown(content, dangerously_allow_html=True, mathjax=True)])
play = dbc.Container(html.Div(
    [
        dbc.Row([
            dbc.Col(
                [
                    html.Img(src='assets/smoking2.jpg')
                ], width=4
            ),
            dbc.Col(
                [
                    dcc.RadioItems(df.day.unique(), id='day-choice', value='Sat')
                ], width=6
            )
        ]),
        dbc.Row([
            dbc.Col(
                [
                    dcc.Graph(id='bar-fig',
                              figure=px.bar(df, x='smoker', y='total_bill'))
                ], width=12
            )
        ])
    ]
))


@callback(
    Output('bar-fig', 'figure'),
    Input('day-choice', 'value')
)
def update_graph(value):
    dff = df[df.day == value]
    fig = px.bar(dff, x='smoker', y='total_bill')
    return fig


layout = create_page_layout(learn_tab=learn, play_tab=play)
