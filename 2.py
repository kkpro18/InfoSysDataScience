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



