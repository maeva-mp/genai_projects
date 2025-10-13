# Exercise 1:  Loan Default Prediction

## Problem Statement
The Goal of this projet is to build a machine learning model to predict if someone will fail to repay a loan. By looking at past data, the model will help banks make better lending choices, avoid losses, and manage loans more safely.ML will learn from patterns in personal details, financial habits, and loan information.


## Data Collection:
Types of Data Needed:

1.Personal Information
*   Age
*   Gender
*   Address
*   Employment status

2.Financial Details

*   Annual Income
*   Credit Score
*   Debt-to-income ratio
*   Number of existing loans

3.Loan Information

*   Loan amount
*   Interest rate
*   Loan term(duration)
*   Loan purpose(eg. car/home/personal...)

4.Repayment History

*   On-tine payments
*   Missed or late payment
*   Number of defaults
*   Account activity over time

## Data Sources
1.Internal Bank Records

- Historical loan applications
- Repayment logs
- Customer profiles

2.Credit Bureau

- Credit scores
- Credit history reports
- Default records

3.Public Datasets

- Open financial datasets (e.g., LendingClub, Kaggle)
- Government financial statistics

4.Third-Party APIs

- Real-time financial data
- Income verification services
- Fraud detection tools


# Exercise 2: Feature Selection and Model Choice

Feature Selection

1. Credit Score
- Indicates how reliable a borrower is based on past financial behavior
- Lower scores often mean higher risk of default

2. Annual Income
- Helps assess the borrower’s ability to repay the loan
- Higher income usually means lower risk

3. Debt-to-Income Ratio
- Shows how much debt the borrower already has compared to their income
- A high ratio may signal financial stress

4. Loan Amount
- Larger loans may be harder to repay
- Important for understanding repayment burden

5. Loan Purpose
- Some loan types (e.g., personal loans) may carry higher risk
- Helps categorize risk based on intent

6. Repayment History
- Past missed or late payments are strong indicators of future default
- Directly reflects borrower behavior

7. Employment Status
- Stable employment reduces the chance of income loss
- Unemployment or unstable jobs increase risk

8. Loan Term
- Longer terms may increase risk due to changing financial conditions
- Shorter terms often mean quicker repayment

# Justification
- These features are directly linked to financial health, repayment ability, and loan risk
- They are quantitative, making them suitable for machine learning models
- Using fewer but more relevant features improves model accuracy and efficiency
- Helps avoid overfitting and reduces noise in the dat


# Exercise 3: Training, Evaluating, and Optimizing the Model


## Model Choice for Loan Default Prediction

1. Logistic Regression
- Simple and interpretable
- Good for binary classification (default vs. no default)

2. Random Forest
- Handles nonlinear relationships
- Robust to overfitting and works well with mixed data types

3. XGBoost
- High accuracy and performance
- Great for handling missing data and complex patterns

## Model Evaluation Steps

1. Split the Data
- Divide into training and test sets 
- Optionally use a validation set or cross-validation

2. Train the Model
- Fit the model on the training data
- Tune hyperparameters to improve performance

3. Make Predictions
- Use the test set to generate predictions
- Compare predicted vs. actual outcomes

4. Evaluate Using Metrics
Accuracy - Overall correctness of predictions
Precision - How many act wereual positive predictions were correct
Recall - How many actual values arde correctly predicted
F1 Score - Balance between precision and recall

5. Optimize the Model
- Use grid search or random search to tune hyperparameters

# Exercise 4 :  Designing Machine Learning Solutions for Specific Problems

1.Predicting Stock Prices : predict future prices
Type of ML : Supervised Learning
Explanation: model learns from labeled data - where input data(past data) - output(actual future price).

2.Organising a Library of Books
Type of ML : Unsupervised Learning
Explanation : group books into genres/ categories based on similarities in content or keywords without predefined labels. Model finds patterns and clusters in the data by itself.

3.Programming a Robot to Navigate a Maze
Type of ML : Reinforcement Learning 
Explanation : Robot learns by trial and error -  receiving rewards for correct moves and penalties for wrong ones. It gradually learns the most effective route by choosing actions that maximize its total reward.


# Exercise 5 : Designing an Evaluation Strategy for Different ML Models

## Selection of three ML models : 
- supervised learning : classification
- unsupervised learning : clustering

1.Supervised model : Classification
Evaluation Strategy: 
Accuracy : out of all predictions, how many number of correcteness.
Precision : how many prediction were actually correct
Recall : how many actual predictions are correctly predicted
F1-Score : Balance between precision and recall.

## Methods:
Train/Test Split : Divide ddata to test generalization.
Cross-Validation : Rotate training/testing across folds to reduce bias.

2.Unsupervised model : Clustering
Evaluation Strategy:
