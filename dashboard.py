import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../cleaned_customers_final.csv")
df["signup_date"] = pd.to_datetime(df["signup_date"])

st.title("Customer Analytics Dashboard")
st.write("Interactive exploratory dashboard built with Streamlit")

# Sidebar filters
st.sidebar.header("Filters")

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

age_group_filter = st.sidebar.multiselect(
    "Select Age Groups",
    options=df["age_group"].unique(),
    default=df["age_group"].unique()
)

year_filter = st.sidebar.multiselect(
    "Select Signup Year",
    options=sorted(df["signup_year"].unique()),
    default=sorted(df["signup_year"].unique())
)

# Apply filters
filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["age_group"].isin(age_group_filter)) &
    (df["signup_year"].isin(year_filter))
]

st.subheader("Filtered Data Preview")
st.dataframe(filtered_df)

# Chart 1 — Age Distribution
st.subheader("Age Distribution")
fig1, ax1 = plt.subplots()
ax1.hist(filtered_df["age"], bins=10, edgecolor="black")
st.pyplot(fig1)

# Chart 2 — Gender Distribution
st.subheader("Gender Distribution")
gender_counts = filtered_df["gender"].value_counts()
fig2, ax2 = plt.subplots()
ax2.bar(gender_counts.index, gender_counts.values, edgecolor="black")
st.pyplot(fig2)

# Chart 3 — Signup Trend
st.subheader("Signup Trend by Year")
signup_counts = filtered_df["signup_year"].value_counts().sort_index()
fig3, ax3 = plt.subplots()
ax3.plot(signup_counts.index, signup_counts.values, marker="o")
st.pyplot(fig3)

# Chart 4 — Tenure Distribution
st.subheader("Tenure Distribution")
fig4, ax4 = plt.subplots()
ax4.hist(filtered_df["tenure_years"], bins=10, edgecolor="black")
st.pyplot(fig4)

# Chart 5 — Age Group Pie Chart
st.subheader("Age Group Breakdown")
age_group_counts = filtered_df["age_group"].value_counts()
fig5, ax5 = plt.subplots()
ax5.pie(
    age_group_counts.values,
    labels=age_group_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"edgecolor": "black"}
)
st.pyplot(fig5)
