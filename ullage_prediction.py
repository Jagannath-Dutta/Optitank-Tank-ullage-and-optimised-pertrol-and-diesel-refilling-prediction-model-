import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\Projects\Tank ullage and optimised pertrol and diesel refilling prediction model\ullage_prediction.csv')

features = df[['temperature', 'humidity', 'pressure', 'fill_level']]
ullage = df['ullage']

X_train, X_test, y_train, y_test = train_test_split(features, ullage, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

plt.scatter(y_test, predictions)
plt.xlabel('Actual Ullage')
plt.ylabel('Predicted Ullage')
plt.title('Tank Ullage Prediction')
plt.show()

print("Actual Ullage vs Predicted Ullage:")
for i in range(10):
    print(f"Sample {i+1}: Actual Ullage = {y_test.iloc[i]}, Predicted Ullage = {predictions[i]}")
