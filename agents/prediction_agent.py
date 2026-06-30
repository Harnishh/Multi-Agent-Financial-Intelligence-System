import joblib

from ml.historical_data import load_stock_history
from ml.indicators import add_technical_indicators
from ml.feature_engineering import engineer_features
from utils.ticker_mapper import TICKER_MAP

PRICE_MODEL = joblib.load("ml/models/price_model.pkl")

DIRECTION_MODEL = joblib.load("ml/models/direction_model.pkl")

FEATURE_COLUMNS = joblib.load("ml/models/feature_columns.pkl")


def prediction_agent(state):

    company = state["company"].lower().strip()

    ticker = TICKER_MAP.get(company)

    if ticker is None:
        raise ValueError(f"No ticker found for {company}")

    df = load_stock_history(ticker)

    df = add_technical_indicators(df)

    df = engineer_features(df)

    latest = df.iloc[-1]

    X = latest[FEATURE_COLUMNS]

    X = X.to_frame().T

    predicted_return = PRICE_MODEL.predict(X)[0]

    probability = DIRECTION_MODEL.predict_proba(X)[0]

    prediction = DIRECTION_MODEL.predict(X)[0]

    confidence = max(probability)

    current_price = latest["Close"]

    predicted_price = current_price * (1 + predicted_return)

    if prediction == 1:

        direction = "UP"

    else:

        direction = "DOWN"

    if confidence >= 0.70:

        recommendation = "BUY" if direction == "UP" else "SELL"

    else:

        recommendation = "HOLD"

    return {

        "ml_prediction":{

            "current_price":round(current_price,2),

            "predicted_price":round(predicted_price,2),

            "predicted_return":round(predicted_return*100,2),

            "direction":direction,

            "confidence":round(confidence*100,2),

            "recommendation":recommendation
        }

    }