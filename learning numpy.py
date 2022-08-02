import numpy as np 


#Call np.array to create a NumPy matrix with your own hand-picked values.
#  For example, the following call to np.array creates an 8-element vector:

one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print(one_dimensional_array)

#You can also use np.array to create a two-dimensional matrix. To create a two-dimensional matrix, specify an extra layer of square brackets. 
# For example, the following call creates a 3x2 matrix:

two_dimensional_array = np.array([[2,3,4],[5,2,5],[3,2,9]])
print(two_dimensional_array)

two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print(two_dimensional_array)

#To populate a matrix with all zeroes, call np.zeros. 
# To populate a matrix with all ones, call np.ones.


sequence_of_integers = np.arange(5, 12)
print(sequence_of_integers)

#Notice that np.arange generates a sequence that includes the 
# lower bound (5) but not the upper bound (12).

#np.random.randint generates random integers between a low and high value.
# The following call populates a 6-element vector with random integers between 50 and 100.

random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
print(random_integers_between_50_and_100)

#Note that the highest generated integer np.random.randint is one less than the high argument.
#To create random floating-point values between 0.0 and 1.0, call np.random.random.

random_floats_between_0_and_1 = np.random.random([6])
print(random_floats_between_0_and_1) 

#to add or subtract two vectors or matrices, linear algebra requires that the two operands have the same dimensions
#NumPy uses a trick called broadcasting to virtually expand the smaller operand to dimensions

random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print(random_floats_between_2_and_3)

# to multiply each cell in a vector by 3
random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print(random_integers_between_150_and_300)

