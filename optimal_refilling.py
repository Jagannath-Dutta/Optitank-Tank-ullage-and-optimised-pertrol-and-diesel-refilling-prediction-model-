import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns

df = pd.read_csv(r"D:\Projects\Tank ullage and optimised pertrol and diesel refilling prediction model\optimal_refillation.csv")

current_time = datetime.now()
time_since_last_refill = timedelta(days=10)
df['last_refill_timestamp'] = current_time - time_since_last_refill

df['time_since_last_refill'] = (current_time - pd.to_datetime(df['last_refill_timestamp'])).dt.days

features = df[['petrol_level', 'diesel_level', 'petrol_drain_rate', 'diesel_drain_rate', 'time_since_last_refill']]
target = df['optimal_refill_amount']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, color='blue', label='Predictions')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', lw=2, label='Actual')
plt.xlabel('Actual Optimal Refill Amount')
plt.ylabel('Predicted Optimal Refill Amount')
plt.title('Optimal Tank Refill Prediction')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
sns.kdeplot(y_test, color='blue', label='Actual Refill Amount', fill=True)
sns.kdeplot(predictions, color='orange', label='Predicted Refill Amount', fill=True)
plt.xlabel('Optimal Refill Amount')
plt.ylabel('Density')
plt.title('Distribution of Actual and Predicted Refill Amounts')
plt.legend()
plt.show()

residuals = y_test - predictions
plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True, color='green')
plt.xlabel('Residuals')
plt.ylabel('Density')
plt.title('Distribution of Residuals')
plt.show()
