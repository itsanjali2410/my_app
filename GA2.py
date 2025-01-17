
from sklearn.datasets import load_breast_cancer

# Load the dataset
data = load_breast_cancer()

# Get the feature matrix shape
print(data.data.shape)

#display the dataset details 
print(data.DESCR)

#library used for mathematical calculations 
import numpy as np 
#Here for beging patient target is 1
print(f"benign patient : {np.sum(data.target == 1)}")

#for malignant patient the target given as 0
print(f"malignant patient: {np.sum(data.target == 0)}")

from sklearn.datasets import fetch_california_housing
data = fetch_california_housing()
print(data.DESCR)
print(data.data.shape)
print(f"first five features name : {data.feature_names[:5]}")
print(f"target label: {data.target_names}")