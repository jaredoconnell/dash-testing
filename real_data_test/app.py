# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html
import dash_bootstrap_components as dbc
import pandas as pd

import simdata

df = pd.DataFrame.from_records(simdata.data)

def generate_table(dataframe, max_rows=10):
    return dbc.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = Dash(__name__,
      external_stylesheets=[dbc.themes.CYBORG]
)


app.layout = html.Div([
    html.H4(children='Example data'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
