# Write  a program to interchange first and last element of a list

"""
This function interchanges the first element with the last element and
it uses the indexes to interchange
"""
def interchange_first_and_last(nums):
    nums[0],nums[-1] = nums[-1],nums[0]
    return nums


# Write a program to check whether a string is a palindrome
"""
This functions checks if a string is a palindrome and returns true if
it is one,a palindrome is a string that can be reversed and remain the 
same.I chose to do it with slicing method
"""
def check_if_palindrome(str):
    return str == str[::-1]  


#Write a program to find the sum of elements in a tuple
"""
This program calculates the sum of numbers in a tuple
"""
def sum_of_tuple(nums):
    sum = 0

    for i in nums:
        sum += i

    return sum

