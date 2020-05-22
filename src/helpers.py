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


def get_cpi():
    """
    Read in the cpi data.
    """
    df = (
        pd.read_csv('data/CPIAUCSL.csv')
        .assign(date = lambda x: pd.to_datetime(x['DATE']))
        .drop(labels=['DATE'], axis=1)
        .rename(columns={'CPIAUCSL':'cpi'})
        [['date', 'cpi']]
    )
    
    return df


def get_prices():
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
            .assign(date = lambda x: pd.to_datetime(x['DATE']))
            .drop(labels=['DATE'], axis=1)
            .rename(columns={fixed:'price'})
            .assign(price = lambda x: pd.to_numeric(x.price, 
                                                    errors='coerce'))
            .assign(Meat = lambda x: x['Series'].map(CODE_MAP))
        )

    df = pd.concat([read_in(x) for x in FILES])
    
    return df

