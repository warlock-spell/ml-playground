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
from content.knn import content
import plotly.graph_objects as go
from src.component import ids
from algorithm.knn import KNN

dash.register_page(__name__, title="Knn", name="Knn", order=page_order["knn_page"])

learn = dbc.Container([dcc.Markdown(content, dangerously_allow_html=True, mathjax=True)])

# load dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target


def split_dataset(test_percent):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_percent, random_state=1234
    )
    return X_train, X_test, y_train, y_test


def plot_fig(X, y, cmap=["#FF0000", "#00FF00", "#0000FF"]):
    scatter = go.Scatter(x=X[:, 0], y=X[:, 1], mode='markers',
                         marker=dict(size=10, color=y, colorscale=cmap, line=dict(color='black', width=1)))
    fig = go.Figure(data=scatter)
    return fig


# select test percent
test_percent_knn = html.Div([html.H4("Choose percentage of test data to split: "),
                             dbc.RadioItems(id=ids.KNN_SELECT_TEST_SIZE,
                                            options=[
                                                {'label': '10 %', 'value': 0.1},
                                                {'label': '20 %', 'value': 0.2},
                                                {'label': '30 %', 'value': 0.3}
                                            ],
                                            value=0.2, inline=True), html.Br()])

# select k value
choose_k = html.Div([html.H4("Choose value of K: "),
                     dbc.RadioItems(id=ids.KNN_SELECT_K_VALUE,
                                    options=[
                                        {'label': 'Value of K: 3', 'value': 3},
                                        {'label': 'Value of K: 5', 'value': 5},
                                        {'label': 'Value of K: 7', 'value': 7}
                                    ],
                                    value=5, inline=True),
                     html.Br()])

# graph component
knn_graph = html.Div([
    dbc.Label("Dataset Figure:"),
    dcc.Graph(figure=plot_fig(X, y), id=ids.KNN_GRAPH_VIZ),
    html.Br(),
])

# accuracy
show_accuracy = html.Div(
    [
        html.P("The accuracy obtained is:"),
        html.Br(),
        html.P(id=ids.KNN_SHOW_ACCURACY),
        html.Br(),
    ]
)


@callback(
    Output(ids.KNN_SHOW_ACCURACY, "children"),
    Input(ids.KNN_SELECT_TEST_SIZE, "value"),
    Input(ids.KNN_SELECT_K_VALUE, "value"),
)
def modify_legend(test_percent_knn, k_value):
    X_train, X_test, y_train, y_test = split_dataset(test_percent_knn)
    clf = KNN(k=k_value)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)

    acc = np.sum(predictions == y_test) / len(y_test)
    return f"{acc * 100:.12f} %"


play = dbc.Container(html.Div([
    test_percent_knn,
    html.Br(),
    choose_k,
    html.Br(),
    knn_graph,
    html.Br(),
    show_accuracy,
    html.Br(),
]))

layout = create_page_layout(learn_tab=learn, play_tab=play)
