# @Project:     LearnML
# @Filename:    app.py
# @Author:      Daksh
# @Time:        09-12-2022 03:48 pm

from dash import Dash, html



def main() -> None:
    app = Dash()
    app.title = "Learn ML"
    app.layout = html.Div("Learn ML")
    app.run(debug=True)


if __name__ == "__main__":
    main()