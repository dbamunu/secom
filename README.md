## Summary:
Data from a semi-conductor manufacturing process at SECOM.
SECOM Dataset: 1567 examples 591 features, 104 fails.
Dataset: McCann, M. & Johnston, A. (2008). SECOM [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C54305.

## Project deliverables:

1. Business problem and analytical objectives: Define the business problem, prediction target and success criteria.
2. Data quality and exploratory analysis: Investigate missing values, distributions, outliers, class imbalance and relationships between variables.
3. Statistical investigation: Investigate differences between defective and non-defective products and identify potentially informative features.
4. Predictive modelling: Develop baseline and improved classification models.
5. Model evaluation: Evaluate precision, recall, F1-score, confusion matrix, ROC-AUC and PR-AUC. Explain the trade-offs.
6. Business recommendations: Explain how the model could support quality control, including limitations and recommendations for deployment.


- FSmethod (40 features) BER % True + % True - %
- S2N (signal to noise) 34.5 +-2.6 57.8 +-5.3 73.1 +2.1
- Ttest 33.7 +-2.1 59.6 +-4.7 73.0 +-1.8
- Relief 40.1 +-2.8 48.3 +-5.9 71.6 +-3.2
- Pearson 34.1 +-2.0 57.4 +-4.3 74.4 +-4.9

