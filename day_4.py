import pandas as pd

df = pd.read_csv("superstore.csv")

g = df.groupby(['Region', 'Category'])[['Sales', 'Profit']].sum()

print("\nSales And Profit:\n", g)

t = df.groupby(['Region', 'Sub-Category'])['Sales'].sum().reset_index()

t = t.sort_values(['Region', 'Sales'], ascending=[True, False])

print("\nTop 3 Sub Categories:\n")

for i in t['Region'].unique():
    print("\n", i)
    print(t[t['Region'] == i].head(3))

df['Margin'] = (df['Profit'] / df['Sales']) * 100

print("\nProfit Margin:\n", df[['Sales', 'Profit', 'Margin']].head())

p = pd.pivot_table(
    df,
    values='Sales',
    index='Region',
    columns='Segment',
    aggfunc='mean'
)

print("\nPivot Table:\n", p)

df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Month'] = df['Order Date'].dt.month_name()

m = df.groupby('Month')['Profit'].sum()

n = m[m < 0]

print("\nNegative Profit Months:\n", n)

q = df.set_index('Order Date').resample('Q')['Sales'].sum()

print("\nQuarterly Sales:\n", q)