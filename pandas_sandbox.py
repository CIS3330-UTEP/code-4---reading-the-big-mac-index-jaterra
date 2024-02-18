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

import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')
print(len(df))
print(df.index)
print(len(df.index))
print (type(df.index))

numbers = range(1631)
print(numbers)

for i in df.index:
    print(i)
    print(df['dollar_price'][i])
    print(df.loc[i]['name'])
    print(type(df.loc[i]))