import pandas as pd
import os
import matplotlib.pyplot as plt
## Created a list of all the files that i need to concatenate together
## by listing all the files in a directory 'folder_path'
folder_path=r'C:\Users\pc\Downloads\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data'
files=[file for file in os.listdir(folder_path)]
## Created the empty data frame that will contain all the files
all_months_data=pd.DataFrame()
## Used a for loop to iterate over the list of files and read them as a csv
## then put each file into a df and finally concatenate the empty data frame
## with the recently created data frame
for file in files:
    file_path=os.path.join(folder_path,file)
    df=pd.read_csv(file_path)
    all_months_data=pd.concat([all_months_data,df])
## transformed the all_months_data to a csv by passing the new csv 'path\the_csv_name'
out_put_path=r'C:\Users\pc\Downloads\Pandas-Data-Science-Tasks-master\SalesAnalysis\all_data.csv'
all_months_data.to_csv(out_put_path,index=None)
pd.set_option('display.max_columns',7)
## adding a month column by converting the order date column into a str then
## using the first 2 characters
all_months_data['month']=all_months_data['Order Date'].str[0:2]
## removing the nan values
all_months_data=all_months_data.dropna(how='all')
## removing rows when the data in order data column starts with 'or'
all_months_data=all_months_data[all_months_data['Order Date'].str[0:2]!='Or']
## convert the columns into numeric values using astype() and pd.numeric
all_months_data['month']=all_months_data['month'].astype('int32')
all_months_data['Price Each']=pd.to_numeric(all_months_data['Price Each'])
all_months_data['Quantity Ordered']=pd.to_numeric(all_months_data['Quantity Ordered'])
## creating the sales column
all_months_data['sales']=all_months_data['Quantity Ordered']*all_months_data['Price Each']
## Using .groupby() to group the month and the sum to get the total sales
m=all_months_data.groupby("month").sum()
months=range(1,13)
## Creating a bar plot while the x axis is the months and the y axis is the the sales
plt.bar(months,m["sales"])
plt.xlabel('month')
plt.ylabel('total sales')
plt.title("sales per month")
#plt.show()
## Creating the city column using a function for the city and the state
def get_city(address):
    return address.split(',')[1]
def get_state(address):
    return address.split(',')[2].split(' ')[1]
all_months_data['city']=all_months_data['Purchase Address'].apply(lambda x:f"{get_city(x)} ({get_state(x)})")
## Group by the new city column and sum the sales
results=all_months_data.groupby('city').sum('sales')
cities=[city for city,df in all_months_data.groupby('city')]
## visualizing the sales per city by using a bar plot
plt.bar(cities,results['sales'])
plt.xlabel('cities name')
plt.ylabel('sales per city')
plt.xticks(cities,rotation='vertical',size=6)
plt.show()
## Using the pd.datetime to convert the order data into data and time
## then creating the hour column using dt.hour
all_months_data['Order Date']=pd.to_datetime(all_months_data['Order Date'])
all_months_data['hour']=all_months_data['Order Date'].dt.hour
hourly_order_counts = all_months_data['hour'].value_counts().sort_index()

# Plotting the bar plot
plt.figure(figsize=(10, 6))
plt.plot(hourly_order_counts.index, hourly_order_counts.values, color='skyblue')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.title('Distribution of Orders Across Hours of the Day')
plt.xticks(hourly_order_counts.index)
plt.show()
## Created a new data frame that contains only the duplicated values using .duplicated
new_df=all_months_data[all_months_data['Order ID'].duplicated(keep=False)]
## New column 'grouped' has products that has the same order id and then removed the duplicates
new_df['grouped'] = new_df.groupby('Order ID')['Product'].transform(lambda x: ', '.join(x))
new_df=new_df[["Order ID","grouped"]].drop_duplicates()
## Using .value_counts to count all the similar values in the grouped column
grouped_counts = new_df['grouped'].value_counts().reset_index()
## Renameing the columns
grouped_counts.columns = ['grouped', 'count']
## Grouping by the product and sum up the quantity order
## to see which product was sold the most
product_group = all_months_data.groupby('Product')
m = product_group['Quantity Ordered'].sum().reset_index()
unique_prices = all_months_data.groupby("Product")["Price Each"].unique()
print(unique_prices)
plt.figure(figsize=(12, 6))
plt.bar(m['Product'], m['Quantity Ordered'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Quantity Ordered')
plt.title('Total Quantity Ordered per Product')
plt.xticks(rotation='vertical', size=8)
plt.show()












