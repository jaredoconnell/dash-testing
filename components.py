from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
    dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal', multi=True),
    dcc.Slider(-5, 10, 1, value=-3),
    dcc.Slider(-10, 10, 0, value=-3)
])

if __name__ == '__main__':
    app.run_server(debug=True)

