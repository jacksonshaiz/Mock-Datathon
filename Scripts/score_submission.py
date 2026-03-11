import pandas as pd
from sklearn.metrics import mean_squared_error

# Load ground truth data
true_data = pd.read_csv("data/Stock_Data.csv")

# Load submission
submission = pd.read_csv("submission.csv")

# Merge predictions with true returns
merged = pd.merge(
    submission,
    true_data[["Ticker","Return"]],
    left_on="ticker",
    right_on="Ticker"
)

# Calculate MSE
mse = mean_squared_error(merged["Return"], merged["predicted_return"])

print("Submission Score")
print("----------------")
print("Mean Squared Error:", mse)

# Portfolio evaluation
top10 = submission.sort_values(
    "predicted_return",
    ascending=False
).head(10)

portfolio = pd.merge(
    top10,
    true_data[["Ticker","Return"]],
    left_on="ticker",
    right_on="Ticker"
)

portfolio_return = portfolio["Return"].mean()

print("Top 10 Portfolio Return:", portfolio_return)
