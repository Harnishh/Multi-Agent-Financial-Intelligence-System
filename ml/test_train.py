from historical_data import load_stock_history
from indicators import add_technical_indicators
from feature_engineering import engineer_features
from dataset_builder import build_dataset
from train_model import train_models

df = load_stock_history("INFY.NS")

df = add_technical_indicators(df)

df = engineer_features(df)

X,  y_return, y_class, features = build_dataset(df)

train_models(
    X,
    y_return,
    y_class,
    features
)