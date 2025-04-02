import numpy as np
import pandas as pd

def adjust_prices(prices):
    # Adjust prices
    prices['adj_close'] = np.where(prices['adj_close'] <0, prices['close'], prices['adj_close'])
    prices['adj_rate'] = prices['adj_close'] / prices['close']
    prices[['open','high','low']] *= prices['adj_rate'].values.reshape(-1, 1)
    prices.rename(columns={'close': 'close_raw', 'adj_close': 'close'}, inplace=True)
    prices.drop(columns=['adj_rate'], inplace=True)