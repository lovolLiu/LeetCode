"""
Description:
Implement atoi to convert a string to an integer.

Requirements:
The function first discards as many whitespace characters as necessary until the first non-whitespace character
is found.

Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits
as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have
no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of
representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Solution:
The implementation is not hard, but it is hard to come up the requirements.
"""


class Solution(object):
    class Solution(object):
        def myAtoi(self, s):
            """
            :type str: s
            :rtype: int
            """
            strips = s.strip()
            index = 0
            flag = 1
            res = 0
            if index < len(strips) and strips[index] == '-':
                flag = -1
                index += 1
            elif index < len(strips) and strips[index] == '+':
                index += 1
            while index < len(strips):
                if strips[index] < '0' or strips[index] > '9':
                    return res * flag
                digit = ord(strips[index]) - ord('0')
                if flag == 1 and res * 10 + digit > 2147483647:
                    return 2147483647
                if flag == -1 and res * 10 + digit > 2147483648:
                    return -2147483648
                res = res * 10 + digit
                index += 1
            return res * flag
