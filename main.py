import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


print("Loading data...")
try:
    data = pd.read_csv('housing.csv')
except FileNotFoundError:
    print("Error: housing.csv not found.")
    exit()

data.dropna(inplace=True)
data = data.drop('ocean_proximity', axis=1)
X = data.drop('median_house_value', axis=1)
y = data['median_house_value']
print(f"Training on {X.shape[1]} different features (Income, Age, Rooms, etc.)...")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print("-" * 30)
print(f"R-Squared Score: {r2:.4f}")
print("-" * 30)


plt.figure(figsize=(10, 6))


plt.scatter(y_test, y_pred, alpha=0.5, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linewidth=2)

plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title(f'Actual vs Predicted Prices (Accuracy: {r2:.2f})')
plt.show()