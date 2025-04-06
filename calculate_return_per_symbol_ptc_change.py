def calculate_returns(prices):
    # Sort by symbol and date
    prices.sort_values(by=['symbol', 'date'], inplace=True)
    # Calculate returns
    prices['returns'] = prices.groupby('symbol')['close'].pct_change()
    # Remove missing values
    prices.dropna(inplace=True)