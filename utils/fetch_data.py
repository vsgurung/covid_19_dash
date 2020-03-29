# Python script to read data from ArcGIS REST API and download the relevant data
# There are separate spreadsheet for daily indicator and cumulative data.
# A new spreadsheet is available
import pandas as pd

# Pulling data from separate spreadsheet.

source_spreadsheet_url = 'https://fingertips.phe.org.uk/documents/Historic%20COVID-19%20Dashboard%20Data.xlsx'
uk_cases_worksheet = 'UK Cases'
uk_deaths_worksheet = 'UK Deaths'
countries_worksheet = 'Countries'
nhs_regions_worksheet = 'NHS Regions'
utla_worksheet = 'UTLAs'
recovered_patient_worksheet = 'Recovered patients'

# ArcGIS REST URL and other variables
arcgis_rest_url = 'https://www.arcgis.com/sharing/rest/content/items/'

def daily_indicators():
    """
    Function to read from ArcGIS REST API and download the daily indicator data.
    Returns: Pandas dataframe
    """
    try:
        raw_data = pd.read_excel(arcgis_rest_url +'bc8ee90225644ef7a6f4dd1b13ea1d67/data')
        df = pd.DataFrame(raw_data)
        return df
    except Exception as e:
        print(f'The function returned error {e}.')

def daily_confirmed_cases():
    """
    Function to read from ArcGIS REST API and download the daily indicator data.
    Returns: Pandas dataframe
    """
    try:
        raw_data = pd.read_excel(arcgis_rest_url+'e5fd11150d274bebaaf8fe2a7a2bda11/data')
        df = pd.DataFrame(raw_data)
        return df
    except Exception as e:
        print(f"The function returned error {e}.")


def nhs_england_cases():
    try:
        raw_data = pd.read_csv(arcgis_rest_url+'ca796627a2294c51926865748c4a56e8/data')
        df = pd.DataFrame(raw_data)
        return df
    except Exception as e:
        print(f"The function returned error {e}.")

def county_ua_cases():
    try:
        raw_data = pd.read_csv(arcgis_rest_url+'b684319181f94875a6879bbc833ca3a6/data')
        df = pd.DataFrame(raw_data)
        return df.sort_values(by='TotalCases', ascending=True)
    except Exception as e:
        print(f"The function returned error {e}.")

## All function from here onwards use the Historic COVID-19 Dashboard Data.xlsx to create the dataframe.
def recovered_patients_df():
    """
    The spreadsheet contains few rows which are not needed for creating the dataframe. Hence skiprows parameter is needed.
    Returns pandas dataframe.
    """
    try:
        raw_data = pd.read_excel(source_spreadsheet_url, recovered_patient_worksheet, skiprows=range(0, 5))
        df = pd.DataFrame(raw_data).fillna(0.0)
        return df
    except Exception as e:
        print(f"The function returned error. {e}")

# The function below is disabled for now
# def uk_deaths_df():
#     try:
#         raw_data = pd.read_excel(source_spreadsheet_url, uk_deaths_worksheet, skiprows=range(0,6))
#         df = pd.DataFrame(raw_data).fillna(0)
#         return df
#     except Exception as e:
#         print(f'An error occured while executing the function. {e}')
