# EDA with pandas
 EDA project 
   ------- DESCRIPTION-------
""" The purpose of this Python script is to analyze sales data
from multiple CSV files, perform data preprocessing, and generate visualizations
to gain insights into sales trends and product performance.

1-Data Concatenation:
The script first creates a list of all the CSV files
containing sales data in a specified directory (folder_path).
It then iterates over each file, reads it as a DataFrame using Pandas,
and concatenates all the DataFrames into a single DataFrame named all_months_data.
The combined DataFrame is then saved to a CSV file named "all_data.csv".

2-Data Preprocessing:
The script performs several data preprocessing steps on the combined DataFrame:
It adds a 'month' column extracted from the 'Order Date' column to represent the month of each order.
Rows with missing or erroneous data are removed.
The 'month' column is converted to an integer type,
and numeric columns ('Price Each', 'Quantity Ordered') are converted to numeric types.
A 'sales' column is created by multiplying the 'Quantity Ordered' and 'Price Each' columns
to calculate the total sales for each order.

3-Sales Analysis:
The script analyzes sales data by:
*Grouping the data by month and summing the total sales for each month.
*Generating a bar plot to visualize the total sales per month.
*Creating a new 'city' column by extracting city names from the 'Purchase Address' column
  and grouping the data by city to analyze sales per city.
*Generating a bar plot to visualize sales per city.
*Analyzing the distribution of orders across different hours of the day and plotting a line plot to show the distribution.
*Identifying duplicated orders and grouping products with the same order ID together.
*Counting the occurrences of grouped products and visualizing them with a bar plot.
*Analyzing the total quantity of each product ordered and plotting a bar plot to visualize the results.

4-Visualization:
Throughout the script, Matplotlib is used to generate various visualizations
such as bar plots and line plots to represent the analyzed data.
"""
   
   
