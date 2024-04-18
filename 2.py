import numpy as np
import pandas as pd


# series is 1D
# can be created using pd.series(data,index, dtype) = 2nd and 3rd param is optional
# values can be obtained by series.values
# get index using series.index
# slice using [1:3] - returns 2,3
# custom index can be created sort of like a label for that var
# a dictionary can be used to create a series, make the dict then pd.series(dict)
# a df can be used to collect lots of series, where each series represents a column
# a df can be created by pd.DataFrame(data, index, columns) e.g pd.DataFrame({'Price': car_price , 'Manufacturer' : car_man}), where a dict is used but converted to series first
# use pd.read_json(.json) - to get data from json as a pd
# important param in pd DF is axis, can be 0/1 0 is row, 1 is column.

# df = pd.read_csv("PythonForDataScienceCodeData/auto_mpg.csv")
# print(df)
# # use df.head() - first 5
# # use df.tail() - last 5
# # use df.describe() - to get summary of data
# # use df.info() - information about dtype, no. rows, no. null e.t.c
# df.describe()
# df.info()
# # use df.dropna(inplace= True) to get rid of rows with null values
# df.dropna(inplace = True) # inplace allows changes to the actual df
# # use df.fillna(condition) to fill missing values with mean,median,mode or constant vals
# df.info()
# # clear drop of rows from 398 to 392
# print(df['name']) # outputs the series of just names
# print(df[['name']]) # returns a series in form nx1 that can readily be a DF
#
# # custom indexes can be set using df.head.set_index('name',inplace=True)
# df.head().set_index('name', inplace=True)


marks = {'Chemistry': [67,90,66,32],
        'Physics': [45,92,72,40],
        'Mathematics': [50,87,81,12],
        'English': [19,90,72,68]}

marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])
print(marks_df)

marks_df['Total'] = marks_df['Chemistry'] + marks_df['Physics'] + marks_df['Mathematics'] + marks_df['English']
print(marks_df)
# to remove a column use df.drop(columns='',inplace=True)
marks_df.drop(columns = 'Total', inplace = True)
print(marks_df)

# mask operation can be used to replace values when condition is true
# syntax - DF.mask(cond, other = nan, inplace = False, axis = None)
# value is original if cond is false, else other is applied
# e.g make scores less than 33 say fail instead of score

marks_df.mask((marks_df < 33),'Fail', inplace = True)
print(marks_df)
