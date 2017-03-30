"""
Description:
Given a string, find the length of the longest substring without repeating characters.

Example:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
subsequence and not a substring.

Solution:
1. Sliding Window:
Use a HashSet to store all characters appeared in the current sliding window [i, j), then slide j to the right:
    If the next character is not in the HashSet, slide j further, add s[j] to the HashSet and update the longest length.
    Keep doing it until s[j] is already in the HashSet, at this point the longest length of substring in sliding window
    [i, j) is found.
    Do the above steps for every i and we can find the answer.

2. Sliding Window Optimized:
The above solution requires at most 2n steps. But if we use a HashMap to map the character and the index, it could be
optimized to require at most n steps.
The reason is that if character s[j] has a duplicate in the range [i, j) with index j', we don't need to increase i
little by little. We can skip all the elements in the range [i, j'] and let i to be j' + 1 directly.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = longest = 0
        usedchar = {}
        for i in range(len(s)):
            if s[i] in usedchar and start <= usedchar[s[i]]:
                start = usedchar[s[i]] + 1
            else:
                longest = max(longest, i - start + 1)
            usedchar[s[i]] = i
        return longest
