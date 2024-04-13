if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    import numpy as np
    import pandas as pd
    
    # remove bad dates
    data = data[data['Area Type'] == 'Metropolitan Area']
    data = data[data['Year'] >= 2020]
    data = data[data['Seasonally Adjusted(Y/N)'] == 'Y']
    
    # remove empty area names
    data = data[data['Unemployment Rate'].notnull()]

    # select wanted columns
    data = data[['Date_Numeric', 'Unemployment Rate']]
    data = data.rename(columns={'Date_Numeric': 'date_numeric', 'Unemployment Rate': 'unemployment_rate'})

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
