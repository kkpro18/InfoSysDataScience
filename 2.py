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

marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])

encrypted_marks = np.sin(marks_df) # encrypts all scores using sin()
print(encrypted_marks)

# as indexes were changed, it can be reset back by df.reset_index(inplace = True)
encrypted_marks.reset_index(inplace=True)
print(encrypted_marks) # can be seen the existing index e.g names is added as a column, and default index is set 1,2,3..

new_marks = marks_df + 5 # implmentaion of broadcasting by adding 5 to each mark
print(new_marks)
print(marks_df)
final_mark = marks_df + [5,10,10,2] # adds these marks to the corresponding
print(final_mark)

# to apply a function along an axis DF.apply(func,axis=0,result_type=None)
# result_type can be expand, reduce or broadcast
# broadcast mean it will result the original index and columns


#Creating the DataFrame
marks = {'Chemistry': [67,90,66,32],
        'Physics': [45,92,72,40],
        'Mathematics': [50,87,81,12],
        'English': [19,90,72,68]}
marks_df = pd.DataFrame(marks, index = ['James', 'Lee', 'Anderson', 'John'])

print(marks_df.apply(np.sum,axis=0)) # axis 0 means rows, axis 1 is columns
# sum of all rows so each subject

print(marks_df.apply(np.sum,axis=1))
# sum of marks per student

print(marks_df.apply(np.mean, axis=0, result_type='broadcast'))
# fills marks with mean of last term...

marks_A = {'Chemistry': [67,90,66,32],
        'Physics': [45,92,72,40],
          }
marks_A_df = pd.DataFrame(marks_A, index = ['Subodh', 'Ram', 'Abdul', 'John'])
marks_B = {'Chemistry': [72,45,60,98],
        'Physics': [78,34,72,95],
          }
marks_B_df = pd.DataFrame(marks_B, index = ['Nandini', 'Zoya', 'Shivam', 'James'])

# to concat both mark a class and mark b class
pd.concat([marks_A_df,marks_B_df],sort=False)

# when there is a column mismatch i.e two df with a common column such as users, then some unique ones, merge can be used
# e.g pd.merge(df1,df2)

df1 = pd.DataFrame({'employee': ['Jyoti', 'Sapna', 'Raj', 'Ramaswamy'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Jyoti', 'Sapna', 'Raj', 'Ramaswamy'],
                    'hire_date': [2004, 2008, 2012, 2014]})
df3 = pd.merge(df1,df2)
print(df3)

# to get a frequency distribution for a specific column or category crosstab may be used.
