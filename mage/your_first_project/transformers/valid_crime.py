if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    import numpy as np
    import pandas as pd
    
    # remove bad dates
    data = data[data['Date Rptd'].dt.year >= 2020]
    data = data[data['DATE OCC'].dt.year >= 2020]
    
    # remove empty area names
    data = data[data['AREA NAME'].notnull()]

    #add a column days delay
    data['days delay'] = (data['Date Rptd'] - data['DATE OCC']).dt.days
    data = data[data['days delay'] >= 0]

    # rename headers
    columns_original = data.columns
    data.columns = (data.columns
        .str.replace(' ', '_')
        .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
        .str.lower()
        )
    columns_new = data.columns

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
