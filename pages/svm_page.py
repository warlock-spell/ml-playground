# @Project:     LearnML
# @Filename:    svm_page.py
# @Author:      Daksh
# @Time:        03-01-2023 11:01 pm

import dash
from dash import dcc, html, callback, Output, Input
from src.component.page_layout import create_page_layout
import dash_bootstrap_components as dbc
from src.component.page_order import order
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import plotly.express as px

dash.register_page(__name__, title="SVM", name="SVM", order=order["svm_page"])
learn = dbc.Container("Hello")

play = dbc.Container("Hi")

layout = create_page_layout(learn_tab=learn, play_tab=play)