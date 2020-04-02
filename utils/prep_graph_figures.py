"""
All the figures that are needed will be drawn here.
"""
from . import fetch_data, prep_data

daily_confirmed_cases = fetch_data.daily_confirmed_cases()
county_ua_cases = fetch_data.county_ua_cases()

# Creating a separate colour for highest reported case of the day. 
colours = ['#FC7979' if x==daily_confirmed_cases['CMODateCount'].max() else '#909EFC' for x in daily_confirmed_cases['CMODateCount']]
text = ['Highest Case' if x==daily_confirmed_cases['CMODateCount'].max() else None for x in daily_confirmed_cases['CMODateCount']]


# Bar chart
# daily_metrics_figure = {'data':[{'x':fetch_data.daily_confirmed_cases()['DateVal'],
#                                  'y':fetch_data.daily_confirmed_cases()['CMODateCount'],
#                                  'type':'bar',
#                                  'marker':{'color':colours}
#                                  }],
#                         'layout':{
#                                 'title':'Daily Confirmed Cases',
#                                 'titlefont':{'size':20},
#                                 'paper_bgcolor':'#B9BBBD',
#                                 'plot_bgcolor':'#faebd7',
#                                 'autosize':True,
#                                 'xaxis':{'tickformat':'%d %b'},
#                                 'yaxis':{'tickformat':','},
#                                 'annotations':[{
#                                                 'xref':'paper',
#                                                 'yref':'paper',
#                                                 'x':0.5,
#                                                 'y':-0.15,
#                                                 'xanchor':'center',
#                                                 'yanchor':'bottom',
#                                                 'text':'The bar in red colour is the highest reported case in a day.',
#                                                 'showarrow':False
#                                                 }]
#                                 }
#                         }

# Area Plot
daily_metrics_figure = {'data':[# Adding the daily deaths data
                                 {'x':daily_confirmed_cases['DateVal'],
                                 'y':daily_confirmed_cases['DailyDeaths'],
                                 'type':'scatter',
                                 'mode':'lines',
                                 'name':'Daily Reported Deaths',
                                 'marker':{'color':'rgba(196, 0, 0, 1)'},
                                 'fill':'tonexty',
                                 'fillcolor':' rgba(0, 0, 0, 1)',
                                 'stackgroup':'one'
                                 },
                                 {'x':daily_confirmed_cases['DateVal'],
                                 'y':daily_confirmed_cases['CMODateCount'],
                                 'type':'scatter',
                                 'name':'Daily Confirmed Cases',
                                 'mode':'lines+text+markers',
                                 'text':text,
                                 'textposition':'left center',
                                 'marker':{'color':'rgba(196, 0, 0, 0.56)'},
                                 'fill':'tonexty',
                                 'fillcolor':'rgba(196, 0, 0, 0.56)',
                                 'stackgroup':'one'
                                 }
                                 
                                 ],
                        'layout':{
                                'title':'Daily Confirmed Cases and Deaths',
                                'titlefont':{'size':20},
                                'paper_bgcolor':'#B9BBBD',
                                'plot_bgcolor':'#faebd7',
                                'autosize':True,
                                'xaxis':{'tickformat':'%d %b'},
                                'yaxis':{'tickformat':','}
                                }
                        }



daily_cumulative_figure = {'data':[{'x':daily_confirmed_cases['DateVal'],
                                    'y':daily_confirmed_cases['CumCases'],
                                    'type':'scatter',
                                    'mode':'lines+markers',
                                    'marker':{'symbol':'0',
                                              'color':'#f4f4f2',
                                              'line':{'width':1,'color':'#f16a09'},
                                              'size':4},
                                    'line':{'width':4, 'color':'#f16a09'}}],
                            'layout':{
                                'title':'Daily Cumulative Cases',
                                'titlefont':{'size':20},
                                'paper_bgcolor':'#B9BBBD',
                                'plot_bgcolor':'#faebd7',
                                'autosize':True,
                                'xaxis':{'tickformat':'%d %b'},
                                'annotations':[{
                                                'xref':'paper',
                                                'yref':'paper',
                                                'x':0.5,
                                                'y':-0.15,
                                                'xanchor':'center',
                                                'yanchor':'bottom',
                                                'text':'People who have recovered and those who have died are included in cumulative counts.',
                                                'showarrow':False
                                                }]
                                }                        
                        }

county_ua_figure = {'data':[{'y':fetch_data.county_ua_cases()['GSS_NM'],
                             'x':fetch_data.county_ua_cases()['TotalCases'],
                             'type':'bar',
                             'orientation':'h',
                             'marker' :{
                                        'color':'#52B5D1',
                                        'line':{'color':'#333',
                                                'width':1}
                                        }
                        }],
                    'layout':{
                                'title':'Total Cases per County/UA',
                                'titlefont':{'size':20},
                                'paper_bgcolor':'#B9BBBD',
                                'plot_bgcolor':'#D1D1D1',
                                'xaxis':{'title':'Total Cases', 'tickformat':','},
                                'autosize':True,
                                'height':720
                        }
                    }