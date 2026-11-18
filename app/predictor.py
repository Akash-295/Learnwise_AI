
import joblib
import pandas as pd
import logging

from pathlib import Path

logger = logging.getLogger(__name__)

# Locate the project directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models" / "learnwise_model.joblib"


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


# Load model safely
try:
    model = load_model()
    model_load_error = None

except Exception as error:
    model = None
    model_load_error = error

    logger.exception("Failed to load the machine learning model.")


def predict_student_outcome(student_data):

    if model is None:
        raise RuntimeError(
            "The machine learning model is currently unavailable."
        ) from model_load_error

    input_df = pd.DataFrame([student_data])

    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    class_names = model.named_steps["classifier"].classes_

    probability_results = {
        class_name: round(float(probability) * 100, 2)
        for class_name, probability in zip(
            class_names,
            probabilities
        )
    }

    return {
        "prediction": prediction,
        "probabilities": probability_results
    }
