# 🎓 LearnWise AI
### Student Academic Outcome Prediction Using Machine Learning

LearnWise AI is a machine learning-powered educational analytics application that predicts students' academic outcomes based on demographic, enrollment, academic, and socioeconomic information.

The application estimates one of three possible outcomes:

- **Graduate** – The student successfully completes the academic programme.
- **Dropout** – The student discontinues the academic programme.
- **Enrolled** – The student remains enrolled.

The project aims to demonstrate how machine learning can support educational analytics and help institutions identify students who may benefit from additional academic support.

## 🚀 Key Features

- Student academic outcome prediction.
- Three-class classification: Graduate, Dropout, and Enrolled.
- Estimated class probability visualization.
- Interactive Streamlit interface.
- Human-readable categorical feature labels.
- Input validation for logically inconsistent academic information.
- Contextual explanations for predictions.
- Academic support recommendations.
- Student information summary.
- Model evaluation and transparency information.
- Logging and user-friendly error handling.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and preprocessing |
| Joblib | Model serialization and loading |
| Streamlit | Interactive web application |
| Matplotlib / Seaborn | Exploratory data visualization |

## 📊 Dataset

This project uses the **Predict Students' Dropout and Academic Success** dataset from the UCI Machine Learning Repository.

Dataset characteristics:

- 4,424 student records.
- 37 original columns.
- Demographic information.
- Academic performance information.
- Enrollment-related information.
- Socioeconomic indicators.

**Target variable:** Target

The target contains three classes:

- Graduate
- Dropout
- Enrolled

## 🤖 Machine Learning Model

LearnWise AI uses a trained machine learning classification pipeline to predict academic outcomes.

The model processes student information and generates:

- A predicted academic outcome.
- Estimated probabilities for all three outcome classes.

### Model Evaluation

| Evaluation Metric | Result |
|---|---:|
| Test Accuracy | 70.96% |
| Macro F1-Score | 66.11% |

Accuracy measures overall prediction correctness, while Macro F1 evaluates performance across all classes with equal importance.

## 📁 Project Structure

```text
LearnWise-AI/
│
├── app/
│   ├── main.py
│   ├── predictor.py
│   ├── category_labels.py
│   └── feature_config.json
│
├── models/
│   └── learnwise_model.joblib
│
├── README.md
└── requirements.txt
```

*Additional files used for training, exploration, or dataset storage may also be present in the project.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Akash-295/Learnwise_AI.git
```

### 2. Navigate to the project directory

```bash
cd LearnWise-AI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app/main.py
```

The application will be available at:

```text
http://localhost:8501
```

## 📌 How to Use

1. Open the LearnWise AI application.
2. Enter the student's demographic and enrollment information.
3. Select the attendance schedule.
4. Enter academic performance and economic information.
5. Submit the student information.
6. View the predicted academic outcome.
7. Explore the estimated class probabilities.
8. Review the prediction explanation and academic support recommendations.

## ⚠️ Limitations and Responsible Use

- Predictions are estimates, not guaranteed academic outcomes.
- Model performance may differ when applied to students from other institutions or populations.
- The model was trained using historical educational data.
- Estimated class probabilities should not automatically be interpreted as calibrated individual risks.
- Predictions should not be used as the sole basis for admission, academic, or administrative decisions.
- Human judgment and individual student circumstances must always be considered.

## 🎯 Project Objective

LearnWise AI was developed as a practical machine learning portfolio project to demonstrate the application of data preprocessing, classification, model evaluation, prediction pipelines, and interactive deployment.

## 👨‍💻 Author

**AKASH**

Machine Learning Portfolio Project

---

*LearnWise AI — Turning Educational Data into Meaningful Insights.*