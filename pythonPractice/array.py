from array import *
arr1 = array('i', [10,15,20,25,30,35])
arr2 = array(arr1.typecode, (n for n in arr1))
arr1[0] = 11
print(arr1)
print(arr2)