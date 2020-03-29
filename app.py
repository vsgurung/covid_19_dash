import dash 
import dash_core_components as dcc 
import dash_html_components as html
from utils.check_net_connectivity import connection_status

from utils import fetch_data, prep_data, prep_graph_figures
from utils.prep_data import total_england_cases, total_scotland_cases, \
                            total_ni_cases, total_wales_cases
from utils.prep_html_tags import    heading_tag, markdown_tag, left_column_tags, \
                                    right_column_tags, footer, error_page

external_stylesheets = ['https://fonts.googleapis.com/css?family=Nunito', 'https://codepen.io/chriddyp/pen/bWLwgP.css'] 

# Setting out the Dash Application
app = dash.Dash(__name__, assets_folder='./assets/', external_stylesheets=external_stylesheets)

server = app.server # This line is needed for heroku
app.title = 'COVID-19 UK Metrics'


# Application layout v1.
app.layout = html.Div([
            heading_tag,
            markdown_tag,
            html.Div([
                # Left column with UK metrics and County/Unitary Authority Cases
                left_column_tags,
                # Right Column with metrics and the graphs
                right_column_tags,
                ], className="row", style={'display':'flex'}),
                html.Div(footer, style={'width':'100%'})
        ], style={'fontFamily':'nunito', 'backgroundColor':'#ffffe6'})



# Running the app
if __name__ == "__main__":
    app.run_server()
