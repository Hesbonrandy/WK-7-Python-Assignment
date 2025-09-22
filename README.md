# 🌸 Iris Dataset Analysis

This project performs **exploratory data analysis (EDA)** on the classic **Iris dataset** using Python.  
It includes data cleaning, descriptive statistics, grouping by species, and four types of visualizations.

---

## 🛠️ Libraries Used
- `pandas` – Data manipulation and analysis  
- `matplotlib` – Data visualization  
- `scikit-learn` – Loading the Iris dataset  
- `numpy` – Numerical computations  

---

## 📂 Dataset
The **Iris dataset** contains 150 samples of iris flowers from three species:
- Setosa  
- Versicolor  
- Virginica  

Each sample has four features:  
- Sepal length (cm)  
- Sepal width (cm)  
- Petal length (cm)  
- Petal width (cm)  

---

## 🔍 Steps Performed
1. Load the dataset into a Pandas DataFrame.  
2. Display the first 5 rows of the dataset.  
3. Check data types and missing values.  
4. Clean data (fill missing values if any).  
5. Compute basic statistics of numerical columns.  
6. Group by species and compute mean values.  
7. Create visualizations:
   - **Line chart** – Trends of petal length and width ordered by sepal length.  
   - **Bar chart** – Average petal length per species.  
   - **Histogram** – Distribution of petal length.  
   - **Scatter plot** – Sepal length vs petal length colored by species.  

---

## 📊 Visualizations

### 1. Line Chart
Shows the trend of petal length and width based on sorted sepal length.

### 2. Bar Chart
Compares the average petal length for each species.

### 3. Histogram
Displays the distribution of petal length across all samples.

### 4. Scatter Plot
Plots sepal length vs petal length with different colors for each species.

---

## 📝 Observations
1. **Setosa** species has the smallest petal dimensions.  
2. **Virginica** has the largest petal dimensions.  
3. Petal length is strongly correlated with species type.  
4. Scatter plot shows clear separation between species, especially Setosa.  

---

## ▶️ How to Run
1. Clone the repository.  
2. Install required libraries:
```bash
pip install pandas matplotlib scikit-learn numpy
