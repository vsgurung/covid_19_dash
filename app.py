import dash 
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output

from utils.check_net_connectivity import connection_status

from utils import fetch_data, prep_data, prep_graph_figures
from utils.prep_data import total_england_cases, total_scotland_cases, \
                            total_ni_cases, total_wales_cases
from utils.prep_html_tags import    generate_heading_tag, generate_markdown_tag, generate_left_column_tags, \
                                    generate_right_column_tags, generate_footer_tags

external_stylesheets = ['https://fonts.googleapis.com/css?family=Nunito', dbc.themes.BOOTSTRAP] 

# Setting out the Dash Application
app = dash.Dash(__name__, assets_folder='./assets/', external_stylesheets=external_stylesheets)

server = app.server # This line is needed for heroku
app.title = 'COVID-19 UK Metrics'

# Application layout v1.
suppress_callback_exceptions=True
app.layout = html.Div([
            html.Div(id='heading-tag'),
            html.Div(id='markdown-tag'),
            html.Div([
                # Left column with UK metrics and County/Unitary Authority Cases
                html.Div(id='left-column-tag', style={'width':'40%','backgroundColor':'#B9BBBD'}),
                # Right Column with metrics and the graphs
                html.Div(id='right-column-tag', style={'width':'60%','backgroundColor':'#B9BBBD'}),
                ], className="row", style={'display':'flex'}),
                html.Div(id='footer-tag'),
                dcc.Interval(
                    id='timer',
                    interval = 1*900000, # the page should refresh every 15 minutes
                    n_intervals=0
                )
        ], className='container-fluid',  style={'fontFamily':'nunito', 'backgroundColor':'#ffffe6'})


# All the callbacks 
@app.callback(Output('heading-tag', 'children'),
[Input('timer', 'n_intervals')])

def update_header(n):
    header = generate_heading_tag()
    return header

@app.callback(Output('markdown-tag', 'children'),
[Input('timer', 'n_intervals')])

def update_markdown(n):
    md = generate_markdown_tag()
    return md

@app.callback(Output('left-column-tag', 'children'),
[Input('timer', 'n_intervals')])

def update_left_column_tag(n):
    lt = generate_left_column_tags()
    return lt

@app.callback(Output('right-column-tag', 'children'),
[Input('timer', 'n_intervals')])

def update_right_column_tag(n):
    rt = generate_right_column_tags()
    return rt

@app.callback(Output('footer-tag', 'children'),
[Input('timer', 'n_intervals')])

def update_footer_tag(n):
    rt = generate_footer_tags()
    return rt


# Running the app
if __name__ == "__main__":
    app.run_server(debug=True)
