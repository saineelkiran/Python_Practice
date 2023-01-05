from numpy import *
arr =array([
    [23,34,56,75,24,93,22,87,64],
    [22,3,3,23,42,6,9,54,76]
        ])
print("data type : "+str(arr.dtype))
print("dimension : "+str(arr.ndim))

arr_f= arr.flatten()
print("Flattened array : " + str(arr_f))

arr_re= arr.reshape(3,2,3)
print("Reshaped array : \n" +str(arr_re))

matrx = matrix('12 3 4;3 4 5;34 54 34;3 5 9')
print("Matrix o/p \n"+str(matrx))

print("Daignol Elements are \n" +str(diagonal(matrx)))

print("min Element \n" +str(matrx.min()))
print("max Element \n" +str(matrx.max()))