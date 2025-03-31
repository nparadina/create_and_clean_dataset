def clear_duplicates(prices):
    # Convert column names to lowercase and replace spaces with underscores
    prices.columns = prices.columns.str.lower().str.replace(' ', '_')
    # Remove duplicate rows based on 'symbol' and 'date'
    prices.drop_duplicates(subset=['symbol', 'date'], inplace=True)

    # Remove rows with duplicated symbols (e.g., 'phun' and 'phun.1')
    # Create `symbol_short` by removing any trailing '.number' suffix
    prices['symbol_short'] = prices['symbol'].str.replace(r'\.\d$', '', regex=True)

    # Define columns to check for duplicates
    cols = ['date', 'open', 'high', 'low', 'close', 'volume', 'adj_close', 'symbol_short']

    # Drop duplicates but keep the first occurrence
    prices = prices.drop_duplicates(subset=cols, keep='first').drop(columns=['symbol_short'])
    return prices