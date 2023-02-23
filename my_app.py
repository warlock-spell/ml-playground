# @Project:     LearnML
# @Filename:    my_app.py
# @Author:      Daksh
# @Time:        09-12-2022 03:48 pm

import dash
from dash import Dash
from src.component.main_layout import create_layout, url_theme1
import dash_bootstrap_components as dbc
external_scripts = [
    {
        'src': 'https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css',
        'integrity': 'sha384-vKruj+a13U8yHIkAyGgK1J3ArTLzrFGBbBc0tDp4ad/EyewESeXE/Iv67Aj8gKZ0',
        'crossorigin': 'anonymous'
    }
]



app = Dash(__name__, use_pages=True, external_stylesheets=[url_theme1], external_scripts=external_scripts)
server = app.server
app.title = "Learn ML"
app.layout = create_layout(app)
app.run(debug=False)

