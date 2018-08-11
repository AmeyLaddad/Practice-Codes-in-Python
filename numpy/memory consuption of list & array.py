from sys import getsizeof as size
import numpy as np
lst = [24, 12, 57]
size_of_list_object = size(lst)   # only green box
size_of_elements = len(lst) * size(lst[0]) # 24, 12, 57
total_list_size = size_of_list_object + size_of_elements
print("Size without the size of the elements: ", size_of_list_object)
print("Size of all the elements: ", size_of_elements)
print("Total size of list, including elements: ", total_list_size)

a = np.array([24, 12, 57])
print("Size of array = ", size(a))

e = np.array([])
print("Size of an empty array = ", size(e))


a = np.array([24, 12, 57], np.int8)
print("Size of array with data type int8 = ", size(a) - 96) # size(a)-96 because 96 is the size of empty array
a = np.array([24, 12, 57], np.int16)
print("Size of array with data type int16 = ",size(a) - 96)
a = np.array([24, 12, 57], np.int32)
print("Size of array with data type int32 = ",size(a) - 96)
a = np.array([24, 12, 57], np.int64)
print("Size of array with data type int64 = ",size(a) - 96)