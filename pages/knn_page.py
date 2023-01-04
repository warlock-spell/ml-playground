# @Project:     LearnML
# @Filename:    knn_page.py
# @Author:      Daksh
# @Time:        10-12-2022 12:19 am

import dash
from dash import dcc, html, callback, Output, Input
from src.component.page_layout import create_page_layout
import dash_bootstrap_components as dbc
from src.component.page_order import page_order
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import plotly.express as px

dash.register_page(__name__, title="Knn", name="Knn", order=page_order["knn_page"])
learn = dbc.Container("Hello")

# load dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

test_percent_knn = html.Div([html.H4("Choose percentage of test data to split: "),
                             dbc.RadioItems(id="test-percent-knn",
                                            options=[
                                                {'label': '10 %', 'value': 0.1},
                                                {'label': '20 %', 'value': 0.2},
                                                {'label': '30 %', 'value': 0.3}
                                            ],
                                            value=0.2, inline=True)])

def split_dataset(test_percent):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1234
    )
    return [X_train, X_test, y_train, y_test]

choose_k = html.Div([html.H4("Choose value of K: "),
                     dbc.RadioItems(id="k-value-radio-items",
                                    options=[
                                        {'label': 'Value of K: 3', 'value': 3},
                                        {'label': 'Value of K: 5', 'value': 5},
                                        {'label': 'Value of K: 7', 'value': 7}
                                    ],
                                    value=3, inline=True)])

# fig = px.scatter(id="graph",
#                  x=X[:, 0], y=X[:, 1], )
# fig.show()


# @callback(
#     Output("graph", "figure"),
#     Input("test-percent-knn", "value"),
# )
# def modify_legend(test_percent_knn):
#     data = split_dataset(test_percent_knn)
#     fig = px.scatter(
#         id="graph",
#         x=X[:, 0], y=X[:, 1],
#         text="country",
#         log_x=True,
#         size_max=60,
#         title="GDP and Life Expectancy (Americas, 2007)",
#     )
#     fig.update_traces(textposition=f"{pos_y} {pos_x}")
#     return fig


play = dbc.Container(html.Div([
    test_percent_knn,
    choose_k,
]))

layout = create_page_layout(learn_tab=learn, play_tab=play)
