import ta
import pandas as pd


def add_technical_indicators(df: pd.DataFrame):

    df = df.copy()

    # ==========================
    # Trend Indicators
    # ==========================

    df["SMA_5"] = ta.trend.sma_indicator(
        df["Close"],
        window=5
    )

    df["SMA_10"] = ta.trend.sma_indicator(
        df["Close"],
        window=10
    )

    df["SMA_20"] = ta.trend.sma_indicator(
        df["Close"],
        window=20
    )

    df["EMA_10"] = ta.trend.ema_indicator(
        df["Close"],
        window=10
    )

    df["EMA_20"] = ta.trend.ema_indicator(
        df["Close"],
        window=20
    )

    df["EMA_50"] = ta.trend.ema_indicator(
        df["Close"],
        window=50
    )

    # ==========================
    # Momentum
    # ==========================

    df["RSI"] = ta.momentum.rsi(
        df["Close"],
        window=14
    )

    macd = ta.trend.MACD(df["Close"])

    df["MACD"] = macd.macd()

    df["MACD_SIGNAL"] = macd.macd_signal()

    df["MACD_DIFF"] = macd.macd_diff()

    # ==========================
    # Volatility
    # ==========================

    bollinger = ta.volatility.BollingerBands(df["Close"])

    df["BB_HIGH"] = bollinger.bollinger_hband()

    df["BB_LOW"] = bollinger.bollinger_lband()

    df["BB_MIDDLE"] = bollinger.bollinger_mavg()

    df["ATR"] = ta.volatility.average_true_range(
        df["High"],
        df["Low"],
        df["Close"]
    )

    # ==========================
    # Volume
    # ==========================

    df["OBV"] = ta.volume.on_balance_volume(
        df["Close"],
        df["Volume"]
    )

    return df