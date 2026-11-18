
import streamlit as st
import json
import sys
import pandas as pd
import logging
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
    
from app.category_labels import CATEGORY_LABELS, BINARY_LABELS

logger = logging.getLogger(__name__)

def format_category(value, labels):
    try:
        numeric_value = int(value)
    except (TypeError, ValueError):
        numeric_value = value

    return labels.get(
        numeric_value,
        labels.get(
            str(numeric_value),
            f"Code {value}"
        )
    )

def get_academic_recommendations(prediction):

    recommendations = {
        "Graduate": {
            "title": "Continue building academic excellence",
            "items": [
                "Maintain consistent study habits.",
                "Explore internships and practical projects.",
                "Develop communication and professional skills.",
                "Prepare for higher education or career opportunities."
            ]
        },

        "Enrolled": {
            "title": "Support continued academic progress",
            "items": [
                "Create a structured semester-wise study plan.",
                "Monitor attendance and assignment completion.",
                "Seek faculty guidance when facing difficult subjects.",
                "Use peer learning groups and academic resources."
            ]
        },

        "Dropout": {
            "title": "Prioritize additional academic support",
            "items": [
                "Arrange a discussion with an academic advisor.",
                "Identify subjects or academic areas needing support.",
                "Explore tutoring and mentoring opportunities.",
                "Discuss financial or personal barriers with appropriate college support services.",
                "Create a realistic plan for continuing education."
            ]
        }
    }

    return recommendations.get(prediction)

def get_prediction_explanation(prediction):
    explanations = {
        "Graduate": (
            "The model estimates that this student is most likely "
            "to successfully complete their academic programme."
        ),
        "Dropout": (
            "The model estimates that this student may be at risk "
            "of leaving their academic programme."
        ),
        "Enrolled": (
            "The model estimates that this student is likely to "
            "remain enrolled without yet completing the programme."
        )
    }

    return explanations.get(
        prediction,
        "The model generated an outcome that could not be explained."
    )

NUMERICAL_HELP = {
    "Previous qualification (grade)": (
        "Grade obtained in the student's previous qualification."
    ),
    "Admission grade": (
        "Grade obtained by the student during the admission process."
    ),
    "Age at enrollment": (
        "Student's age when enrolling in the academic programme."
    ),
    "Curricular units 1st sem (credited)": (
        "Number of first-semester curricular units credited to the student."
    ),
    "Curricular units 1st sem (enrolled)": (
        "Total curricular units in which the student enrolled during the first semester."
    ),
    "Curricular units 1st sem (evaluations)": (
        "Number of evaluation events during the first semester."
    ),
    "Curricular units 1st sem (approved)": (
        "Number of first-semester curricular units successfully approved."
    ),
    "Curricular units 1st sem (grade)": (
        "Average grade obtained in first-semester curricular units."
    ),
    "Curricular units 1st sem (without evaluations)": (
        "Number of curricular units without evaluation results."
    ),
    "Unemployment rate": (
        "Unemployment rate recorded in the dataset's economic context."
    ),
    "Inflation rate": (
        "Inflation rate recorded in the dataset's economic context."
    ),
    "GDP": (
        "Gross Domestic Product indicator recorded in the dataset's economic context."
    )
}


CATEGORICAL_HELP = {
    "Marital status": (
        "The student's marital status at the time of enrollment."
    ),
    "Application mode": (
        "The admission or application method used by the student."
    ),
    "Application order": (
        "The order or preference associated with the student's application."
    ),
    "Course": (
        "The academic programme or course selected by the student."
    ),
    "Previous qualification": (
        "The student's highest previous educational qualification."
    ),
    "Nacionality": (
        "The nationality category recorded in the original dataset."
    ),
    "Mother's qualification": (
        "The educational qualification of the student's mother."
    ),
    "Father's qualification": (
        "The educational qualification of the student's father."
    ),
    "Mother's occupation": (
        "The occupation category recorded for the student's mother."
    ),
    "Father's occupation": (
        "The occupation category recorded for the student's father."
    ),
    "Displaced": (
        "Indicates whether the student is classified as displaced "
        "in the original dataset."
    ),
    "Educational special needs": (
        "Indicates whether the student has recorded educational "
        "special needs."
    ),
    "Debtor": (
        "Indicates whether the student is recorded as having "
        "outstanding financial debt."
    ),
    "Tuition fees up to date": (
        "Indicates whether the student's tuition fee payments "
        "are up to date."
    ),
    "Gender": (
        "The gender category recorded in the original dataset."
    ),
    "Scholarship holder": (
        "Indicates whether the student holds a scholarship."
    ),
    "International": (
        "Indicates whether the student is classified as an "
        "international student."
    )
}

def validate_student_data(student_data):

    errors = []

    enrolled = student_data["Curricular units 1st sem (enrolled)"]
    approved = student_data["Curricular units 1st sem (approved)"]
    without_evaluations = student_data[
        "Curricular units 1st sem (without evaluations)"
    ]

    if approved > enrolled:
        errors.append(
            "Approved curricular units cannot exceed enrolled curricular units."
        )

    if without_evaluations > enrolled:
        errors.append(
            "Curricular units without evaluations cannot exceed enrolled curricular units."
        )

    if approved + without_evaluations > enrolled:
        errors.append(
            "Approved units and units without evaluations cannot together exceed enrolled units."
        )

    return errors

# --------------------------------------------------
# PROJECT CONFIGURATION
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.predictor import (
    predict_student_outcome,
    model,
    model_load_error
)

CONFIG_PATH = PROJECT_ROOT / "app" / "feature_config.json"

with open(CONFIG_PATH, "r", encoding="utf-8") as file:
    feature_config = json.load(file)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="LearnWise AI",
    page_icon="🎓",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🎓 LearnWise AI")

st.subheader("Student Academic Outcome Prediction")

st.write(
    "An AI-powered educational analytics application "
    "designed to estimate student academic outcomes."
)

st.info(
    "Predictions are statistical estimates for educational "
    "support and research. They are not guarantees or "
    "definitive judgments about individual students."
)

st.divider()


# --------------------------------------------------
# MODEL STATUS
# --------------------------------------------------

if model is not None:
    st.success("Machine learning model loaded successfully!")
else:
    st.error(
        "Machine learning model could not be loaded. "
        "Predictions are currently unavailable."
    )

st.caption(
    "Prediction classes: Dropout | Enrolled | Graduate"
)

st.divider()


# --------------------------------------------------
# STUDENT INPUT FORM
# --------------------------------------------------

st.header("📝 Student Information")

st.markdown(
    "Provide the student's information in the sections below "
    "to generate an estimated academic outcome."
)

st.caption(
    "Complete each section carefully. Hover over the information "
    "icons for explanations of individual fields."
)

student_data = {}

with st.form("student_prediction_form"):

    # ----------------------------------------------
    # CATEGORICAL FEATURES
    # ----------------------------------------------

    st.subheader("1. Student and Enrollment Information")

    st.caption(
        "Enter personal details, admission information, "
        "educational background, and family-related information."
    )

    categorical_columns = feature_config["categorical"]

    categorical_items = list(categorical_columns.items())

    col1, col2 = st.columns(2)

    for index, (column, options) in enumerate(categorical_items):

        with col1 if index % 2 == 0 else col2:

            labels = CATEGORY_LABELS.get(column, {})

            if column in BINARY_LABELS:
                labels = BINARY_LABELS[column]

            student_data[column] = st.selectbox(
                column,
                options=options,
                format_func=lambda value, label_map=labels: format_category(
                    value, label_map
                ),
                key=f"input_{column}",
                help=CATEGORICAL_HELP.get(column)
            )

    # ----------------------------------------------
    # ATTENDANCE FEATURE
    # ----------------------------------------------

    st.divider()

    st.subheader("2. Attendance Information")

    st.caption(
        "Select the student's regular attendance schedule."
    )

    attendance_column, attendance_details = next(
        iter(feature_config["binary_select"].items())
    )

    attendance_options = attendance_details["options"]

    attendance_label = st.selectbox(
        "Attendance Schedule",
        options=list(attendance_options.keys()),
        format_func=lambda value: value
    )

    student_data[attendance_column] = (
        attendance_options[attendance_label]
    )

    # ----------------------------------------------
    # NUMERICAL FEATURES
    # ----------------------------------------------

    st.divider()

    st.subheader("3. Academic and Economic Information")

    st.caption(
        "Enter previous academic grades, first-semester performance, "
        "and relevant economic indicators."
    )

    numerical_columns = feature_config["numerical"]

    numerical_items = list(numerical_columns.items())

    # Attendance is already collected through its dropdown.
    binary_columns = set(feature_config["binary_select"].keys())

    # Exclude attendance from numerical input controls.
    numerical_items = [
        (column, details)
        for column, details in numerical_items
        if column not in binary_columns
    ]


    col1, col2 = st.columns(2)

    # Features that represent whole-number counts or age.
    integer_features = {
        "Age at enrollment",
        "Curricular units 1st sem (credited)",
        "Curricular units 1st sem (enrolled)",
        "Curricular units 1st sem (evaluations)",
        "Curricular units 1st sem (approved)",
        "Curricular units 1st sem (without evaluations)"
    }

    for index, (column, details) in enumerate(numerical_items):

        with col1 if index % 2 == 0 else col2:

            if column in integer_features:

                student_data[column] = st.number_input(
                    column,
                    min_value=int(details["min"]),
                    max_value=int(details["max"]),
                    value=int(details["default"]),
                    step=1,
                    format="%d",
                    help=NUMERICAL_HELP.get(column),
                )

            else:

                student_data[column] = st.number_input(
                    column,
                    min_value=float(details["min"]),
                    max_value=float(details["max"]),
                    value=float(details["default"]),
                    step=0.01,
                    format="%.2f",
                    help=NUMERICAL_HELP.get(column),
                )



    # ----------------------------------------------
    # SUBMIT BUTTON
    # ----------------------------------------------

    st.divider()

    st.subheader("Generate Prediction")

    st.caption(
        "Review the information above before submitting. "
        "LearnWise AI will estimate the student's most likely academic outcome."
    )

    submitted = st.form_submit_button(
        "🔍 Predict Student Outcome",
        width="stretch",
        disabled=model is None
    )


# --------------------------------------------------
# PREDICTION RESULTS
# --------------------------------------------------

if submitted and (validation_errors := validate_student_data(student_data)):

    for error in validation_errors:
        st.error(error)

elif submitted:

    try:

        result = predict_student_outcome(student_data)


        prediction = result["prediction"]
        probabilities = result["probabilities"]

        st.divider()

        st.header("📊 Prediction Results")

        st.subheader("Predicted Academic Outcome")

        if prediction == "Graduate":
            st.success("🎓 Predicted Outcome: Graduate")

        elif prediction == "Dropout":
            st.warning("Predicted Outcome: Dropout")

        else:
            st.info("Predicted Outcome: Enrolled")

        st.caption(
            "This is the model's most likely class, "
            "not a guaranteed student outcome."
        )

        st.subheader("Understanding the Prediction")

        st.write(get_prediction_explanation(prediction))

        st.caption(
            "The probabilities represent the model's estimated class scores. "
            "They are not guaranteed outcomes or necessarily calibrated "
            "probabilities. Actual academic outcomes may differ."
        )

        st.subheader("Estimated Class Probabilities")

        probability_df = pd.DataFrame({
            "Outcome": list(probabilities.keys()),
            "Probability (%)": list(probabilities.values())
        })

        st.bar_chart(
            probability_df,
            x="Outcome",
            y="Probability (%)"
        )

        for outcome, probability in probabilities.items():
            st.write(f"**{outcome}: {probability:.2f}%**")

        # ------------------------------------------
        # RESULT SUMMARY
        # ------------------------------------------

        st.divider()

        st.subheader("Prediction Summary")

        result_col1, result_col2, result_col3 = st.columns(3)

        result_col1.metric(
            "Predicted Outcome",
            prediction
        )

        result_col2.metric(
            "Top Class Probability",
            f"{max(probabilities.values()):.2f}%"
        )

        result_col3.metric(
            "Number of Outcomes",
            len(probabilities)
        )

        st.info(
            "These probabilities are model estimates. "
            "They should not be interpreted as calibrated "
            "individual risks or certainty."
        )

        # ------------------------------------------
        # STUDENT INFORMATION SUMMARY
        # ------------------------------------------

        st.divider()

        with st.expander("📋 View Student Information Used for Prediction"):

            display_student_data = {}

            for column, value in student_data.items():

                # Get category labels
                labels = CATEGORY_LABELS.get(column, {})

                if column in BINARY_LABELS:
                    labels = BINARY_LABELS[column]

                # Handle attendance separately
                if column in feature_config["binary_select"]:

                    attendance_options = (
                        feature_config["binary_select"][column]["options"]
                    )

                    reverse_options = {
                        code: label
                        for label, code in attendance_options.items()
                    }

                    display_value = reverse_options.get(value, value)

                elif labels:

                    display_value = format_category(value, labels)

                else:

                    display_value = value

                display_student_data[column] = str(display_value)

            summary_df = pd.DataFrame(
                list(display_student_data.items()),
                columns=["Student Information", "Submitted Value"]
            )

            st.dataframe(
                summary_df,
                width="stretch",
                hide_index=True
            )

        # ------------------------------------------
        # ACADEMIC SUPPORT RECOMMENDATIONS
        # ------------------------------------------

        st.divider()

        st.header("🎯 Academic Support Recommendations")

        recommendation = get_academic_recommendations(prediction)

        if recommendation:

            st.subheader(recommendation["title"])

            for item in recommendation["items"]:
                st.markdown(f"- {item}")

        st.caption(
            "These suggestions are general educational guidance. "
            "They should be considered alongside the student's "
            "actual academic performance and personal circumstances."
        )

    except Exception:

        logger.exception(
            "An unexpected error occurred while generating a prediction."
        )

        st.error(
            "We couldn't generate a prediction. "
            "Please try again."
        )

        st.info(
            "If the problem continues, please contact the application administrator."
        )


# --------------------------------------------------
# MODEL INFORMATION AND TRANSPARENCY
# --------------------------------------------------

st.divider()

with st.expander("ℹ️ About the Machine Learning Model"):

    st.subheader("Dataset Information")

    st.write(
        "LearnWise AI uses the UCI Student Academic Success "
        "dataset, titled 'Predict Students' Dropout and "
        "Academic Success'."
    )

    st.write(
        "The dataset contains 4,424 student records and "
        "37 original columns. It includes student enrollment, "
        "demographic, academic, and economic information."
    )

    st.subheader("Prediction Categories")

    st.markdown("""
    - **Graduate:** The student completed the academic programme.
    - **Dropout:** The student discontinued the academic programme.
    - **Enrolled:** The student remained enrolled.
    """)

    st.subheader("Model Evaluation")

    metric_col1, metric_col2 = st.columns(2)

    metric_col1.metric(
        "Test Accuracy",
        "70.96%"
    )

    metric_col2.metric(
        "Macro F1-Score",
        "66.11%"
    )

    st.write(
        "Accuracy measures the overall proportion of correct "
        "predictions. Macro F1 calculates the F1-score for "
        "each class and gives every class equal importance."
    )

    st.subheader("Understanding Predictions")

    st.write(
        "The application uses student information to estimate "
        "the most likely academic outcome. The probability chart "
        "shows the model's estimated probabilities for all "
        "three outcome categories."
    )

    st.subheader("Important Limitations")

    st.markdown("""
    - Model predictions are estimates, not guaranteed outcomes.
    - Performance may differ for students from other institutions.
    - The model was trained using historical educational data.
    - Predictions should not be used as the sole basis for
      academic, admission, or administrative decisions.
    - Human judgment and individual student circumstances
      must always be considered.
    """)

    st.caption(
        "LearnWise AI is an educational analytics portfolio "
        "project intended for learning, research, and academic "
        "support."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "LearnWise AI | Machine Learning Portfolio Project"
)
