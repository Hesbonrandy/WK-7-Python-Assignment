# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Clean dataset (Iris has no missing values, but demonstrate handling)
if df.isnull().sum().sum() > 0:
    # Fill missing numerical values with column mean
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col].fillna(df[col].mean(), inplace=True)
    print("Missing values filled with column means.")
else:
    print("No missing values to handle.")

# Basic statistics of numerical columns
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Group by species and compute mean of numerical columns
print("\nMean values by species:")
grouped = df.groupby('species').mean()
print(grouped)

# Create 4 required visualizations

# 1. Line chart (simulated trend by sorting data)
df_sorted = df.sort_values('sepal length (cm)').reset_index()
plt.figure(figsize=(10, 6))
plt.plot(df_sorted.index, df_sorted['petal length (cm)'], label='Petal Length', marker='o')
plt.plot(df_sorted.index, df_sorted['petal width (cm)'], label='Petal Width', marker='s')
plt.title('Trend of Petal Dimensions (Ordered by Sepal Length)')
plt.xlabel('Sample Index')
plt.ylabel('Measurement (cm)')
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(8, 6))
species_means = df.groupby('species')['petal length (cm)'].mean()
plt.bar(species_means.index, species_means.values, color=['red', 'green', 'blue'], alpha=0.7)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 3. Histogram (distribution of petal length)
plt.figure(figsize=(8, 6))
plt.hist(df['petal length (cm)'], bins=15, edgecolor='black', color='steelblue')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(8, 6))
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal length (cm)'], subset['petal length (cm)'], 
                label=species, alpha=0.7)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.grid(True)
plt.show()

# Final observations 
print("\n=== OBSERVATIONS ===")
print("1. Setosa species has the smallest petal dimensions.")
print("2. Virginica has the largest petal dimensions.")
print("3. Petal length is strongly correlated with species type.")
print("4. The scatter plot shows clear separation between species, especially Setosa.")