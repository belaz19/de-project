import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://data.lacity.org/api/views/2nrs-mtv8/rows.csv'
    
    crime_dtypes = {
        'DR_NO': pd.Int64Dtype(),
        'TIME OCC': pd.Int64Dtype(),
        'AREA': pd.Int64Dtype(),
        'AREA NAME': str,
        'Rpt Dist No': pd.Int64Dtype(),
        'Part 1-2': pd.Int64Dtype(),
        'Crm Cd': pd.Int64Dtype(),
        'Crm Cd Desc': str,
        'Mocodes': str,
        'Vict Age': pd.Int64Dtype(),
        'Vict Sex': str,
        'Vict Descent': str,
        'Premis Cd': pd.Int64Dtype(),
        'Premis Desc': str,
        'Weapon Used Cd': pd.Int64Dtype(),
        'Weapon Desc': str,
        'Status': str,
        'Status Desc': str,
        'Crm Cd 1': pd.Int64Dtype(),
        'Crm Cd 2': pd.Int64Dtype(),
        'Crm Cd 3': pd.Int64Dtype(),
        'Crm Cd 4': pd.Int64Dtype(),
        'LOCATION': str,
        'Cross Street': str,
        'LAT': float,
        'LON': float
    }
    
    parse_dates = ['Date Rptd', 'DATE OCC']
    response = requests.get(url)

    data = pd.read_csv(url, sep=",", dtype=crime_dtypes, parse_dates=parse_dates)
    return data
    # return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
