import pandas as pd
def remove_penny_stocks (prices):
    #removed_prices=prices[prices.groupby('symbol')['close'].transform('last') < 5]
    prices= prices[prices.groupby('symbol')['close'].transform('last') >= 5]
    print("iN FUNCTION")
    print(prices)
    return prices