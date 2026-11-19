def not_string(str):
    """
    Given a string, return a new string where "not" has been added to the front.
    However, if the string already begins with "not", return the string unchanged.
    not_string("cat") returns "notcat"
    not_string("not") returns not
    """ 
    if str[0:3] == "not":
        return str
    else:
        return "not" + str

def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """

    min_index = lst.index(min(lst))
    lst[0], lst[min_index] = lst[min_index], lst[0]
    return lst


def count_spaces(string):
 """
 Use comprehension to count the number of spaces in a string.
 *** Important: your code must use comprehensions and should not be more than
 two lines of code including the return statement ***
 count_spaces("the cow jumped over the moon") returns 5
 """

 return sum([1 for char in string if char == " "])

def sum67(nums):
    '''
    Return the sum of the numbers in the array, except ignore sections
    of numbers starting with a 6 and extending to the next 7
    (every 6 will be followed by at least one 7).
    Return 0 for no numbers.
    sum67([1, 2, 2]) → 5
    sum67([1, 2, 2, 6, 99, 99, 7]) → 5
    sum67([1, 1, 6, 7, 2]) → 4
    '''

    total = 0
    i = 0

    while i < len(nums):
        if nums[i] == 6:
            i += 1
            while nums[i] != 7:
                i+= 1
            i += 1
        else:
            total += nums[i]
            i += 1

def minmaxdiff(nums):
 """
 Given an array length 1 or more of ints, return the difference between the largest
 and smallest values in the array.
 minmaxdiff([1,2,3,4,5]) returns 4
 """
 return max(nums) - min(nums)

