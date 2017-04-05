"""
Description:
Reverse digits of an integer.

Examples:
x = 123, return 321
x = -123, return -321
Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

Solution1:
Get the tail of the input integer by keep modulo it by 10 and multiply the tail by ten to construct the new number.

Solution2:
Use python built-in function to reverse the string.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        result = 0
        absolutex = abs(x)
        while absolutex != 0:
            rev = rev * 10 + absolutex % 10
            absolutex = absolutex / 10
        if x > 0 and rev < 2147483648:
            result = rev
        elif x < 0 and -rev >= -2147483648:
            result = -rev
        else:
            result = 0
        return result

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return x if x >= -2147483648 and x < 2147483648 else 0
