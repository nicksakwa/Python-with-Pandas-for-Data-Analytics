<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*RsPKgwrJO-h9DBovrcVBLA.jpeg" alt="Data Analytics Cover photo for python pandas library" width="800">
</p>

# Python with Pandas for Data 

In this GitHub repository, I discuss data analytics with the Python Pandas library.

Pandas is a  core library used for reading, analyzing, cleaning, and visualizing data from CSV files, excel sheets, JSON data, and SQL databases.

* **Reading Data:** Loads data from dataset formats such as CSV files, Excel sheets, JSON data, and SQL databases.
* **Analyzing Data:** Generating insights.
* **Cleaning Data:** Dealing with missing rows and columns from data, duplicates, inconsistencies, and other errors.
* **Visualizing Data:** Generating charts and graphs from Data.

## For this repository, the prerequisites are:

Before diving into this repository, ensure you have the following installed:

1.  **Python:** Which you can download from the [official Python website](https://www.python.org/downloads/).
2.  **Pandas:** Install the library using pip in your bash terminal or your directory:
    ```bash
    pip install pandas
    ```

## How to Run Examples

To execute the Python scripts in this repository:

1.  Navigate to the directory containing the .py` files in your terminal.
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


