import numpy as np

a = np.random.randint(0, 100, size=50)

print("Scores:\n", a)

print("\nMean:", np.mean(a))
print("Median:", np.median(a))
print("Highest:", np.max(a))
print("Lowest:", np.min(a))
print("Std Dev:", np.std(a))
print("90 Percentile:", np.percentile(a, 90))

f = a[a < 40]
d = a[a > 85]

print("\nFail Students:", f)
print("Distinction Students:", d)

n = (a - np.min(a)) / (np.max(a) - np.min(a))

print("\nNormalized Scores:\n", n)

b = a.reshape(5, 10)

print("\n5x10 Matrix:\n", b)

r = np.mean(b, axis=1)

print("\nRow Wise Average:", r)

t = np.random.randint(40, 100, size=50)
p = np.random.randint(40, 100, size=50)

w = (0.4 * t) + (0.6 * p)

print("\nTheory Marks:\n", t)
print("\nPractical Marks:\n", p)
print("\nWeighted Final Scores:\n", w)