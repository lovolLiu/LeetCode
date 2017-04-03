"""
Description:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);

Example:
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

Solution:
We can use nRows String to store each line of the converted string and combine them together to get the result.
The key to this problem is to use a variable incre to tell the pointer which direction it should go, if the pointer is
at the first line, than go down, if it is at the last line, than go up.
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        incre = 1
        index = 0
        slist = []
        for i in range(numRows):
            slist.append("")
        for i in range(len(s)):
            slist[index] += s[i]
            if index == 0:
                incre = 1
            if index == numRows - 1:
                incre = -1
            index += incre
        result = ""
        for i in range(numRows):
            result += slist[i]
        return result