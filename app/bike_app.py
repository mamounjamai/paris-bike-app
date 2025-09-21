import streamlit as st
import pandas as pd
from src.data_io import load_parquet_with_time_features
from src.filters import filter_by_values
import matplotlib.pyplot as plt

st.set_page_config(page_title="🚲 Paris Bike Explorer", layout="wide")
st.title("🚲 Paris Bike Counts Explorer")

@st.cache_data
def load_data():
    return load_parquet_with_time_features("train.parquet")

df = load_data()
st.success(f"{len(df):,} records loaded from train.parquet")

# Filters
col1, col2 = st.columns(2)
with col1:
    stations = st.multiselect("Filter by counter_name:", sorted(df["counter_name"].dropna().unique()))
with col2:
    sites = st.multiselect("Filter by site_name:", sorted(df["site_name"].dropna().unique()))

df_f = df.copy()
if stations:
    df_f = filter_by_values(df_f, "counter_name", stations)
if sites:
    df_f = filter_by_values(df_f, "site_name", sites)

st.info(f"{len(df_f):,} records after filtering.")
if df_f.empty:
    st.warning("No records with current filters."); st.stop()

# Daily counts
st.subheader("📈 Daily total bike counts")
daily = df_f.groupby("day", as_index=False)["bike_count"].sum().sort_values("day")
st.line_chart(daily, x="day", y="bike_count")

# Monthly & yearly
c1, c2 = st.columns(2)
with c1:
    st.subheader("📅 Average by month")
    monthly = df_f.groupby("month", as_index=False)["bike_count"].mean().sort_values("month")
    st.bar_chart(monthly, x="month", y="bike_count")
with c2:
    st.subheader("📅 Average by year")
    yearly = df_f.groupby("year", as_index=False)["bike_count"].mean().sort_values("year")
    st.bar_chart(yearly, x="year", y="bike_count")

# Heatmap (weekday × hour)
st.subheader("🔥 Average intensity per hour and weekday")
pivot = df_f.pivot_table(index="weekday_idx", columns="hour", values="bike_count", aggfunc="mean")
pivot = pivot.reindex(index=range(0,7), columns=range(0,24))
fig, ax = plt.subplots(figsize=(12,5))
im = ax.imshow(pivot, aspect="auto", origin="upper")
ax.set_xlabel("Hour of the day"); ax.set_ylabel("Weekday")
ax.set_xticks(range(0,24)); ax.set_yticks(range(0,7))
ax.set_yticklabels(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
cbar = fig.colorbar(im, ax=ax); cbar.set_label("Average bike_count")
st.pyplot(fig, clear_figure=True)

# Map
st.subheader("🗺️ Station map")
map_df = df_f[["latitude","longitude"]].dropna().drop_duplicates()
st.map(map_df) if not map_df.empty else st.info("No coordinates after filtering.")

# Raw preview
if st.checkbox("Show raw data preview"):
    st.dataframe(df_f.head(200))
