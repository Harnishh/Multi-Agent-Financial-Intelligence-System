from historical_data import load_stock_history
from indicators import add_technical_indicators

df = load_stock_history("INFY.NS")
# print(df.columns)
# print(type(df["Close"]))
df = add_technical_indicators(df)

print(df.columns)

print(df.tail())