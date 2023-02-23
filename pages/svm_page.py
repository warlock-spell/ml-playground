# @Project:     LearnML
# @Filename:    svm_page.py
# @Author:      Daksh
# @Time:        03-01-2023 11:01 pm

import dash
from dash import dcc, html, callback, Output, Input
from src.component.page_layout import create_page_layout
import dash_bootstrap_components as dbc
from src.component.page_order import page_order
import numpy as np
from sklearn import datasets
from algorithm.svm import SVM
from src.component import ids
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from content.svm import content

dash.register_page(__name__, title="SVM", name="SVM", order=page_order["svm_page"])
learn = dbc.Container([dcc.Markdown(content, dangerously_allow_html=True, mathjax=True)])

# Select sample size
select_sample_size = html.Div(
    [
        dbc.Label("Choose sample size"),
        dbc.RadioItems(
            options=[
                {"label": "Sample size: 50", "value": 50},
                {"label": "Sample size: 75", "value": 75},
                {"label": "Sample size: 100", "value": 100},
                {"label": "Sample size: 150", "value": 150},
            ],
            value=50,
            id=ids.SVM_SELECT_SAMPLE_SIZE,
            inline=True,
        ),
    ]
)

# Select Features
select_features = html.Div(
    [
        dbc.Label("Choose number of features"),
        dbc.RadioItems(
            options=[
                {"label": "No of features: 2", "value": 2},
                {"label": "No of features: 3 (coming soon!)", "value": 3, "disabled": True},
            ],
            value=2,
            id=ids.SVM_SELECT_NO_OF_FEATURES,
            inline=True,
        ),
    ]
)

# Select Mean
select_mean = html.Div(
    [
        dbc.Label("Choose Mean of the Dataset(To be generated)"),
        dcc.Slider(1, 5, 1,
                   value=2,
                   id=ids.SVM_SELECT_MEAN,
                   ),
    ])

# Select SD
select_sd = html.Div(
    [
        dbc.Label("Choose Standard deviation of the Dataset(To be generated)"),
        dcc.Slider(1, 3, 0.2,
                   value=1.2,
                   id=ids.SVM_SELECT_SD
                   ),
    ])

# figure
svm_graph = html.Div([
    dbc.Label("Let's see the dataset"),
    dcc.Graph(figure={}, id=ids.SVM_GRAPH_DATA),
    html.Br(),
    dbc.Label("Let's visualize results"),
    dcc.Graph(figure={}, id=ids.SVM_GRAPH_VIZ),
])


# helper graph function
def make_scatter_dataset(X, df):
    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(go.Scatter(x=X[:, 0], y=X[:, 1], mode='markers', marker=dict(size=8, color=df['group'])), row=1,
                  col=1)
    return fig


def make_scatter_results(X, df, all_coordinates):
    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(go.Scatter(x=X[:, 0], y=X[:, 1], mode='markers', marker=dict(size=8, color=df['group'])), row=1,
                  col=1)

    fig.add_shape(type='line',
                  x0=all_coordinates[0],
                  y0=all_coordinates[2],
                  x1=all_coordinates[1],
                  y1=all_coordinates[3],
                  line=dict(color='Black', dash="dash"),
                  xref='x',
                  yref='y'
                  )

    fig.add_shape(type='line',
                  x0=all_coordinates[0],
                  y0=all_coordinates[4],
                  x1=all_coordinates[1],
                  y1=all_coordinates[5],
                  line=dict(color='Yellow', ),
                  xref='x',
                  yref='y'
                  )

    fig.add_shape(type='line',
                  x0=all_coordinates[0],
                  y0=all_coordinates[6],
                  x1=all_coordinates[1],
                  y1=all_coordinates[7],
                  line=dict(color='Yellow', ),
                  xref='x',
                  yref='y'
                  )
    return fig


# helper function to get required coordinates
def get_hyperplane_value(x, w, b, offset):
    return (-w[0] * x + b + offset) / w[1]


def get_coordinates(X, clf):
    x0_1 = np.amin(X[:, 0])
    x0_2 = np.amax(X[:, 0])

    x1_1 = get_hyperplane_value(x0_1, clf.w, clf.b, 0)
    x1_2 = get_hyperplane_value(x0_2, clf.w, clf.b, 0)

    x1_1_m = get_hyperplane_value(x0_1, clf.w, clf.b, -1)
    x1_2_m = get_hyperplane_value(x0_2, clf.w, clf.b, -1)

    x1_1_p = get_hyperplane_value(x0_1, clf.w, clf.b, 1)
    x1_2_p = get_hyperplane_value(x0_2, clf.w, clf.b, 1)

    x1_min = np.amin(X[:, 1])
    x1_max = np.amax(X[:, 1])

    return [x0_1, x0_2, x1_1, x1_2, x1_1_m, x1_2_m, x1_1_p, x1_2_p, x1_min, x1_max]


@callback(
    Output(ids.SVM_GRAPH_DATA, "figure"),
    Input(ids.SVM_SELECT_SAMPLE_SIZE, "value"),
    Input(ids.SVM_SELECT_NO_OF_FEATURES, "value"),
    Input(ids.SVM_SELECT_MEAN, "value"),
    Input(ids.SVM_SELECT_SD, "value"),
)
def plot_dataset(sample_size, features, mean, sd):
    X, y = datasets.make_blobs(n_samples=sample_size, n_features=features, centers=mean, cluster_std=sd,
                               random_state=40)
    y = np.where(y == 0, -1, 1)

    clf = SVM()
    clf.fit(X, y)

    df = {
        'a': X[:, 0],
        'b': X[:, 1],
        'group': y
    }
    figure = make_scatter_dataset(X, df)
    return figure


@callback(
    Output(ids.SVM_GRAPH_VIZ, "figure"),
    Input(ids.SVM_SELECT_SAMPLE_SIZE, "value"),
    Input(ids.SVM_SELECT_NO_OF_FEATURES, "value"),
    Input(ids.SVM_SELECT_MEAN, "value"),
    Input(ids.SVM_SELECT_SD, "value"),
)
# the arguments in the function are received sequentially from callback
def create_dataset_and_plot(sample_size, features, mean, sd):
    # print(sample_size, features, mean, sd)
    X, y = datasets.make_blobs(n_samples=sample_size, n_features=features, centers=mean, cluster_std=sd,
                               random_state=40)
    y = np.where(y == 0, -1, 1)

    clf = SVM()
    clf.fit(X, y)

    df = {
        'a': X[:, 0],
        'b': X[:, 1],
        'group': y
    }

    all_coordinates = get_coordinates(X, clf)

    figure = make_scatter_results(X, df, all_coordinates)
    return figure


play = dbc.Container(html.Div([
    html.Br(),
    select_sample_size,
    html.Br(),
    select_features,
    html.Br(),
    select_mean,
    html.Br(),
    select_sd,
    html.Br(),
    svm_graph,
]))

layout = create_page_layout(learn_tab=learn, play_tab=play)
