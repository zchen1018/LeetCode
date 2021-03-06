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
        # For a 32-bit int, the maximal value is Maxint = 2^32/2 - 1
        # Thus, the maximal power of 3 is floor(log_3^Maxint) = 19
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



# 231. Power of Two
# Given an integer, write a function to determine if it is a power of two.
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max_power = math.floor(math.log(2**32/2 -1, 2))
        return n > 0 and 2**max_power % n == 0



# 121. Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price, max_profit = float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
            
        return max_profit



# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_l1 = l1
        cur_l2 = l2
        
        head = ListNode(None)
        output = head
        
        while cur_l1 and cur_l2:
            if cur_l1.val < cur_l2.val:
                output.next = cur_l1
                cur_l1 = cur_l1.next
            else:
                output.next = cur_l2
                cur_l2 = cur_l2.next
            output = output.next
        else:
            if cur_l1 == None:
                output.next = cur_l2
            else:
                output.next = cur_l1
        
        return head.next



# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyNode = p0 = ListNode(0)
        dummyNode.next = head
        
        # p0->p1->p2->p2.next ----> p0->p2->p1->p2.next
        while p0.next and p0.next.next:
          p1, p2 = p0.next, p0.next.next
          p0.next, p1.next, p2.next = p2, p2.next, p1
          p0 = p1

        return dummyNode.next



# 198. House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
class Solution(object):
    #def rob(self, nums):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # special case
        # if len(nums) < 1:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # # opt: max number of money until house i
        # opt = [0] * len(nums)
        # # base case
        # opt[0] = nums[0]
        # opt[1] = max(nums[0], nums[1])
        
        # for i in range(2, len(nums)):
        #     opt[i] = max(opt[i-2] + nums[i], opt[i-1])
        
        # return opt[-1]

        prev, curr = 0, 0
        
        for x in nums:
            prev, curr = curr, max(x+prev, curr)

        return curr