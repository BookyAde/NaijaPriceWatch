import pandas as pd
data = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\Data_cleaning_course\data\datasets\sales_data.csv")
df = pd. DataFrame(data)
# print (df)
df.set_index('order_id', inplace=True)
# print (df)
df["date"] = pd.to_datetime(df["date"])
print (df.head(10))
print (df.tail(10))
print (f'Shape: {df.shape}')
print (df.dtypes)
print (df.columns)
df_sorted_date = df.sort_values(by="date", ascending=False)
# This is the correct line (use the 'price' column, not 'product')
expensive_products = df[df['price'] > 400]

print(f"There are {len(expensive_products)} products priced over $400:\n")
print(expensive_products[['product', 'category', 'price', 'quantity', 'date']])
stationery_products = df[df['category'] == 'Stationery']
print(f"There are {len(stationery_products)} products in the category SATIONARY: \n")
print (stationery_products)
medium_quantity = df[(df['quantity'] >= 50) & (df['quantity'] <= 150)]
print(f"There are {len(medium_quantity)} products within 50 - 150 in quantity:\n")
print (medium_quantity)
stationery_mid = df[(df['category'] == 'Stationery') & (df['price'] < 300) & (df['quantity'] > 50)]
print(f"There are {len(stationery_mid)} products that are stationary and greater than 50 quantity: \n")
print(stationery_mid)