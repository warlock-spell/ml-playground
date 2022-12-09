# @Project:     LearnML
# @Filename:    app.py
# @Author:      Daksh
# @Time:        09-12-2022 03:48 pm

import dash
from dash import Dash
from src.component.main_layout import create_layout, url_theme1
import dash_bootstrap_components as dbc


def main() -> None:
    app = Dash(__name__, use_pages=True, external_stylesheets=[url_theme1])
    app.title = "Learn ML"
    app.layout = create_layout(app)
    app.run(debug=True)


if __name__ == "__main__":
    main()
