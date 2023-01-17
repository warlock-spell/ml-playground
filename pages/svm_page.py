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
from sklearn.model_selection import train_test_split
import plotly.express as px

dash.register_page(__name__, title="SVM", name="SVM", order=page_order["svm_page"])
learn = dbc.Container("Hello")

# Select sample size

# Select Features

# Select Mean

# Select SD

X, y = datasets.make_blobs(n_samples=50, n_features=2, centers=2, cluster_std=1.05, random_state=40)
y = np.where(y == 0, -1, 1)

clf = SVM()
clf.fit(X, y)

df = {
    'a': X[:, 0],
    'b': X[:, 1],
    'group': y
}


def get_hyperplane_value(x, w, b, offset):
    return (-w[0] * x + b + offset) / w[1]


def get_coordinates():
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


all_coordinates = get_coordinates()

play = dbc.Container("Hi")

layout = create_page_layout(learn_tab=learn, play_tab=play)