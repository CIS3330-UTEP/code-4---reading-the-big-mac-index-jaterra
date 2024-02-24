# import pandas as pd

# list_teams = ['49ers', 'KC', 'Cowboys', 'Steelers']

# print(type(list_teams))

# print(list_teams)

# series_teams = pd.Series(list_teams)
# print()


# students = {'Hawaii':'Isabella','Ohio':'David'}
# print(type(students))

# student_series = pd.Series(index = students.keys(), data)

# df = pd.read_csv('big-mac-full-index.csv')

# # print(type(df))
# # print(df.columns)
# # print(type(df.columns))


# country_code = 'USA'
# query_text = f"iso_a == @country_code"
# query = f"iso_a3 == 'USA'"

# import pandas as pd

# df = pd.read_csv('big-mac-full-index.csv')
# print(len(df))
# print(df.index)
# print(len(df.index))
# print (type(df.index))

# numbers = range(1631)
# print(numbers)

# for i in df.index:
#     print(i)
#     print(df['dollar_price'][i])
#     print(df.loc[i]['name'])
#     print(type(df.loc[i]))



# import pandas as pd
# fruits = ['apple','melon','grapes','orange','kiwi']
# fruit_series = pd.Series(fruits)

# print('Fruits')
# print(fruits)
# print('Fruits series')
# print(fruit_series)


# import pandas as pd

# students = {"Texas":"Jazmin","Alabama":"Roberto","Virginia":"David","California":"Alex"}
# student_series = pd.Series(data=students.values(), index=students.keys())

# print("Students")
# print(students)
# print("Student Series")
# print(student_series)


# print(fruit_series.index)
# print(student_series.index)

# print(fruit_series.index.values)



# import pandas as pd

# filename = "./big-mac-full-index.csv"
# df = pd.read_csv(filename)

# print(df.columns)
# print(df)
# print(df['dollar_price'])



# Pandas queries
# Prints all of MEX rows in file
# import pandas as pd

# filename = "./big-mac-full-index.csv"
# df = pd.read_csv(filename)

# query = f"(iso_a3 == 'MEX')"
# mxn_df = df.query(query)

# print(mxn_df)



# Pandas operations

# import pandas as pd

# filename = "./big-mac-full-index.csv"
# df = pd.read_csv(filename)

# query = f"(iso_a3 == 'MEX')"
# mxn_df = df.query(query)

# print(mxn_df.median())



# import pandas as pd

# filename = "./big-mac-full-index.csv"
# df = pd.read_csv(filename)

# query = f"(iso_a3 == 'MEX')"
# mxn_df = df.query(query)

# print(type(mxn_df['dollar_price'].median()))



# MEAN
import pandas as pd

filename = "./big-mac-full-index.csv"
df = pd.read_csv(filename)

print(df['dollar_price'])

query = f"(iso_a3 == 'MEX')"
mxn_df = df.query(query)

print(mxn_df['dollar_price'].min())
print(mxn_df['dollar_price'].max())
print(round(mxn_df['dollar_price'].mean(), 2))



# prints min dollar price in japan
# import pandas as pd

# filename = "./big-mac-full-index.csv"
# df = pd.read_csv(filename)

# query = f"(iso_a3 == 'JPN')"
# jpn_df = df.query(query)
# min_idx = jpn_df['dollar_price'].idxmin()

# print(min_idx)
# print(jpn_df.loc[min_idx])
# print(jpn_df.loc[min_idx]['dollar_price'])



# prints max dollar price in argentina
# import pandas as pd

# filename = "./big-mac-full-index.csv"
# df = pd.read_csv(filename)

# query = f"(iso_a3 == 'ARG')"
# arg_df = df.query(query)
# max_idx = arg_df['dollar_price'].idxmax()

# print(max_idx)
# print(arg_df.loc[max_idx])
# print(arg_df.loc[max_idx]['dollar_price'])



# prints more vertically
# import pandas as pd

# filename = "./big-mac-full-index.csv"
# df = pd.read_csv(filename)

# query = f"(iso_a3 == 'ARG')"
# arg_df = df.query(query)

# for index, row in arg_df.iterrows():
#     print(index)
#     print(row)


# import pandas as pd

# filename = "./big-mac-full-index.csv"
# df = pd.read_csv(filename)

# query = f"(iso_a3 == 'ARG')"
# arg_df = df.query(query)

# print(arg_df)