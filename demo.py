# # # # List1=[5, 10, 15, 20]
# # # import numpy as np
# # # # List1=[1,2,3,4,5]
# # # # # list2 =[List1,List4]
# # # # a = np.array(List1)
# # # # l2=List1+2
# # # # a2= a+2
# # # # # print(a)
# # # # print(a2)


# # # import numpy as np
# # # data = np.array([
# # #     [1, 85, 5, 90],
# # #     [2, 78, 4, 85],
# # #     [3, 92, 6, 95],
# # #     [4, 60, 2, 70],
# # #     [5, 75, 3, 80]
# # # ])

# # # # print(data)
# # # print(data[0])        # First row
# # # print(data[:,1])       # Last row
# # # print(data[1:4])     # Element at row 1, column 2
# # # # print(list2)

# # import numpy as np
# # data = np.array([
# #     [1, 85, 5, 90],
# #     [2, 78, 4, 85],
# #     [3, 92, 6, 95],
# #     [4, 60, 2, 70],
# #     [5, 75, 3, 80]
# # ])
# # data[:,1]= data[:,1]+5
# # print(data)
# # print(np.mean(data[:,1]))
# # print(np.max(data[:,1]))
# # print(np.min(data[:,1]))

# import numpy as np

# import pandas as pd
# data = np.array([
#     [1, 85, 5, 90],
#     [2, 78, 4, 85],
#     [3, 92, 6, 95],
#     [4, 60, 2, 70],
#     [5, 75, 3, 80]
# ])
# df = pd.DataFrame(data, columns = ["ID", "Score", "Hours Studied", "Final Score"])
# # print(df)
# ss = data[:,1]
# # print(type(ss))
# # print(df.describe())
# df["performance"] = df["Score"] > 80
# # print(df)
# import pandas as pd

# # ── Reading ────────────────────────────────────────

# df = pd.read_csv(r"C:\Users\Vishwash\Downloads\sample.csv")

# df = pd.read_csv(
#     r"C:\Users\Vishwash\Downloads\sample.csv",
#     index_col="id"
# )      # set column as index

# df = pd.read_csv(
#     r"C:\Users\Vishwash\Downloads\sample.csv",
#     usecols=["name", "price"]
# )      # select columns

# df = pd.read_csv(
#     r"C:\Users\Vishwash\Downloads\sample.csv",
#     nrows=1000
# )      # first 1000 rows only

# df = pd.read_csv(
#     r"C:\Users\Vishwash\Downloads\sample.csv",
#     encoding="utf-8"
# )      # specify encoding

# df = pd.read_csv(
#     r"C:\Users\Vishwash\Downloads\sample.csv",
#     na_values=["N/A", "-", "NA", ""]
# )

# # ── Writing ────────────────────────────────────────

# df.to_csv(
#     r"C:\Users\Vishwash\Downloads\output.csv",
#     index=False
# )   # don't write index column

# df.to_csv(
#     r"C:\Users\Vishwash\Downloads\output_selected.csv",
#     columns=["name", "price"],
#     index=False
# )

# print("CSV files processed successfully!")


import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

# print(df.shape)  # Get the number of rows and columns
# print(df.head())  
# print(df.info())  # Get information about the DataFrame
# print(df.describe().round(2)) 
# print(df.isnull().sum())  # Check for missing values
scores_only=df[['math score','reading score','writing score']]
df.columns=['gender','race/ethnicity','parental level of education','lunch','test preparation course','math score','reading score','writing score']
df['avg-score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3
df['avg-score'] = df['avg-score'].round(2)
print(df.head())