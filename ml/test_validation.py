from historical_data import load_stock_history
from indicators import add_technical_indicators
from feature_engineering import engineer_features
from feature_validation import FeatureValidator

df = load_stock_history("INFY.NS")

df = add_technical_indicators(df)

df = engineer_features(df)

validator = FeatureValidator(df)

validator.generate_report()