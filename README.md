# UVA Stock Selection Datathon

This repository hosts the **UVA Stock Selection Datathon**, a quantitative finance challenge where participants build machine learning models to identify high-performing stocks.

The goal of the datathon is to develop predictive models that estimate future stock returns and construct portfolios that outperform the market.

## 🌐 Event Website

The official datathon website can be viewed here:

https://jacksonshaiz.github.io/Mock-Datathon/

The site contains:

* Competition overview
* Model framework
* Dataset description
* Submission instructions

## 🎯 Objective

Participants will build a **machine learning model** that predicts future stock returns using historical financial data and engineered technical indicators.

Teams will then **rank stocks based on predicted returns** and construct a portfolio using the highest-ranked assets.

## 🧠 Baseline Model: Random Forest Regression

The recommended baseline model for the competition is a **Random Forest Regressor**.

The model should learn the relationship between financial indicators and future returns.

Typical pipeline:

1. Data collection
2. Feature engineering
3. Model training
4. Portfolio ranking

Example implementation:

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

data = pd.read_csv("stock_features.csv")

X = data.drop("future_return", axis=1)
y = data["future_return"]

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

## 📊 Feature Engineering

Participants are encouraged to engineer features such as:

* Moving averages (MA10, MA50)
* Relative Strength Index (RSI)
* Momentum indicators
* Volatility measures
* Trading volume trends

Additional macroeconomic or market features may also be incorporated.

## 📁 Repository Structure

```
Mock-Datathon
│
├── docs/            # Datathon website (GitHub Pages)
│   └── index.html
│
├── data/            # Dataset
├── notebooks/       # Exploration and experiments
├── src/             # Model code
└── README.md
```

## 📥 Submission Requirements

Each team should submit:

* Predicted returns for each stock
* Ranked portfolio
* Model description
* Source code

Submissions should be provided via GitHub repository.

## 🏫 Host

University of Virginia
Mock Datathon Project

---

If you have questions or issues, please open an issue in this repository.
