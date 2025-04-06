def calculate_market_returns_SPY(prices):
    """
    Calculate market returns for SPY.
    
    Parameters:
    prices (DataFrame): DataFrame containing stock prices with a column that already has a return calcuation column prices['returns'] per symbol. 
    
    Returns:
    DataFrame: DataFrame with market returns for SPY.
    """
    
    spy_ret = prices[prices['symbol'] == 'spy'][['date', 'returns']].rename(columns={'returns': 'market_ret'})
    prices.merge(spy_ret, on='date', how='left')
    print("IN FUNCTION")
    print(prices)
