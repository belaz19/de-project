if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    import pandas as pd

    data = data[
        ['dr_no', 'date_occ', 'time_occ', 'days_delay',
        'area_name', 'crm_cd_desc', 'weapon_used_cd',
        'vict_age', 'vict_sex', 'vict_descent']
    ]

    data = data[data['vict_age']>0]
    data = data[data['vict_sex'].notnull()]
    data = data[data['vict_descent'].notnull()]

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
