# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a positive integer, return its corresponding column title as appear in an Excel sheet.

    For example:
        1 -> A
        2 -> B
        3 -> C
        ...
        26 -> Z
        27 -> AA
        28 -> AB

Tags: Math
Time: O(logn); Space: O(1)
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''

        while n:
            result += chr((n-1) % 26 + ord('A'))
            n = (n-1) / 26
        return result[::-1]

if __name__ == "__main__":
    for i in xrange(1, 29):
        print Solution().convertToTitle(i)
