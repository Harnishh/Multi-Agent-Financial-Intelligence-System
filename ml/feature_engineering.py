import pandas as pd


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # ====================================================
    # PRICE RETURNS
    # ====================================================

    df["Daily_Return"] = df["Close"].pct_change()

    df["Return_2"] = df["Close"].pct_change(2)

    df["Return_5"] = df["Close"].pct_change(5)

    df["Return_10"] = df["Close"].pct_change(10)

    # ====================================================
    # LOG RETURN
    # ====================================================

    import numpy as np

    df["Log_Return"] = np.log(df["Close"] / df["Close"].shift(1))

    # ====================================================
    # LAG FEATURES
    # ====================================================

    for lag in [1, 2, 3, 5, 10]:

        df[f"Close_Lag_{lag}"] = df["Close"].shift(lag)

        df[f"Volume_Lag_{lag}"] = df["Volume"].shift(lag)

        df[f"RSI_Lag_{lag}"] = df["RSI"].shift(lag)

    # ====================================================
    # ROLLING STATISTICS
    # ====================================================

    for window in [5, 10, 20]:

        df[f"Rolling_Mean_{window}"] = (
            df["Close"]
            .rolling(window)
            .mean()
        )

        df[f"Rolling_STD_{window}"] = (
            df["Close"]
            .rolling(window)
            .std()
        )

        df[f"Rolling_Max_{window}"] = (
            df["Close"]
            .rolling(window)
            .max()
        )

        df[f"Rolling_Min_{window}"] = (
            df["Close"]
            .rolling(window)
            .min()
        )

    # ====================================================
    # PRICE RANGE FEATURES
    # ====================================================

    df["High_Low_Range"] = (
        df["High"] - df["Low"]
    )

    df["Open_Close_Range"] = (
        df["Close"] - df["Open"]
    )

    df["High_Low_Pct"] = (
        (df["High"] - df["Low"])
        / df["Close"]
    )

    df["Open_Close_Pct"] = (
        (df["Close"] - df["Open"])
        / df["Open"]
    )

    # ====================================================
    # DISTANCE FROM MOVING AVERAGES
    # ====================================================

    df["Dist_SMA_20"] = (
        df["Close"] - df["SMA_20"]
    )

    df["Dist_EMA_20"] = (
        df["Close"] - df["EMA_20"]
    )

    df["Dist_BB_High"] = (
        df["Close"] - df["BB_HIGH"]
    )

    df["Dist_BB_Low"] = (
        df["Close"] - df["BB_LOW"]
    )

    # ====================================================
    # VOLUME FEATURES
    # ====================================================

    df["Volume_Change"] = (
        df["Volume"].pct_change()
    )

    df["Volume_MA_10"] = (
        df["Volume"]
        .rolling(10)
        .mean()
    )

    df["Relative_Volume"] = (
        df["Volume"]
        / df["Volume_MA_10"]
    )

    # ====================================================
    # VOLATILITY FEATURES
    # ====================================================

    df["ATR_Percent"] = (
        df["ATR"]
        / df["Close"]
    )

    df["Rolling_Volatility"] = (
        df["Daily_Return"]
        .rolling(10)
        .std()
    )

    # ====================================================
    # TIME FEATURES
    # ====================================================

    df["DayOfWeek"] = df.index.dayofweek

    df["Month"] = df.index.month

    df["Quarter"] = df.index.quarter

    df["WeekOfYear"] = df.index.isocalendar().week.astype(int)

    df["Year"] = df.index.year

    # ====================================================
    # TARGETS
    # ====================================================

    # Tomorrow Closing Price
    df["Target"] = df["Close"].shift(-1)

    df["Target_Return"] = (
        df["Target"] - df["Close"]
    ) / df["Close"]

    df["Target_Class"] = (
        df["Target_Return"] > 0
    ).astype(int)

    # ====================================================
    # REMOVE NaN
    # ====================================================

    df.dropna(inplace=True)

    return df