import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

VALID_USERNAME_PASSWORD_PAIRS = [
    ['tobi', 'rule1tobi'],
    ['billy', 'rule1billy'],
    ['marco', 'rule1marco'],
]

app = dash.Dash('auth')
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
server = app.server
app.config.supress_callback_exceptions = True

app.scripts.config.serve_locally = True

stock_cache = {}


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/screener':
         from .boards import screenerboard
         return screenerboard.layout
    elif pathname == '/stock':
         from .boards import stockboard
         return stockboard.layout
    else:
        return html.Div([
            dcc.Link('Stockscreener', href='/screener'),
            html.Br(),
            dcc.Link('Stock', href='/stock'),
        ])
