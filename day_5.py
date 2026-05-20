import pandas as pd

o = pd.read_csv("orders.csv")
c = pd.read_csv("customers.csv")
i = pd.read_csv("order_items.csv")
p = pd.read_csv("products.csv")

x = pd.merge(o, c, on='customer_id')
x = pd.merge(x, i, on='order_id')
x = pd.merge(x, p, on='product_id')

print("\nMaster Data:\n")
print(x.head())

r = x.groupby('customer_id')['price'].sum()

print("\nRevenue Per Customer:\n", r)

a = o.groupby('customer_id')['order_id'].count().reset_index()

s = a[a['order_id'] == 1]

print("\nCustomers With One Order:\n", s)

w = pd.DataFrame({
    'id': [1,2,3],
    'Jan': [1000,2000,3000],
    'Feb': [1200,2100,3100],
    'Mar': [1500,2200,3200]
})

m = pd.melt(
    w,
    id_vars='id',
    var_name='Month',
    value_name='Sales'
)

print("\nMelt Data:\n", m)

o['order_purchase_timestamp'] = pd.to_datetime(o['order_purchase_timestamp'])

o['Year'] = o['order_purchase_timestamp'].dt.year
o['Month'] = o['order_purchase_timestamp'].dt.month

print("\nYear And Month:\n")
print(o[['Year', 'Month']].head())

o['order_delivered_customer_date'] = pd.to_datetime(
    o['order_delivered_customer_date']
)

o['Days'] = (
    o['order_delivered_customer_date']
    - o['order_purchase_timestamp']
).dt.days

print("\nAverage Delivery Time:",
      o['Days'].mean())

d = pd.merge(o, c, on='customer_id')

z = d.groupby('customer_city')['Days'].mean().sort_values(ascending=False)

print("\nSlowest Delivery Cities:\n", z.head())