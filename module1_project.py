import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("retail_sales.csv", parse_dates=["order_date"])

print("Shape:", df.shape)
print("\nColumn types:\n", df.dtypes)
print("\nFirst look:\n", df.head())
print("\nMissing values:\n", df.isnull().sum())
print("\nBasic stats:\n", df.describe())

def clean_retail_data(df):
    """
    Complete cleaning pipeline for retail sales data.
    Returns a cleaned copy of the DataFrame.
    """
    df = df.copy()

    # 1. Remove exact duplicates
    before = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Duplicates removed: {before - len(df)}")

    # 2. Fix column names (lowercase, no spaces)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # 3. Type conversion
    df["order_date"]  = pd.to_datetime(df["order_date"], errors="coerce")
    df["price"]       = pd.to_numeric(df["price"],       errors="coerce")
    df["quantity"]    = pd.to_numeric(df["quantity"],     errors="coerce")

    # 4. Handle missing values
    df["category"].fillna("Unknown", inplace=True)
    df["region"]  .fillna(df["region"].mode()[0], inplace=True)
    df["price"]   .fillna(df["price"].median(),   inplace=True)
    df["quantity"].fillna(1, inplace=True)

    # 5. Cap price outliers using IQR
    Q1, Q3 = df["price"].quantile([0.25, 0.75])
    IQR    = Q3 - Q1
    df["price"] = df["price"].clip(lower=Q1 - 1.5*IQR,
                                    upper=Q3 + 1.5*IQR)

    print(f"Clean dataset shape: {df.shape}")
    return df

df = clean_retail_data(df)

df["revenue"]    = df["price"] * df["quantity"]
df["profit"]     = df["revenue"] - (df["cost"] * df["quantity"])
df["profit_pct"] = (df["profit"] / df["revenue"] * 100).round(2)

# Time-based features
df["year"]       = df["order_date"].dt.year
df["month"]      = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.month_name()
df["quarter"]    = df["order_date"].dt.quarter
df["day_of_week"]= df["order_date"].dt.day_name()

# Categorise order size
df["order_size"] = pd.cut(
    df["quantity"],
    bins=[0, 5, 20, 50, float("inf")],
    labels=["Small", "Medium", "Large", "Bulk"]
)

# ── Revenue by Category ───────────────────────────
category_summary = df.groupby("category").agg(
    total_revenue = ("revenue",    "sum"),
    avg_price     = ("price",      "mean"),
    total_orders  = ("order_id",   "count"),
    avg_profit_pct= ("profit_pct", "mean")
).round(2).sort_values("total_revenue", ascending=False)

print("═══ Revenue by Category ═══")
print(category_summary)

# ── Monthly Trend ─────────────────────────────────
monthly = (df.groupby(["year", "month_name"])["revenue"]
             .sum()
             .reset_index()
             .rename(columns={"revenue": "monthly_revenue"}))

# ── Top 10 Products ───────────────────────────────
top_products = (df.groupby("product_name")["revenue"]
                  .sum()
                  .nlargest(10)
                  .reset_index())

# ── Regional Performance ──────────────────────────
region_perf = df.groupby("region").agg(
    revenue       = ("revenue", "sum"),
    avg_profit_pct= ("profit_pct", "mean"),
    orders        = ("order_id", "count")
).sort_values("revenue", ascending=False)

print("\n═══ Regional Performance ═══")
print(region_perf)

df.to_csv("retail_sales_clean.csv", index=False)
print("✓ Clean dataset saved.")

# ── Save multi-sheet Excel report ─────────────────
with pd.ExcelWriter("retail_analysis_report.xlsx",
                    engine="openpyxl") as writer:

    df.to_excel(writer,
                sheet_name="Clean_Data",  index=False)

    category_summary.to_excel(writer,
                sheet_name="Category_Summary")

    monthly.to_excel(writer,
                sheet_name="Monthly_Trend",    index=False)

    top_products.to_excel(writer,
                sheet_name="Top_10_Products",  index=False)

    region_perf.to_excel(writer,
                sheet_name="Regional_Performance")

print("✓ Excel report saved: retail_analysis_report.xlsx")

# ── Summary print ─────────────────────────────────
print("\n" + "═"*45)
print("      RETAIL SALES — EXECUTIVE SUMMARY")
print("═"*45)
print(f"  Total Revenue  : ₹{df['revenue'].sum():>12,.0f}")
print(f"  Total Orders   : {len(df):>12,}")
print(f"  Avg Profit %   : {df['profit_pct'].mean():>12.1f}%")
print(f"  Top Category   : {category_summary.index[0]:>12}")
print(f"  Top Region     : {region_perf.index[0]:>12}")
print("═"*45)