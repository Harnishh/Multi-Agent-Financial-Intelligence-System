import yfinance as yf
import pandas as pd

def get_nifty_index():
    nifty = yf.Ticker("^NSEI")
    info = nifty.info
    current = info.get("regularMarketPrice")
    previous = info.get("previousClose")
    change = current - previous
    change_percent = (change / previous) * 100

    return{
        "current": round(current, 2),
        "previous": round(previous, 2),
        "change" : round(change, 2),
        "change_percent": round(change_percent, 2)
    }

def get_nifty_chart(period = "1mo"):
    nifty = yf.Ticker("^NSEI")
    if period == "5d":
        return nifty.history(
            period = "1mo",
            interval = "1h"
        )
    elif period == "1mo":
        return nifty.history(
            period = "1mo",
            interval = "1d"
        )
    elif period == "3mo":
        return nifty.history(
            period = "3mo",
            interval = "1d"
        )
    elif period == "6mo":
        return nifty.history(
            period = "6mo",
            interval = "1d"
        )
    elif period == "1y":
        return nifty.history(
            period = "1y",
            interval = "1d"
        )
    return nifty.history(period = period)

nifty_df = pd.read_csv(r"A:\project's\multi-agent financial intelligence system\market\nifty50.csv")

def get_market_leaders():
    symbols = nifty_df["Symbol"].tolist()

    data = yf.download(
        tickers = symbols,
        period = "2d",
        interval = '1d',
        group_by = "ticker",
        progress = False,
        auto_adjust = False
    )
    stocks = []

    for _, row in nifty_df.iterrows():
        company = row["Company"]
        symbol = row["Symbol"]

        try:
            closes = data[symbol]["Close"].dropna()
            if len(closes) < 2:
                continue

            previous_close = closes.iloc[-2]
            current_close = closes.iloc[-1]

            change_percent = (
                (current_close - previous_close) / previous_close
            ) * 100
            stocks.append(
                {
                    "company": company,
                    "symbol": symbol,
                    "price": round(current_close, 2),
                    "change": round(change_percent, 2)
                }
            )
        except Exception:
            continue
    gainers = sorted(
        stocks,
        key=lambda x: x["change"],
        reverse= True
    )[:5]

    losers = sorted(
        stocks,
        key= lambda x:x["change"]
    )[:5]

    return gainers, losers
        