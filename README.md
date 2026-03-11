# UVA Stock Selection Datathon

Welcome to the **University of Virginia Stock Selection Datathon**.

In this challenge, participants will build machine learning models to predict stock returns using historical financial data and engineered features.

The goal is to develop a model that **identifies stocks likely to outperform the market**.

---

# 🌐 Event Website

The datathon website is hosted using GitHub Pages:

https://jacksonshaiz.github.io/Mock-Datathon/

The website contains:

* competition overview
* dataset description
* modeling framework
* submission instructions
* evaluation criteria

---

# 🎯 Objective

Participants will develop a **machine learning model** that predicts future stock returns.

Using model predictions, teams should:

1. Predict stock returns
2. Rank stocks based on predicted returns
3. Construct a portfolio of the highest ranked stocks

---

# 📊 Dataset

Participants will receive a dataset containing historical stock prices and engineered financial indicators.

Dataset location:

```
data/Stock_Data.csv
```

### Dataset Size

* ~590 observations
* 11 variables

### Dataset Columns

| Column       | Description                  |
| ------------ | ---------------------------- |
| Date         | Trading date                 |
| Close        | Closing stock price          |
| Return       | Daily stock return           |
| lag_1        | Return from previous day     |
| lag_2        | Return from two days prior   |
| lag_3        | Return from three days prior |
| lag_5        | Return from five days prior  |
| MA_3         | 3-day moving average         |
| MA_5         | 5-day moving average         |
| Volatility_5 | 5-day rolling volatility     |
| Ticker       | Stock ticker symbol          |

### Prediction Task

Participants should predict stock performance using features such as:

```
lag_1
lag_2
lag_3
lag_5
MA_3
MA_5
Volatility_5
```

The goal is to **predict stock returns and rank stocks by expected performance**.

---

# 🧠 Baseline Model: Random Forest Regression

The recommended baseline model is a **Random Forest Regression model**.

Example implementation:

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

data = pd.read_csv("data/Stock_Data.csv")

features = [
"lag_1",
"lag_2",
"lag_3",
"lag_5",
"MA_3",
"MA_5",
"Volatility_5"
]

X = data[features]
y = data["Return"]

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
n_estimators=200,
max_depth=10,
random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

Teams are encouraged to experiment with additional models and feature engineering.

---

# 📦 Deliverables

Each team must submit the following materials.

### 1. Predicted Returns File

CSV file containing predicted returns.

Example:

```
ticker,predicted_return
AAPL,0.032
MSFT,0.027
NVDA,0.041
```

---

### 2. Portfolio Selection

Teams must submit a ranked list of the top stocks selected by their model.

Example:

```
Top 10 Stocks

1. NVDA
2. MSFT
3. AAPL
4. AMZN
5. META
```

---

### 3. Model Description

Short document explaining:

* modeling approach
* feature engineering
* training process
* evaluation method

Recommended length: **1–2 pages**.

---

### 4. Code Repository

Teams must submit a GitHub repository containing:

* data preprocessing code
* feature engineering code
* model training scripts
* prediction scripts

The repository should include a clear README explaining how to run the code.

---

# 🏆 Evaluation Criteria

Submissions will be evaluated using the following criteria.

### Model Performance — 40%

Accuracy of predicted returns.

Metrics may include:

* Mean Squared Error (MSE)
* directional accuracy

---

### Portfolio Performance — 30%

Performance of the selected portfolio relative to a benchmark index.

---

### Feature Engineering & Methodology — 20%

Judges will evaluate:

* feature engineering
* modeling approach
* validation strategy

---

### Code Quality & Reproducibility — 10%

Submissions should include:

* well-organized code
* documentation
* reproducible workflow

---

# 📁 Repository Structure

```
Mock-Datathon
│
├── docs
│   └── index.html
│
├── data
│   └── Stock_Data.csv
│
├── notebooks
│
└── README.md
```

---

# 🏫 Host

University of Virginia
Mock Datathon Project

