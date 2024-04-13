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
    url = 'https://data.ca.gov/dataset/59218446-5760-4683-b52e-f6210021840a/resource/b4bc4656-7866-420f-8d87-4eda4c9996ed/download'
    
    unemp_dtypes = {
        'Area Name': str,
        'Area Type': str,
        'Year': pd.Int64Dtype(),
        'Month': str,
        'Seasonally Adjusted(Y/N)': str,
        'Status': str,
        'Employment': pd.Int64Dtype(),
        'Unemployment': pd.Int64Dtype(),
        'Unemployment Rate': float
    }
    
    parse_dates = ['Date_Numeric']
    response = requests.get(url)

    data = pd.read_csv(url, sep=",", dtype=unemp_dtypes, parse_dates=parse_dates)
    return data
    # return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
