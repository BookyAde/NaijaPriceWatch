import pandas as pd
# ages = pd.Series([25, 30, 35, 40])
# print(ages)


# records = [
#  {'product': 'Pen', 'price': 200, 'quantity': 50},
#  {'product': 'Notebook', 'price': 500, 'quantity': 30},
#  {'product': 'Eraser', 'price': 100, 'quantity': 100}
# ]
# # df = pd.DataFrame(records)
# print(df)


data = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\Data_cleaning_course\data\raw\customers.csv")
df = pd.DataFrame(data)
# print(df)
# print (df.head())
# print (df.tail())
# print (f'Shape: {df.shape}')
# print (df.dtypes)
# print (df.columns)
# print (df.describe())
# print (df[['gender','location', 'signup_date']])  #you can add any detail to single them out 

# df.set_index('customer_ id', inplace=True)
# print (df)


# print ( df[['gender', 'age']])
# print (df.iloc[5:11])
# print (df.loc[10, 'location']) #or  print (df.loc['C009', 'location']) (works with the loc func, use a key or an indexed key)
# print (df.iloc[10, 5]) #only uses indeexes
# print (df.loc())
# import pandas as pd
 # adjust path if needed

# print("\nMISSING VALUES (per column):")
# print(df.isnull().sum())
# print("\nNUMBER OF DUPLICATE ROWS:")
# print(df.duplicated().sum())

# print("\nDUPLICATE ROWS (if any):")
# print(df[df.duplicated()])
# print("\nDATA TYPES:")
# print(df.dtypes)
# Convert signup_date to datetime
# df["signup_date"] = pd.to_datetime(df["signup_date"])

# print("\nDATA TYPES AFTER CONVERSION:")
# print(df.dtypes)
# print("\nUNIQUE GENDER VALUES BEFORE CLEANING:")
# print(df["gender"].unique())
# print("\nNAME COLUMN BEFORE CLEANING:")
# print(df["name"].head())
# Clean name column: remove spaces + proper capitalization
# df["name"] = df["name"].str.strip()           # remove extra spaces
# df["name"] = df["name"].str.title()           # Ensure proper casing (Title Case)

# print("\nNAME COLUMN AFTER CLEANING:")
# print(df["name"].head())
# print("\nLOCATION COLUMN BEFORE CLEANING:")
# print(df["location"].head())

# # Clean location text
# df["location"] = df["location"].str.strip()    # remove extra spaces
# df["location"] = df["location"].str.title()    # Convert to Title Case

# print("\nLOCATION COLUMN AFTER CLEANING:")
# print(df["location"].head())
# SORT BY AGE (ascending)
# df_sorted_age = df.sort_values(by="age")
# print("\nSORTED BY AGE:")
# print(df_sorted_age.head())

# # SORT BY SIGNUP DATE (newest first)
# df_sorted_date = df.sort_values(by="signup_date", ascending=False)
# print("\nSORTED BY SIGNUP DATE (NEWEST FIRST):")
# print(df_sorted_date.head())

# # RESET INDEX (important before export)
# df_final = df.reset_index(drop=True)

# print("\nFINAL CLEANED DATAFRAME:")
# print(df_final.head())


# df_final.to_csv("cleaned_customers.csv", index=False)


