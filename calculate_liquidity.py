# Function to label most liquid assets. 
"""
Identifies the n most liquid assets.

Parameters:
prices (DataFrame): DataFrame containing stock prices with a column that already has a colum dollar_value_total for dollar_value per month. 

Returns:
DataFrame: DataFrame with a column identifying the n most liquid stocks
"""

def calculate_liquidity(prices, n):
    dt = prices.copy()
    dt.sort_values(by=['date', 'dollar_value_total'], ascending=[True, False], inplace=True)
    dt['liquid_' + str(n)] = dt.groupby('date').cumcount() < n
    print(dt)
    return dt
