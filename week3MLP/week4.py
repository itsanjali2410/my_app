from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names )


print(df.shape)
print(df.head())
X = df  # Features (No need to drop 'target')
y = data.target  # Target values (house prices)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, shuffle=False)
print("X_test shape:", X_test.shape)

# Retrieve the 'HouseAge' value from the third sample of the test set
house_age_value = X_test.iloc[2]['HouseAge']
print(f"The value of house age in the third sample of the test set is: {house_age_value}")

population_value = X_train.iloc[0]['Population']
print(f"The value of Population in the first sample of the training set is: {population_value}")

mean_target_train = np.mean(y_train)

print(f"The mean of the output label in the training set is: {mean_target_train}")