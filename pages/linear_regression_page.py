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
from sklearn import datasets
from sklearn.model_selection import train_test_split
from plotly.subplots import make_subplots
from src.component import ids
import plotly.graph_objects as go
import numpy as np
from algorithm.linear_regression import LinearRegression
from itertools import chain

dash.register_page(__name__, title="Linear Regression", name="Linear Regression",
                   order=page_order["linear_regression_page"])

learn = dbc.Container([dcc.Markdown(content, dangerously_allow_html=True, mathjax=True)])

# select sample size
select_sample_size = html.Div([
    dbc.Label("Select Sample Size"),
    dbc.RadioItems(id=ids.LR_SELECT_SAMPLE_SIZE,
                   options=[
                       {'Size': '50', 'value': 50},
                       {'Size': '100', 'value': 100},
                       {'Size': '150', 'value': 150},
                       {'Size': '200', 'value': 200},
                   ],
                   value=100, inline=True)],
    )

NUMBER_OF_FEATURES = 1

# select noise
select_noise = html.Div([
dbc.Label("Select noise for the Dataset(To be generated)"),
    dbc.RadioItems(id=ids.LR_SELECT_NOISE,
                   options=[
                       {'Noise': '10', 'value': 10},
                       {'Noise': '20', 'value': 20},
                       {'Noise': '30', 'value': 30},
                   ],
                   value=20, inline=True), html.Br()],
    )

# select random state
select_random_state = html.Div([
dbc.Label("Select random state for the Dataset(To be generated)"),
    dbc.RadioItems(id=ids.LR_SELECT_RANDOM_STATE,
                    options=[
                        {'Random State': '1', 'value': 1},
                        {'Random State': '2', 'value': 2},
                        {'Random State': '3', 'value': 3},
                        {'Random State': '4', 'value': 4},
                    ],
                    value=4, inline=True), html.Br()],
    )

# select test size
select_test_size = html.Div(
    [
        dbc.Label("Choose test size (in fraction)"),
        dcc.Slider(0.05, 0.3, 0.05,
                   value=0.2,
                   id=ids.LR_SELECT_TEST_SIZE,
                   ), html.Br()
    ],
    )

# select learning rate - alpha
select_alpha = html.Div(
    [
dbc.Label("Select Learning Rate of the model"),
        dbc.RadioItems(id=ids.LR_SELECT_ALPHA,
                    options=[
                        {'Learning Rate': '0.0001', 'value': 0.0001},
                        {'Learning Rate': '0.001', 'value': 0.001},
                        {'Learning Rate': '0.005', 'value': 0.005},
                        {'Learning Rate': '0.01', 'value': 0.01},
                        {'Learning Rate': '0.05', 'value': 0.05},
                    ],
                    value=0.001, inline=True), html.Br()],
    )

# graph component
# figure
lr_graph = html.Div([
    dbc.Label("Let's see the results"),
    dcc.Graph(figure={}, id=ids.LR_GRAPH_VIZ),
html.Br(),
])

# error component
show_error = html.Div(
    [
        html.P("The Mean Squared Error is:"),
        html.Br(),
        html.P(id=ids.LR_SHOW_ERROR),
html.Br(),
    ]
)


# dataset creation
def create_dataset(n_samples, n_features, noise, random_state, test_size):
    X, y = datasets.make_regression(n_samples=n_samples, n_features=n_features, noise=noise, random_state=random_state)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=1234
    )
    return X, y, X_train, X_test, y_train, y_test


# error function
def mse(y_true, y_predicted):
    return np.mean((y_true - y_predicted) ** 2)


@callback(

    [Output(ids.LR_GRAPH_VIZ, "figure"), Output(ids.LR_SHOW_ERROR, "children")],
    Input(ids.LR_SELECT_SAMPLE_SIZE, "value"),
    Input(ids.LR_SELECT_NOISE, "value"),
    Input(ids.LR_SELECT_RANDOM_STATE, "value"),
    Input(ids.LR_SELECT_TEST_SIZE, "value"),
    Input(ids.LR_SELECT_ALPHA, "value"),
)
def create_dataset_and_plot(sample_size, noise, random_state, test_size, alpha):
    X, y, X_train, X_test, y_train, y_test = create_dataset(n_samples=sample_size,
                                                            n_features=NUMBER_OF_FEATURES,
                                                            noise=noise,
                                                            random_state=random_state,
                                                            test_size=test_size)

    # print(X, y)

    # initializing regressor
    regressor = LinearRegression(lr=alpha)
    regressor.fit(X_train, y_train)
    predicted_values = regressor.predict(X_test)

    mse_i_value = mse(y_test, predicted_values)

    # plotting logic
    X_test = list(chain(*X_test))
    X = list(chain(*X))
    # Define data for scatter plot
    scatter_data = go.Scatter(x=X, y=y, mode='markers')
    # Define data for line plot
    line_data = go.Scatter(x=X_test, y=predicted_values, mode='lines')
    # Define layout for the graph
    layout = go.Layout(title='Scatter Plot with Line', xaxis=dict(title='X-Axis'), yaxis=dict(title='Y-Axis'))
    # Combine scatter and line data in one figure
    fig = go.Figure(data=[scatter_data, line_data], layout=layout)

    # return fig
    return fig, mse_i_value




play = dbc.Container(html.Div(
    [
        html.Br(),
        select_sample_size,
        html.Br(),
        select_noise,
        html.Br(),
        select_random_state,
        html.Br(),
        select_test_size,
        html.Br(),
        select_alpha,
        html.Br(),
        show_error,
        html.Br(),
        lr_graph,
    ]
))

layout = create_page_layout(learn_tab=learn, play_tab=play)
