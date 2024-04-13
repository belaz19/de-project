if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    import numpy as np
    import pandas as pd
    import re

    data = data[
        ['dr_no', 'date_occ', 'time_occ',
        'area_name', 'crm_cd_desc','weapon_used_cd',
        'vict_age', 'vict_sex', 'vict_descent']
    ]

    data = data[data['vict_age']>0]
    data = data[data['vict_sex'].notnull()]
    data = data[data['vict_descent'].notnull()]
    data['weapon_used_cd'] = data['weapon_used_cd'].apply(lambda x: 'Y' if pd.notnull(x) else 'N')
    data['time_occ']=data['time_occ'].apply(lambda x: 0 if x<60 else int(str(x)[:1]) if x<960 else int(str(x)[:2]))
    data['crm_cd_desc']=data['crm_cd_desc'].apply(lambda x: re.split(r'[-, ]+', x)[0])

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
