import pandas as pd

def filter(df):
    key_words = [
    'Market',
    'Short',
    'Foo',
    'plan',
    'Ethereum',
    'eth',
    '🚀',
    '🔥',
    'bitcoin',
    'BTC',
    'HODL',
    'collapse',
    'crypto',
    'cryptocurrency',
    'currency',
    'price',
    'USD',
    'dollar',
    'scaling',
    'scale']
    x= ''
    for i in key_words:
        x += '|'+ i
    x=x[1:]
    refined_data_mask = df.iloc[:,-1].str.contains(x)
    refined_data = df[refined_data_mask]
    return refined_data

def split_data(df,num_splits=5):
    n = int(len(df)/num_splits)
    d = {}
    for x in range(num_splits-1):
        d["expert_df{0}".format(x)] = df.iloc[x*n:(x+1)*n,:]
    if len(df)%n ==0:
        return d
    else:
        d["expert_df{0}".format(num_splits-1)] = df.iloc[(num_splits-1)*n:,:]
        return d
