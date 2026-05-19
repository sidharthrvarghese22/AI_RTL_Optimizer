import pandas as pd
from sklearn.linear_model import LinearRegression

# Load training dataset
data = pd.read_csv("datasets/training_data.csv")

# Input features
X = data[["adders", "multipliers"]]

# Target output
y = data["delay"]

# Train ML model
model = LinearRegression()

model.fit(X, y)

# Predict delay
prediction = model.predict([[2, 1]])

print("\n===== ML DELAY PREDICTION =====\n")
print("Predicted Delay:", prediction[0])