import numpy as np
import pandas
import matplotlib.pyplot as plt

# np.array([]) - to create a list
# ^ these arrays can be lists of lists to represent multiple columns

# array.shape - returns the no. rows and no. elements in each row
# array.dtype - returns the data type for that array
# the dtype can be changed for e.g int to float like np.array(data, dtype='float')
# use indices to access specific positions of an array eg array[-1] for last element
# for a 2-d array we can use multiple indices e.g array[0][1]

# Slice; to get a subset of a array using numPy we can use the array[1:4], which returns subset between 1 and 4
# for a 2-d array, to slice, array[0:2 3:5], which returns the 2 elements nested in the first two lists

# use [:,2] - if want to perform operation only on second column

# for mean use np.mean(Data)
# for median use np.median(data)
# for min/max np.min, np.max(data)
# for the index of the min/max value apply np.argmin/argmax(data)
# to get vals greater than 120, use np.where(array > 120), which returns the index


# a filtered array can be created with elements fulfiling a condition e.g through array = originalArray > 120, then newArray = originalArray[array]

# to order an array use np.sort() - low to high

# to generate values between 0 and 10000, use np.arrange(start, end, step (optional))
# to generate x number of values equally spaced between start and end use np.linspace(start,end, num), num is by defualt set to 50 and is optional

# to get an array with x num values of 0s, use np.zeros(x)
# for 2-D use np.zeros([2,3]), 2 rows with 3 elements filled entirely with zeros
# np.ones for x values of 1s, 2d can be same as above
# for other values use np.full([5,8]) fill 8 elements with value 5, for 2d use np.full([2,2],'n') - 2 rows 2 elements with n

# to get an identity matrix for a given n value where nxn is the matrix that you want an identity matrix of, use np.eye(n)
# to create random numbers use np.random.ranindt/rand, you can specify low, high, num of values.
# to generate random values from a data, use np.random.choice(data, (3,3)) - returns a 3x3 numpy matrix

## TASK 1 Problem

lee_data = np.array(([1,6012],[2,7079],[3,6886],[4,7230],[5,4598],[6,5564],[7,6971],[8,7763],[9,8032],[10,9569]))
print(lee_data)
lee_data[:,1] += 2000 # adds 2000 to each element in 2nd column
print(lee_data)
def returnGreater9000():
    return lee_data[lee_data > 9000]
print(returnGreater9000())

lee_data[:,1].sort()
print(lee_data)

