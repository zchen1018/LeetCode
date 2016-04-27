# 27. Remove Element
# Given an array and a value, remove all instances of that value in place and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Example:
# Given input array nums = [3,2,2,3], val = 3
# Your function should return length = 2, with the first two elements of nums being 2.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # filter(lambda x: x != val, nums) will not change nums
        while val in nums:
            nums.remove(val)
        
        return len(nums)



# 26. Remove Duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# For example,
# Given input array nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # i: position of distinct elements
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return i+1



# 66. Plus One
# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # dig_str = ''.join([str(x) for x in digits])
        # digs = int(dig_str) + 1
        # output = [int(x) for x in str(digs)]
        # return output
        if not digits: return 1
        
        digits_rev = digits[::-1]
        digits_rev[0] += 1
        i = 0
        while digits_rev[i] == 10:
            digits_rev[i] = 0
            i += 1
            if i < len(digits_rev):
                digits_rev[i] += 1
            else:
                digits_rev.append(1)
        return digits_rev[::-1]



# 67. Add Binary
# Given two binary strings, return their sum (also a binary string).
# For example,
# a = "11"
# b = "1"
# Return "100".
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return '{0:b}'.format(int(a, 2) + int(b, 2))



# 342. Power of Four
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# Example:
# Given num = 16, return true. Given num = 5, return false.
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Loop
        # if num <= 0:
        #     return False
        # else:
        #     while num%4 == 0:
        #         num = num/4
                
        # return num == 1
        
        return (num != 0 and num &(num-1) == 0 # make sure it's at least power of 2
                and num & 1431655765 != 0) # get rid of power of 2        
            
