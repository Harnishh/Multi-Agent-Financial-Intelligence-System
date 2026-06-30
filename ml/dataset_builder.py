import pandas as pd

def build_dataset(df: pd.DataFrame):

    target_columns = [
        "Target",
        "Target_Return",
        "Target_Class"
    ]

    feature_columns = [
        col
        for col in df.columns
        if col not in target_columns
    ]

    X = df[feature_columns]

    y_return = df["Target_Return"]

    y_class = df["Target_Class"]

    return X, y_return, y_class, feature_columns