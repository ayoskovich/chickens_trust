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


def apply_adjust(df, col, base):
    """ 
    Convert dataframe column using CPI
    """
    
    return df.apply(
                 lambda x: 
                    get_adjust(
                           past_cpi=x['cpi'],
                           current_cpi=base,
                           past_price=x[col]
                    ),
                 axis=1)


def chicken():
    """ Chicken, Fresh, Whole, Per Lb. (453.6 Gm) in U.S. City Average
    (APU0000706111)
    """
    df = pd.read_csv('data/APU0000706111.csv')
    
    return df


def beef():
    """ Ground Beef, 100% Beef, Per Lb. (453.6 Gm) in U.S. City Average 
    (APU0000703112)
    """
    df = pd.read_csv('data/APU0000703112.csv')
    
    return df


def pork():
    """ All Pork Chops, Per Lb. (453.6 Gm) in U.S. City Average 
    (APU0000FD3101)
    """
    df = pd.read_csv('data/APU0000FD3101.csv')
    
    return df
