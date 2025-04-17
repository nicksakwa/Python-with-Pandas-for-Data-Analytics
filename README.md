<p align="center">
  <img src="your-cover-image-url.png" alt="Data Analytics with Pandas Cover" width="800">
</p>

# Data Analytics with Python Pandas

This repository explores the fundamentals of data analytics using the powerful Python Pandas library.

Pandas is a cornerstone library for Data Science and Data Analytics, essential for:

* **Reading Data:** Loading data from various formats like CSV files, Excel sheets, JSON data, and SQL databases.
* **Analyzing Data:** Performing exploratory data analysis and gaining insights.
* **Cleaning Data:** Handling missing values, duplicates, and inconsistencies.
* **Visualizing Data:** Creating informative plots and charts directly from DataFrames.

## Prerequisites

Before diving into this repository, ensure you have the following installed:

1.  **Python:** Download the latest version from the [official Python website](https://www.python.org/downloads/).
2.  **Pandas:** Install the library using pip in your terminal:
    ```bash
    pip install pandas
    ```

## How to Run Examples

To execute the Python scripts in this repository:

1.  Navigate to the directory containing the `.py` files in your terminal.
2.  Run the desired script using the Python interpreter:
    ```bash
    python filename.py
    ```
    (Replace `filename.py` with the actual name of the script).

## Key Pandas Methods Explored

This repository demonstrates the usage of various essential Pandas methods, including:

### Data Inspection

* **`head()`:** Displays the first few rows of a DataFrame (`df.head()`).
* **`tail()`:** Displays the last few rows of a DataFrame (`df.tail()`).
* **`info()`:** Provides a concise summary of the DataFrame, including data types and non-null values (`df.info()`).

### Data Cleaning

* **`drop_duplicates()`:** Removes duplicate rows from a DataFrame (`df.drop_duplicates()`).
* **`duplicated()`:** Returns a boolean Series indicating which rows are duplicates (`df.duplicated()`).

### Data Visualization

* **`.plot()`:** Generates various types of plots, with line plots as the default (`df.plot()`).
* **Scatter Plot:** Creates scatter graphs to visualize the relationship between two variables.
* **Histogram:** Generates histogram plots to visualize the distribution of a single variable.

```python
# Example of a simple Pandas plot
import pandas as pd
import matplotlib.pyplot as plt

data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 1, 3, 5]}
df = pd.DataFrame(data)
df.plot(x='x', y='y', kind='line', title='Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
