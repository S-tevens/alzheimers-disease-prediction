import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("alzheimers_disease_data.csv")

X = dataset.iloc[:,:-1].values 
y = dataset.iloc[:-1].values

# Viewing the first few rows
print(dataset.head())

# Checking for missing values
print(dataset.isnull().sum())

# Checking the column names
print(dataset.columns)
