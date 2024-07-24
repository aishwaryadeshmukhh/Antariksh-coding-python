# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv('default.csv')

#display first rows
print(data.head())

#assign data, and assume loan_default is the value for preciction
X = data[['loan_amount', 'interest', 'age', 'property_value', 'credit_score', 'term']]
y = data['loan_default']

X__train, X__test, y__train, y__test = train_test_split(X, y, test_size=0.2, random_state=42)

#train model
model = LinearRegression()
model.fit(X__train, y__train)

#predictions
y__pred = model.predict(X__test)

#Accuracy-%error
e = mean_squared_error(y__test, y__pred)
print(f"Error: {e}")

# Plotting 
#for simplicity we plot one feature vs predicted values
plt.scatter(X_test['loan_amount'], y_test, color='blue', label='Actual')
plt.scatter(X_test['loan_amount'], y_pred, color='red', label='Predicted')
plt.xlabel('Loan Amount')
plt.ylabel('Default')
plt.title('Actual vs. Predicted Default')
plt.legend()
plt.show()
