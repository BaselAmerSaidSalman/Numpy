# np.array() => لتحويل ما بداخل القوس الى ارراي => variable1 = np.array([[1],[2],[3],[4],[5]]) 
# .ndim => لمعرفة نوع الارراي عن طريق عدد الاقواس التي تحتويه داخل بعض => print(variable1.ndim) => 2
# np.array([1,2,3,4,5], ndim=2) = np.array([[1],[2],[3],[4],[5]]) => Change dimension of array from 1 to 2 
# print(np.array([[1],[2],[3],[4],[5]]).ravel()) = np.array([1,2,3,4,5]) => Change dimension of array from 2 to 1
# np.arange(150) => عمل قائمة تحتوي على ارقام تتراوح بين 0 الى 149




# Size
# array.itemsize => size of item in memory => equal ? byte => print(array.itemsize)
# array.size => number of items in the array => print(array.size)
# print(sys.getsizeof(write here one elemet from your list)) = print(array.itemsize)
# print(array.size()) = print(len(list))
# Size of array in memory = print(array.itemsize * array.size)
# Size of list in memory = print(sys.getsizeof(write here one elemet from your list) * len(list))

# Examples of Size
# Array
import numpy as np
a = np.arange(150)
print(a.itemsize) # Item Size
print(a.size) # Number of items in the array
print(a.itemsize * a.size) # Array Size
#---------------------------------------------------
# List
import sys
b = range(150)
print(sys.getsizeof(2)) # Item Size
print(len(b)) # Number of items in the list
print(sys.getsizeof(2) * len(b)) # List Size





# Type of items in array
# array.dtype => نوع عناصر الارراي => print(array.dtype)
# a = np.array([1, 2, 3, 4])
# np.array([1, 2, 3, 4], dtype=float) => change type of items in this array from int to float
# np.array([1.5, 2.25, 3.3, 4.98], dtype=float) => change type of items in this array from float to int
# np.array(["Basel", "Ahmed", "Ali"], dtype=float or int) => Value Error
# np.array([1, 2, 3, 4], dtype=float) = a = a.astype('float')
# a = a.astype('bool') => write (true) instead of all numbers except zero write here (false) = np.array([True, True, True, True])
# Capacity for example (float32, int32, float64, float64) = item size * items number => ثبات عدد العناصر يدل على ان حجم العنصر في الذاكره يتضاعف

# Examples of Array items type:
import numpy as np
a = np.array([1, 2, 3, 4]) 
print(a.dtype) # Type = int
#---------------------------------------------------
a = np.array([1, 2, 3, 4], dtype=float) 
print(a.dtype) # Type = float
#---------------------------------------------------
a = np.array([1, 2, 3, 4]) 
a = a.astype('float')
print(a.dtype) # Type = float




# Arithmetic Operations
# 1 Dimension
a = np.array([10,20,30])
b = np.array([2,4,5])
# 1. الجمع
print(a + b) # result [12, 24, 35]
# 2. الطرح
print(a - b) # result [8, 16, 25]
# 3. الضرب
print(a * b) # result [20, 80, 150]
# 4. القسمة
print(a / b) # result [5, 5, 6]

# 2 Dimension
a = np.array([[10,20], [30, 40]])
b = np.array([[2,4], [5, 10]])
# 1. الجمع
print(a + b) # result [ [12, 24], [35, 50] ]
# 2. الطرح
print(a - b) # result [ [8, 16], [25, 30] ]
# 3. الضرب
print(a * b) # result [ [20, 80], [150, 400] ]
# 4. القسمة
print(a / b) # result [ [5, 5], [6, 4] ]



# Min-Max-Sum-Ravel
a = np.array([10,20,30])
print(a.min()) # 10
print(a.max()) # 30
print(a.sum()) # 60
#---------------------------------------------------
b = np.array([[50,60], [70, 10]])
print(b.ravel()) # result [50, 60, 70, 10]

