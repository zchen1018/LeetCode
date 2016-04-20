# 292. Nim Game
# You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
# Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.
# For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 > 0



# 258. Add Digits
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# For example:
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        while len(str(num_str)) > 1:
            num_str = self.digit_sum(num_str)
        
        return int(num_str)
    
    def digit_sum(self, num):
        num_str = str(num)
        s = 0
        for i in range(len(num_str)):
            s = s + int(num_str[i])
        return s
# Follow-up: without any loop       
# By https://en.wikipedia.org/wiki/Digital_root
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            digit_root = 0
        else:
            digit_root = int(num - 9*math.floor((num-1)/9))
            
        return digit_root



# 283. Move Zeroes
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        non_zero = [x for x in nums if x != 0]
        nums[:len(non_zero)] = non_zero
        nums[len(non_zero):] = [0] * (len(nums) - len(non_zero))



# 242. Valid Anagram
# Given two strings s and t, write a function to determine if t is an anagram of s.
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        # create a dictionary for each string and compare them    
        s_dic = {}
        for chr in s:
            if chr in s_dic.keys():
                s_dic[chr] += 1
            else:
                s_dic[chr] = 1
        
        t_dic = {}
        for chr in t:
            if chr in t_dic.keys():
                t_dic[chr] += 1
            else:
                t_dic[chr] = 1
            
        return s_dic == t_dic



# 168. Excel Sheet Column Title
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
def convertToTitle(n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        base = ord('A')
        while n:
            n, r = divmod(n - 1, 26)
            res = '{}{}'.format(chr(base + r), res)
        return res



# 171. Excel Sheet Column Number
# Given a column title as appear in an Excel sheet, return its corresponding column number.
# For example:
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in range(len(s)):
            temp = ord(s[len(s) - i -1]) - 64
            num += temp * 26**i
        return num



# 217. Contains Duplicate
# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        return len(nums_set) != len(nums)



# 169. Majority Element
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in set(nums):
            if nums.count(x) > len(nums)/2:
                return x



# 13. Roman to Integer
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
        sum = 0
        prev = 1001
        for i in range(len(s)):
            curr = roman_dict[s[i]]
            sum += curr
            if prev < curr:
                sum -= 2*prev
            prev = curr
        
        return sum



# 191. Number of 1 Bits
# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
        #return "{0:b}".format(n).count('1')