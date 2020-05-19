#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing one notebook into another isn't the best way to do this,
# but I ran into so many problems needing to reload imported modules
# while working interactively that this is the way I'm doin' it!!


def get_adjust(past_cpi, current_cpi, past_price):
    """
    Return the current dollar value of an amount
    in the past.
    """
    return (current_cpi / past_cpi) * past_price


def get_prices():
    """
    Read in and wrangle pricing data.
    """
    FILES = [
        'data/file-2.csv', 
        'data/file-3.csv', 
        'data/file-4.csv'
    ]
    CODE_MAP = {
        'CUUR0000SEFF':'Poultry',
        'CUUR0000SEFD':'Pork',
        'CUUR0000SEFC':'Beef'
    }
    df = (
        pd.concat([pd.read_csv(x) for x in FILES])
        .assign(Date = lambda x: pd.to_datetime(x['Label']))
        .assign(Meat = lambda x: x['Series ID'].map(CODE_MAP))
        .sort_values(by=['Label', 'Date'])
        .merge(cpi, how='left', on='Date')
    )
    
    return df


def get_indices():
    """
    Read in the index data.
    """
    FILES = [
        'data/APU0000703112.csv',
        'data/APU0000706111.csv',
        'data/APU0000FD3101.csv'
    ]
    CODE_MAP = {
        'APU0000703112':'Beef',
        'APU0000706111':'Chicken',
        'APU0000FD3101':'Pork'
    }

    def read_in(path):
        splt = lambda x: x.split('/')[1].split('.')[0]
        fixed = splt(path)

        return (
            pd.read_csv(path)
            .assign(Series = fixed)
            .assign(Date = lambda x: pd.to_datetime(x['DATE']))
            .rename(columns={fixed:'price'})
            .assign(price = lambda x: pd.to_numeric(x.price, 
                                                    errors='coerce'))
            .assign(Meat = lambda x: x['Series'].map(CODE_MAP))
        )

    df = pd.concat([read_in(x) for x in FILES])
    
    return df
