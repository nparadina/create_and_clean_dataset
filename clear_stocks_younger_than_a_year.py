def clear_stocks_younger_than_a_year(prices):
    # Keep only symbols with at least 253 observations (at least a year of data)
    symbol_counts = prices['symbol'].value_counts()
    remove_symbols = symbol_counts[symbol_counts < 253].index
    prices = prices[~prices['symbol'].isin(remove_symbols)]
    return prices