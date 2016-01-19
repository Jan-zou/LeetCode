# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows:

        string convert(string text, int nRows);
    `convert("PAYPALISHIRING", 3)` should return `"PAHNAPLSIIGYIR"`.

Tag: String
Time: O(n)
Space: O(1)
'''


class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @param {string}
    def convert(self, s, numRows):
        step, zigzag = 2 * numRows - 2, ""    # 4 char a team
        if s is None or len(s) == 0 or numRows <= 0:
            return ""
        if numRows == 1:
            return s
        for i in range(numRows):
            for j in range(i, len(s), step):
                zigzag += s[j]    # When i = 0 or i = 2, fill first row, get after four char in origin characters
                if i > 0 and i < numRows - 1 and j + step - 2 * i < len(s):
                    zigzag += s[j + step - 2 * i]
        return zigzag

if __name__ == '__main__':
    print Solution().convert("PAYPALISHIRING", 3)
