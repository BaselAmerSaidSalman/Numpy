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




# Min-Max-Sum-Mean-Median
a = np.array([10,20,30])

# 1. array.min() => اصغر رقم في الارراي
print(a.min()) # 10

# 2. array.max() => اكبر رقم في الارراي
print(a.max()) # 30

# 3. array.sum() => مجموع عناصر الارراي
print(a.sum()) # 60

# 4. array.mean() => متوسط عناصر الارراي = average = مجموع العناصر على عددهم
print(a.mean()) # 20

# 5. np.median(array) => القيمة التي في منتصف الارراي
print(np.median(a)) # 20





# Reshape Array
import numpy as np
a = np.array([[1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20]]) # 2 Dimension => 1 list & 2 lists in it & 10 Elements in each list
print(a.ndim)
print(a.shape)

reshaped_a = a.reshape(2,5,2) # 3 Dimension => 1 list & 2 lists in it & 5 lists in each one & 2 elements in each list
print(reshaped_a)
print(reshaped_a.ndim)
print(reshaped_a.shape)

print(a.flatten()) # [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(a.flatten()) = print(a.ravel())






# Advanced Methods

# np.full((shape of array), number that you want to put in it) => عمل ارراي بالشكل والرقم الذي تريد
a = np.full((2,5,5), 10)
print(a)

# np.random.randint(number of start, number of end, size=(array shape)) => عمل ارراي بالشكل الذي تريد وبارقام عشوائية
a = np.random.randint(10,100, size=(2,5,5))
print(a)

# np.zeros((shape of array)) => عمل ارراي بالشكل الذي تريد وكل عناصرها اصفار
a = np.zeros((2,5,5))
print(a)

# np.ones((shape of array)) => عمل ارراي بالشكل الذي تريد وكل عناصرها واحد
a = np.ones((2,5,5))
print(a)

# np.array_equal(array_1, array_2) => التحقق من ان الارراي الاولى تساوي الارراي الثانيه اي جميع عناصر الارراي الاولى تساوي جميع عناصر الارراي التانيه وبنفس الترتيب
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5])
np.array_equal(a, b) # True

a = np.array([1,2,3,4,5])
b = np.array([1,2,3,5,4])
np.array_equal(a, b) # False

# np.append(array_name, [item]) => الحاق عنصر واضافته في اخر الارراي
a = np.array([1,2,3,4,5])
a = np.append(a, [6,7])
print(a) # [1,2,3,4,5,6,7]

# np.insert(array_name, item position in the array, [item]) => اضاقه عنصر الى الارراي في موقع محدد
a = np.array([1,2,3,4,5])
a = np.insert(a, 1, [6,7])
print(a) # [1,6,7,2,3,4,5]


# np.delete(array_name, item index) => حذف العنصر صاحب الاندكس المكتوب من الارراي
# 1. delete one item from array 1 Dimension 
a = np.array([1,2,3,4,5])
print(np.delete(a, 1)) # [1,3,4,5]

# 2. delete two items or above from array 1 Dimension
a = np.array([1,2,3,4,5])
print(np.delete(a, [1,2])) # [1,4,5]

# 3. delete one item from array 2 Dimension
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(np.delete(a, 4)) # [1,2,3,4,6,7,8,9,10]

# 4. delete two items from array 2 Dimension
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(np.delete(a, 2, 1)) # [[1,2,4,5], [6,7,9,10]]


# array.transpose() => تحويل الصفوف الى اعمدة ووضعها داخل صفوف
# print(array.transpose()) = print(array.T)
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(a.transpose()) # [ [1,6], [2,7], [3,8], [4,9], [5,10] ]
print(a.T) # [ [1,6], [2,7], [3,8], [4,9], [5,10] ]

# np.stack((array_1, array_2)) => دمج 2 ارراي في ارراي واحدة مع الفصل بينهما اي ان كل ارراي منهما في قوس عن الاخرى وجميعها جوا قوس واحد كبير => [ [array_1], [array_2] ] => 3 Dimension Array
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
b = np.array([[11,12,13,14,15], [16,17,18,19,20]])
print(np.stack((a, b))) # [ [[1,2,3,4,5], [6,7,8,9,10]], [[11,12,13,14,15], [16,17,18,19,20]] ]

# np.vstack((array_1, array_2)) => دمج 2 ارراي في ارراي واحده دون الفصل بينها => [ array_1, array_2 ]
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
b = np.array([[11,12,13,14,15], [16,17,18,19,20]])
print(np.vstack((a, b))) # [ [1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20] ]

# np.hstack((array_1, array_2)) => دمج 2 ارراي في ارراي واحدة ولكن مع وضع اول قوس في الارراي الاولى مع اول قوس في الارراي التانيه في قوس واحد دون فواصل بينهما ووضع تاني قوس في الارراي الاولى مع تاني قوس في الارراي التانيه في قوس واحد دون فواصل والقوسين داخل قوس واحد كبير
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
b = np.array([[11,12,13,14,15], [16,17,18,19,20]])
print(np.hstack((a, b))) # [ [1,2,3,4,5,11,12,13,14,15], [6,7,8,9,10,16,17,18,19,20] ]

# np.random.randint() => اختيار رقم عشوائي صحيح
print(np.random.randint(1,10))
# np.random.random() => اختيار رقم عشوائي عشري بين صفر وواحد
print(np.random.random())
# np.random.choice() => اختيار رقم عشوائي من الارراي
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.random.choice(a))


# save array into file => np.save('file_name', array)
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
np.save('numbers.npy', a)

# Download numpy file in code => np.load('file_name')
a = np.load('numbers.npy')
print(a) # [[1,2,3,4,5], [6,7,8,9,10]]