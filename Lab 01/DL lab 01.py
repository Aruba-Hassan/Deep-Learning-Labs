# task 1
import tensorflow as tf
tensor = tf.random.uniform((3,3))
print ("Tensor: \n" , tensor)
print ("Tensor Sum: \n", tf.reduce_sum(tensor))
print ("Tensor Mean: \n",tf.reduce_mean(tensor))
print ("Tensor Maximum: \n",tf.reduce_max(tensor))
# task 2
import tensorflow as tf
tensor = tf.constant([[[4,7,8],[9,7,0]],
                      [[367,87,99],[54,87,66]]])
print("Specific Element: \n" , tensor[1,0,2])
print("2D Slice: \n" , tensor[1])
print("1D Slice: \n" , tensor[0,1])
# task 3
import numpy as np
array = np.random.rand(6)
print("Array: \n" , array)
print("Ascending Order: \n" , np.sort(array))
print("Descending Order: \n" , np.sort(array)[::-1])
#task 4
import numpy as np
matrix = np.array([[367,99],[33,99]])
print("Transpose: \n" , matrix.T)
print("Inverse: \n" , np.linalg.inv(matrix))
# task 5
import numpy as np
Array_2D = np.array([[3,1,9],[5,7,6],[9,6,1]])
print("Array: \n" , Array_2D)
row_sum = np.sum(Array_2D , axis=1)
column_mean = np.mean(Array_2D , axis=0)
standard_deviation = np.std(Array_2D)
print("Row Sum: \n", row_sum)
print("Column Mean: \n", column_mean)
print("Standard Deviation: \n", standard_deviation)
# task 6
import numpy as np
import tensorflow as tf
numpy_array = np.array([367,98,77,55])
tensor_array = tf.constant(array)
print("Tensor Array: \n" ,tensor_array)
# task7
import tensorflow as tf
tensor = tf.constant([367,88,77])
print("Addition: \n" , tensor + 5)
print("Multiplication: \n" , tensor * 367)
# task 8
import numpy as np
import tensorflow as tf
def update_tensor_array(array):
  tensor_array = tf.constant(array)
  tensor_array = tensor_array + 10
  return tensor_array
array = np.array([367,88,99])
print("Updated tensor array: \n" , update_tensor_array(array))