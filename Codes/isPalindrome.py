"""
Description:
Determine whether an integer is a palindrome. Do this without extra space.

Solution:
It is unnecessary to judge whether the reversed integer is overflow, because the reversed integer should be equal to
the origin integer if it is a palindromic integer, as a result, if the input is not overflow, the reversed integer is
not overflow.
It is easy to reverse the integer and compare it with the origin integer and judge whether they are equal
and get answer.
It can be optimized by only compare a the first half and the second half of the number.
"""


class Solution(object):
    def isPalindrom(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = x
        y = 0
        while tmp:
            y = y * 10 + tmp % 10
            tmp /= 10
        return y == x

    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x /= 10
        return y == x or y / 10 == x