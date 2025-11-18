# streamlit_app.py – 100% WORKING VERSION (NO PLOTLY NEEDED)
import streamlit as st
import pandas as pd

st.set_page_config(page_title="NaijaPriceWatch", page_icon="🇳🇬", layout="wide")

st.title("🇳🇬 NaijaPriceWatch – January 2025")
st.markdown("""
**Real-time food price tracker from National Bureau of Statistics (NBS)**  
Built by Nigerian data engineers | 100% open-source 🔥
""")

# Load data
df = pd.read_csv("data/processed/naija_food_prices_jan2025_clean.csv")

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Food Items", len(df))
col2.metric("Average Price", f"₦{df['Price_Jan25'].mean():,.0f}")
col3.metric("Highest YoY Inflation", f"{df['YoY_%'].max():.1f}%")
col4.metric("States Tracked", df[['Highest_State', 'Lowest_State']].stack().nunique())

# Top 10 most expensive
st.subheader("🔥 Top 10 Most Expensive Items (National Average)")
top10 = df.nlargest(10, "Price_Jan25")[["Item", "Price_Jan25", "Highest_State"]]
top10["Price_Jan25"] = top10["Price_Jan25"].apply(lambda x: f"₦{x:,.0f}")
st.dataframe(top10, use_container_width=True, hide_index=True)

# Inflation leaderboard
st.subheader("📈 Biggest Year-on-Year Price Increases")
inflation_top = df.nlargest(10, "YoY_%")[["Item", "YoY_%"]]
inflation_top = inflation_top.round(1)
st.bar_chart(inflation_top.set_index("Item")["YoY_%"])

# Price comparison by item
st.subheader("🧅 Where is it Cheapest vs Most Expensive?")
item = st.selectbox("Select food item", sorted(df["Item"].unique()))

selected = df[df["Item"] == item].iloc[0]

col_a, col_b = st.columns(2)
with col_a:
    st.error(f"**Most Expensive** → **{selected['Highest_State']}**  \n₦{selected['Price_Jan25']:,.0f}")
with col_b:
    st.success(f"**Cheapest** → **{selected['Lowest_State']}**  \n₦{selected['Price_Jan25']:,.0f}")

st.caption("Data source: National Bureau of Statistics (NBS) Nigeria – January 2025")
st.caption("Built with ❤️ by BookyAde | GitHub: BookyAde/NaijaPriceWatch")