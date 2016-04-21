# 83. Remove Duplicates from Sorted List
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while (curr != None) and (curr.next != None):
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head



# 70. Climbing Stairs
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(n-2):
            a, b = b, a+b
        return b



# 263. Ugly Number
# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
# Note that 1 is typically treated as an ugly number.
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        ugly_prime = [2, 3, 5]
        res = num
        while res > 1:
            res_temp = res
            for x in ugly_prime:
                if res % x == 0:
                    res = res / x
            if res_temp == res:
                return False
        return True



# 326. Power of Three
# Given an integer, write a function to determine if it is a power of three.
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # loop version
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n/3
        return n == 1

        # without loop
        # return n > 0 and 3**19 % n == 0



# 202. Happy Number
# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
# Example: 19 is a happy number
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ckc = set()
        n_str = str(n)
        dig_sqr_sum = 0
        
        while dig_sqr_sum != 1:
            dig_sqr_sum = sum([int(x)**2 for x in n_str])
            n_str = str(dig_sqr_sum)
            if dig_sqr_sum in ckc: # a circle is detected
                return False
            else:
                ckc.add(dig_sqr_sum)
            
        else:
            return True