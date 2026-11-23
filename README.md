# Manufacturing Quality Prediction – SECOM Dataset

## Project Summary

This project investigates the application of statistical analysis and machine learning to predict manufacturing quality failures using the SECOM semiconductor manufacturing dataset from the UCI Machine Learning Repository.

The dataset contains measurements collected during a semiconductor manufacturing process. The objective is to analyse manufacturing process data, identify potentially informative sensor measurements and develop predictive models to distinguish between successful and failed quality outcomes.

### Dataset Overview

- **Observations:** 1,567 manufacturing records
- **Input features:** 590 process measurement variables
- **Target variable:** Manufacturing quality outcome (pass or fail)
- **Failed observations:** 104
- **Passed observations:** 1,463

The dataset presents several analytical challenges, including missing values, a high-dimensional feature space and an imbalanced target variable.

**Dataset source:**

McCann, M. & Johnston, A. (2008). SECOM [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C54305.

## Project Objectives and Deliverables

### 1. Business Problem and Analytical Objectives
- Define the manufacturing quality prediction problem.
- Identify the prediction target and relevant business objectives.
- Establish appropriate model evaluation criteria based on the cost of missed quality failures and false alarms.

### 2. Data Quality Assessment and Exploratory Data Analysis
- Assess data completeness and missing-value patterns.
- Investigate feature distributions and potential outliers.
- Analyse target class distribution and class imbalance.
- Explore relationships and correlations between process measurements.

### 3. Statistical Analysis and Feature Investigation
- Investigate differences in process measurements between passing and failing observations.
- Apply appropriate statistical tests to identify potentially informative features.
- Examine feature relationships, redundancy and potential multicollinearity.
- Assess the implications of statistical findings for feature selection.

### 4. Predictive Model Development
- Establish a baseline classification model.
- Develop and compare suitable machine learning classification algorithms.
- Investigate feature selection and class imbalance handling techniques.
- Apply appropriate preprocessing and cross-validation strategies.

### 5. Model Evaluation and Comparison
Evaluate model performance using:
- Precision and recall
- F1-score
- Confusion matrix
- ROC-AUC
- Precision-Recall AUC (PR-AUC)

Compare models and discuss the trade-offs between detecting manufacturing failures and generating false alarms.

### 6. Business Recommendations and Limitations
- Translate model findings into actionable manufacturing quality-control recommendations.
- Discuss how predictive insights could support inspection and process monitoring.
- Identify model limitations, data constraints and potential deployment considerations.
