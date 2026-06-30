from historical_data import load_stock_history
from indicators import add_technical_indicators
from feature_engineering import engineer_features

df = load_stock_history("INFY.NS")

df = add_technical_indicators(df)

df = engineer_features(df)

print(df.shape)

print(df.columns)

print(df.tail())