import pandas as pd

df = pd.read_csv("matches.csv")

print(df.head())

print("\nInfo:\n")
print(df.info())

print("\nStats:\n")
print(df.describe())

s = df['season'].value_counts().sort_index()

print("\nMatches Per Season:\n", s)

w = df['winner'].value_counts()

print("\nMost Winning Team:\n", w.head(1))

v = df[df['venue'] == 'Wankhede Stadium']

print("\nMatches At Venue:\n", v[['team1', 'team2', 'winner']])

p = df['player_of_match'].value_counts().head(5)

print("\nTop Players:\n", p)

print("\nNull Values:\n", df.isnull().sum())

d = df.dropna()

print("\nAfter Dropping Nulls:", d.shape)

b1 = df[df['win_by_runs'] > 0]['winner'].value_counts()

b2 = df[df['win_by_wickets'] > 0]['winner'].value_counts()

x = pd.DataFrame({
    'Bat First': b1,
    'Field First': b2
}).fillna(0)

x['Total'] = x['Bat First'] + x['Field First']

x['Bat %'] = (x['Bat First'] / x['Total']) * 100
x['Field %'] = (x['Field First'] / x['Total']) * 100

print("\nWin Percentage:\n", x)