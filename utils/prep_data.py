# Python script to create the variables storing COVID-19 metrics to be created here.
from . import fetch_data
import datetime
# import fetch_data
# need to create function instead of variables.

daily_confirmed_cases = fetch_data.daily_confirmed_cases()
daily_indicators = fetch_data.daily_indicators()
nhs_england_data = fetch_data.nhs_england_cases()
county_ua = fetch_data.county_ua_cases()
recovery_data = fetch_data.recovered_patients_df()
# uk_deaths = fetch_data.uk_deaths_df()
first_case_confirmed_date = '31/01/2020'

# Extract the date today and yesterday
# Using the dates in the data

def latest_date():
    """
    Get the latest date from the daily indicator
    """
    # cur_dt = daily_confirmed_cases['DateVal'].iloc[-1].strftime('%d %b %Y')
    cur_dt = daily_confirmed_cases['DateVal'].iloc[-1].date()
    return cur_dt

def previous_day_date():
    prev_dt = daily_confirmed_cases['DateVal'].iloc[-2].date()
    return prev_dt

def calculate_percent_change(pandas_series):
    """
    Accepts two pandas series as parameter
    """
    current = pandas_series.iloc[-1]
    yesterday = pandas_series.iloc[-2]

    if current > yesterday:
        increase = round(((current - yesterday)/yesterday)*100, 1)
        return increase
    elif current == yesterday:
        return 0
    else:
        decrease = round(((current - yesterday)/yesterday)*100, 1)
        return decrease

# Finding the elapsed days
first_case_confirmed_date = datetime.datetime.strptime('31/01/2020', "%d/%m/%Y").date()
todays_date = latest_date()
days_diff= todays_date - first_case_confirmed_date
days_elapsed = days_diff.days

# Creating date in 12 Mar 2020 format
dt_for_heading = latest_date().strftime('%d %b %Y')

# UK Metrics variables
total_uk_cases = daily_indicators.iloc[0]['TotalUKCases']
new_uk_cases = daily_indicators.iloc[0]['NewUKCases']
total_uk_deaths = daily_indicators.iloc[0]['TotalUKDeaths']
daily_uk_deaths = daily_confirmed_cases.iloc[0]['DailyDeaths']
daily_confirmed_case_perc= calculate_percent_change(daily_confirmed_cases['CumCases'])
daily_death_perc = calculate_percent_change(daily_confirmed_cases['CumDeaths'])
recovered_patients = recovery_data['Cumulative Counts'].max()


# Individual country metrics
total_england_cases = daily_indicators.iloc[0]['EnglandCases']
total_england_deaths = daily_indicators.iloc[0]['EnglandDeaths']
# england_death_perc = calculate_percent_change(uk_deaths['England'])
total_wales_cases = daily_indicators.iloc[0]['WalesCases']
total_wales_deaths = daily_indicators.iloc[0]['WalesDeaths']
# wales_death_perc = calculate_percent_change(uk_deaths['Wales'])
total_ni_cases = daily_indicators.iloc[0]['NICases']
total_ni_deaths = daily_indicators.iloc[0]['NIDeaths']
# ni_death_perc = calculate_percent_change(uk_deaths['Northern Ireland'])
total_scotland_cases = daily_indicators.iloc[0]['ScotlandCases']
total_scotland_deaths = daily_indicators.iloc[0]['ScotlandDeaths']
# scotland_death_perc = calculate_percent_change(uk_deaths['Scotland'])

# Variable to store the list of county/unitary authority in alphabetical ascending order.
county_us_dropdown_list = [{'label':f'{name}', 'value':f'{name}'} for name in sorted(county_ua['GSS_NM'].tolist())]