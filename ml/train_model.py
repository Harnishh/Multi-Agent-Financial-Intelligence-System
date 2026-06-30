import os
import joblib

from lightgbm import LGBMRegressor, LGBMClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def train_models(
    X,
    y_return,
    y_class,
    feature_columns
):

    # ==========================================
    # Time Series Split (No Shuffle)
    # ==========================================

    X_train, X_test, y_train_return, y_test_return = train_test_split(
        X,
        y_return,
        test_size=0.2,
        shuffle=False
    )

    _, _, y_train_class, y_test_class = train_test_split(
        X,
        y_class,
        test_size=0.2,
        shuffle=False
    )

    # ==========================================
    # Regression Model
    # ==========================================

    price_model = LGBMRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=6,
        random_state=42
    )

    price_model.fit(
        X_train,
        y_train_return
    )

    pred_return = price_model.predict(X_test)

    # ==========================================
    # Classification Model
    # ==========================================

    direction_model = LGBMClassifier(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=6,
        random_state=42
    )

    direction_model.fit(
        X_train,
        y_train_class
    )

    pred_class = direction_model.predict(X_test)

    # ==========================================
    # Evaluation
    # ==========================================

    print("\n" + "="*60)
    print("REGRESSION RESULTS")
    print("="*60)

    print(f"MAE : {mean_absolute_error(y_test_return,pred_return):.6f}")

    rmse = mean_squared_error(
        y_test_return,
        pred_return
    ) ** 0.5

    print(f"RMSE : {rmse:.6f}")

    print(f"R² : {r2_score(y_test_return,pred_return):.4f}")

    print("\n" + "="*60)
    print("CLASSIFICATION RESULTS")
    print("="*60)

    print(f"Accuracy : {accuracy_score(y_test_class,pred_class):.4f}")

    print(f"Precision : {precision_score(y_test_class,pred_class):.4f}")

    print(f"Recall : {recall_score(y_test_class,pred_class):.4f}")

    print(f"F1 Score : {f1_score(y_test_class,pred_class):.4f}")

    # ==========================================
    # Save Models
    # ==========================================

    os.makedirs("models", exist_ok=True)

    joblib.dump(
        price_model,
        "models/price_model.pkl"
    )

    joblib.dump(
        direction_model,
        "models/direction_model.pkl"
    )

    joblib.dump(
        feature_columns,
        "models/feature_columns.pkl"
    )

    print("\nModels Saved Successfully!")

    return price_model, direction_model