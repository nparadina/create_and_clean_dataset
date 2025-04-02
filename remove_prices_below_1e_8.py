def remove_prices_below_1e8(prices):
    # Filter out rows where any price column is below 1e-8
    small_price_columns = prices[(prices['open'] < 1e-8) & (prices['high'] < 1e-8) & (prices['low'] < 1e-8) & (prices['close'] < 1e-8)]
    prices = prices[(prices['open'] > 1e-8) & (prices['high'] > 1e-8) & (prices['low'] > 1e-8) & (prices['close'] > 1e-8)]
    return prices