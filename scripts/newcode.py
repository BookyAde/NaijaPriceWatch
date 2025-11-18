import pandas as pd
data = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\Data_cleaning_course\cleaned_customers.csv")
df = pd.DataFrame(data)
age_range = df[(df['age'] > 22) | (df ['age'] < 40)]
# print (age_range)

df = pd.read_csv("cleaned_customers.csv")  # or your correct path

# Convert signup_date to datetime
df["signup_date"] = pd.to_datetime(df["signup_date"])

# Extract signup year
df["signup_year"] = df["signup_date"].dt.year


# print("\nAGE STATISTICS:")
# print(df["age"].describe())

# print("\nPOTENTIAL OUTLIER AGES:")
# print(df[df["age"] < 0])
# print(df[df["age"] > 120])

# print("\nCHECKING DUPLICATE CUSTOMER IDs:")
# print(df["customer_id"].duplicated().sum())
# print(df[df["customer_id"].duplicated()])

# print("\nCHECKING SIGNUP DATES IN THE FUTURE:")
# print(df[df["signup_date"] > "2025-12-31"])

# print("\nCHECKING FOR NAME–GENDER MISMATCHES (quick inspection):")
# print(df[["name", "gender"]].head(10))

# print("\nAGE VALUE COUNTS (to see unusual repeats):")
# print(df["age"].value_counts())

def age_category(age):
    if age < 25:
        return "Young Adult"
    elif age < 50:
        return "Adult"
    else:
        return "Senior"

df["age_group"] = df["age"].apply(age_category)

# print("\nAGE GROUPS ADDED:")
# print(df[["name", "age", "age_group"]].head(10))

# Extract signup year
df["signup_year"] = df["signup_date"].dt.year

# Calculate customer tenure
today = pd.to_datetime("today")

df["tenure_days"] = (today - df["signup_date"]).dt.days
df["tenure_years"] = df["tenure_days"] / 365

# print("\nTENURE COLUMNS ADDED:")
# print(df[["name", "signup_date", "signup_year", "tenure_years"]].head(10))

# Split name into first and last
df[["first_name", "last_name"]] = df["name"].str.split(" ", n=1, expand=True)

# print("\nNAME SPLIT INTO FIRST AND LAST:")
# print(df[["name", "first_name", "last_name"]].head(10))

# Reorder columns
new_order = [
    "customer_id",
    "first_name",
    "last_name",
    "name",
    "gender",
    "age",
    "age_group",
    "signup_date",
    "signup_year",
    "tenure_years",
    "location"
]

df = df[new_order]

# print("\nREORDERED DATAFRAME:")
# print(df.head(10))

# EXPORT FINAL CLEANED DATASET
df.to_csv("../cleaned_customers_final.csv", index=False)
df.to_excel("../cleaned_customers_final.xlsx", index=False)

# print("\nFILES EXPORTED SUCCESSFULLY!")

import matplotlib.pyplot as plt

# plt.plot([1, 2, 3], [4, 5, 6])
# plt.title("Test Plot")
# plt.show()
import matplotlib.pyplot as plt

# AGE DISTRIBUTION
# plt.hist(df["age"], bins=10, edgecolor="black")
# plt.title("Age Distribution of Customers")
# plt.xlabel("Age")
# plt.ylabel("Number of Customers")
# plt.show()

# GENDER DISTRIBUTION
gender_counts = df["gender"].value_counts()

# plt.bar(gender_counts.index, gender_counts.values, edgecolor="black")
# plt.title("Gender Distribution of Customers")
# plt.xlabel("Gender")
# plt.ylabel("Number of Customers")
# plt.show()

# SIGNUP TREND (CUSTOMERS PER YEAR)
signup_counts = df["signup_year"].value_counts().sort_index()

# plt.plot(signup_counts.index, signup_counts.values, marker="o")
# plt.title("Customer Signup Trend by Year")
# plt.xlabel("Signup Year")
# plt.ylabel("Number of Customers")
# plt.grid(True)
# plt.show()

# TENURE DISTRIBUTION
# plt.hist(df["tenure_years"], bins=10, edgecolor="black")
# plt.title("Customer Tenure Distribution (Years)")
# plt.xlabel("Tenure in Years")
# plt.ylabel("Number of Customers")
# plt.show()

# AGE GROUP DISTRIBUTION (PIE CHART)
age_group_counts = df["age_group"].value_counts()

# plt.pie(
#     age_group_counts.values,
#     labels=age_group_counts.index,
#     autopct="%1.1f%%",
#     startangle=90,
#     wedgeprops={"edgecolor": "black"}
# )
# plt.title("Age Group Distribution")
# plt.show()

