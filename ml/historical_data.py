import yfinance as yf
import pandas as pd

def load_stock_history(ticker: str, years: int = 10) -> pd.DataFrame:
    period = f"{years}y"
    df = yf.download(
        ticker,
        period = period,
        interval = "1d",
        auto_adjust = True,
        progress = False
    )
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    if df.empty:
        raise ValueError(f"No historical data found for {ticker}")
    
    df.dropna(inplace=True)
    df.index = pd.to_datetime(df.index)
    df = df.rename(
        columns = {
            "Open": "Open",
            "High": "High",
            "Low": "Low",
            "Close": "Close",
            "Volume": "Volume"
        }
    )
    df = df[
        [
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]
    ]
    return df

if __name__ == "__main__":
    data = load_stock_history("INFY.NS", years=10)
    print(data.head())
    print()
    print(data.tail())
    print()
    print(data.shape)