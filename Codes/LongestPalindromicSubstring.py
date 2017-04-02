"""
Descritpion:
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"

Solution:
Expand Around Center:
Use two pointer to point on the center i of a substring, expand them one step a time towards head and tail of the string,
compare the characters pointed by the two pointers, keep expanding them until the two characters are not equal, then we
have found the longest palindromic substring with the center located in i. Iterate every character in the string and we
can find the longest palindromic substring.
Note there are 2n - 1 centers to expand because for palindromic substring with odd length (eg. aba), they have only one
center, for palindromic substring with even length(eg. abba), they have two centers, so we have to check these two
conditions for every character in the string.

Time Complexity: O(n^2)
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(start, end, s):
            while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1:end]
        longest = ""
        temp = ""
        for i in range(len(s)):
            temp = helper(i, i, s)
            if len(temp) >= len(longest):
                longest = temp
            temp = helper(i, i + 1, s)
            if len(temp) >= len(longest):
                longest = temp
        return longest