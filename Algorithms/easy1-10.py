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