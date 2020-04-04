# Python script to create all the html div tags that will be inserted in the layout.
# The styling information for each tag also be included here.
import dash 
import dash_html_components as html
import dash_core_components as dcc 

# from .prep_data import  dt_for_heading, days_elapsed, daily_confirmed_case_perc, daily_death_perc, \
#                         total_england_cases, total_england_deaths, england_death_perc, \
#                         total_scotland_cases, total_scotland_deaths, scotland_death_perc, \
#                         total_ni_cases, total_ni_deaths, ni_death_perc, \
#                         total_wales_cases, total_wales_deaths, wales_death_perc, \
#                         total_uk_cases, total_uk_deaths, new_uk_cases, recovered_patients

from .prep_data import  dt_for_heading, days_elapsed, daily_confirmed_case_perc, daily_death_perc, \
                        total_england_cases, total_england_deaths, \
                        total_scotland_cases, total_scotland_deaths, \
                        total_ni_cases, total_ni_deaths, \
                        total_wales_cases, total_wales_deaths, \
                        total_uk_cases, total_uk_deaths, new_uk_cases, recovered_patients, recovery_patients_date

from .prep_graph_figures import county_ua_figure, daily_cumulative_figure, daily_metrics_figure

# Function to generate the message to display increase/decrease
# def generate_perc_change_message(perc_variable):
#     """
#     Function to generate message for change in percentage.
#     Input: variable storing percentage
#     Output: Relevant message
#     """
#     if perc_variable > 0:
#         msg = f'Increase of {perc_variable}% in last 24h.'
#         return msg
#     elif perc_variable < 0:
#         msg = f'Decrease of {perc_variable}% in last 24h.'
#         return msg
#     else:
#         msg = 'No change'
#         return msg


# new_uk_cases_msg = generate_perc_change_message(daily_confirmed_case_perc)
# daily_death_perc_msg = generate_perc_change_message(daily_death_perc)
# england_death_perc_msg = generate_perc_change_message(england_death_perc)
# wales_death_perc_msg = generate_perc_change_message(wales_death_perc)
# ni_death_perc_msg = generate_perc_change_message(ni_death_perc)
# scotland_death_perc_msg = generate_perc_change_message(scotland_death_perc)

# Header tag for the page heading
def generate_heading_tag():
    heading_tag = html.H1(f'UK COVID-19 Metrics as of {dt_for_heading}', style={'textAlign':'center', 'fontWeight':'bold'})
    return heading_tag

# Markdown content
def generate_markdown_tag():
    markdown_tag = html.Div([
                            dcc.Markdown(f"""The first confirmed case of COVID-19 in the UK was [reported](https://www.standard.co.uk/news/health/coronavirus-35-cases-timeline-uk-covid19-new-a4375311.html "Evening Standard Report") on 31 Jan 2020. Since then, {days_elapsed} days have elapsed and the number of people affected has increased considerably.
                                            This dashboard displays the data as of {dt_for_heading}. This data is supplied by [Public Health England](https://www.gov.uk/government/publications/covid-19-track-coronavirus-cases "Public Health England COVID-19 Page").
                                            The metrics on this page updates as and when the underlying data powering this dashboard changes. If the data doesn't change, please clear the web browser cache and try refreshing the page again. The National Health Service (NHS) advice regarding COVID-19 for everyone can be found [here](https://www.nhs.uk/conditions/coronavirus-covid-19/). \nThe percentage refers to increase/decrease in past 24 hours. 
                                        """),
                            dcc.Markdown("""This dashboard is work in progress and is being improved continuously.""")]
                            , style={'textAlign':'justify', 'width':'100%', 'margin':'auto'})
    return markdown_tag

# Left columns divs, html and graphs
def generate_left_column_tags():
    left_column_tags = html.Div([
                        html.Div([
                            html.Div([
                                html.H2('Total UK Cases', style={'textAlign':'center', 'fontWeight':'bold', 'color': '#bf3afc'}),
                                html.H2(f'{total_uk_cases:,}', style={'textAlign':'center', 'fontWeight':'bold', 'color': '#bf3afc'})
                                ], style={'width':'50%'}),
                            html.Div([
                                html.H2(f'Recovered ({recovery_patients_date})', style={'textAlign':'center', 'color':'green'}),
                                html.H1(f'{recovered_patients:,.0f} ', style={'textAlign':'center', 'fontWeight':'bold', 'color':'green'})
                                ], style={'width':'50%'})
                        ], className='row', style={'display':'flex'}),
                        html.Div([
                            html.Div([
                                html.H3('New UK Cases', style={'textAlign':'center', 'fontWeight':'bold', 'color': '#0015ff'}),
                                html.H2(f'{new_uk_cases:,} ({daily_confirmed_case_perc}%)', style={'textAlign':'center', 'fontWeight':'bold', 'color': '#0015ff'})
                                ],
                                style={'width':'50%'}),
                            html.Div([
                                html.H3('Total UK Deaths', style={'textAlign':'center', 'fontWeight':'bold', 'color': '#d7191c'}),
                                html.H2(f'{total_uk_deaths:,} ({daily_death_perc}%)', style={'textAlign':'center', 'fontWeight':'bold', 'color': '#d7191c'})
                                ],
                                style={'width':'50%'})
                        ], className='row', style={'display':'flex'}),
                        # County & Unitary Authority Dropdown
                        # html.Label(['Select County/Unitary Authority',
                        #     dcc.Dropdown(
                        #     id='county_ua_dropdown',
                        #     options = county_us_dropdown_list,
                        #     multi=True
                        #         )
                        #     ], style={'width':'100%','backgroundColor':'#f2f2f2'}),
                        html.Div([
                            dcc.Graph(
                                id='county_ua_chart',
                                figure=county_ua_figure,
                                config={'displaylogo':False})],                
                                style={'width':'100%'})
                        ], className='container-fluid')
    return left_column_tags

def generate_right_column_tags():
    right_column_tags = html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.H3('England', style={'textAlign':'center'}),
                                    html.H3(f'{total_england_cases:,}', style={'textAlign':'center'}),
                                    html.H4(f'{total_england_deaths:,} deaths', style={'textAlign':'center', 'color': '#d7191c'})
                                    ], style={'width':'25%'}),
                                html.Div([
                                    html.H3('Scotland', style={'textAlign':'center'}),
                                    html.H3(f'{total_scotland_cases:,}', style={'textAlign':'center'}),
                                    html.H4(f'{total_scotland_deaths:,} deaths', style={'textAlign':'center', 'color': '#d7191c'})
                                    ], style={'width':'25%'}),
                                html.Div([
                                    html.H3('Wales', style={'textAlign':'center'}),
                                    html.H3(f'{total_wales_cases:,}', style={'textAlign':'center'}),
                                    html.H4(f'{total_wales_deaths:,} deaths', style={'textAlign':'center', 'color': '#d7191c'})
                                    ], style={'width':'25%'}),
                                html.Div([
                                    html.H3('Northern Ireland', style={'textAlign':'center'}),
                                    html.H3(f'{total_ni_cases:,}', style={'textAlign':'center'}),
                                    html.H4(f'{total_ni_deaths:,} deaths', style={'textAlign':'center', 'color': '#d7191c'})
                                    ], style={'width':'25%'})
                            ], style={'display':'flex'}),
                            dcc.Graph(
                                id='daily_metrics',
                                figure = daily_metrics_figure,
                                config = {'displaylogo':False}
                                ),
                            dcc.Graph(
                                id='cumulative_metrics',
                                figure = daily_cumulative_figure,
                                config = {'displaylogo':False}
                                )
                        ])
                    ])
    return right_column_tags

# Footer
def generate_footer_tags():
    footer = html.Div(
          id='my-footer',
          style={'marginLeft': '1.5%', 'marginRight': '1.5%', 'marginBottom': '1%', 'marginTop': '.5%'},
                 children=[
                     html.Hr(style={'marginBottom': '.5%'},),
                     html.P(style={'textAlign': 'center', 'margin': 'auto'},
                            children=['Developed by Vidya with ❤️', ' | ',
                                      'Stay at Home, Protect the NHS, Save Lives'
                                    ])
                  ])
    return footer

# Error page if not connected to internet.
# This is not needed for the moment so commenting it out.
# error_page = html.Div(
#                 html.H1('It seems, there is network connectivity issue. Please check your internet connection.')
#             )