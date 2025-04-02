import pandas as pd
# CSV Load
# Load data from a path variable
def load_data():
    # Load the data from the CSV file
    path = 'C:/Users/nikap/QuantImp/stocks_daily.csv'
    prices = pd.read_csv(path, engine='pyarrow')
    return prices