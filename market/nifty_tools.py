import yfinance as yf

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