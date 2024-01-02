"""
Monotonic Array - An array is either monotone increasing or monotone decreasing. 
An array is monotone increasing if all its elements from left to right are non-decreasing.
An array is monotone decreasing if all  its elements from left to right are non-increasing. 
Given an integer array return true if the given array is monotonic, or false otherwise.
"""

def monotonic_array(input_array):

    if input_array[0] < input_array[1]:
        print(True)
    else:
        print(False)

monotonic_array([1, 7, 9, 12])


    