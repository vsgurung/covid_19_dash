import dash 
import dash_core_components as dcc 
import dash_html_components as html
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output

from utils.check_net_connectivity import connection_status

from utils import fetch_data, prep_data, prep_graph_figures
from utils.prep_data import total_england_cases, total_scotland_cases, \
                            total_ni_cases, total_wales_cases
from utils.prep_html_tags import    generate_heading_tag, generate_markdown_tag, generate_left_column_figures, \
                                    generate_right_column_figures, generate_footer_tags, generate_number_plates

external_stylesheets = ['https://fonts.googleapis.com/css?family=Nunito', dbc.themes.BOOTSTRAP] 

# Setting out the Dash Application
app = dash.Dash(__name__,
                assets_folder='./assets/',
                external_stylesheets=external_stylesheets,
                meta_tags=[{"name": "viewport", 
                        "content": "width=device-width, height=device-height, initial-scale=1.0"}])

server = app.server # This line is needed for heroku
app.title = 'COVID-19 UK Metrics'

# Application layout v1.
suppress_callback_exceptions=True

app.layout = html.Div(
            [
                html.Div(id='heading-tag'),
                html.Div(id='markdown-tag'),
                html.Div(id='number-plate'),
                dbc.Row([
                    html.Div(id='left-column-figure'),
                    html.Div(id='right-column-figure')],
                    align='center', justify='center', no_gutters=True),
                html.Div(generate_footer_tags()),
                dcc.Interval(
                    id='timer',
                    interval = 1*900000, # the page should refresh every 15 minutes
                    n_intervals=0
                )
            ])


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

@app.callback(Output('number-plate', 'children'),
[Input('timer', 'n_intervals')])

def update_number_plate(n):
    num_plates = generate_number_plates()
    return num_plates

@app.callback(Output('left-column-figure', 'children'),
[Input('timer', 'n_intervals')])

def update_left_column_figures(n):
    lt = generate_left_column_figures()
    return lt

@app.callback(Output('right-column-figure', 'children'),
[Input('timer', 'n_intervals')])

def update_right_column_figures(n):
    rt = generate_right_column_figures()
    return rt



# Running the app
if __name__ == "__main__":
    app.run_server(debug=True)