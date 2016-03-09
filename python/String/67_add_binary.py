# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given two binary strings, return their sum (also a binary string).
    For example,
        a = "11"
        b = "1"
        Return "100".

Tags: Math, String
Time: O(n)
Space: O(1)
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        carry, val = 0, 0
        n = max(len(a), len(b))

        for i in xrange(n):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            carry, val= val / 2, val % 2
            result += str(val)

        if carry:
            result += str(carry)

        return result[::-1]


if __name__ == '__main__':
    print Solution().addBinary('11', '1')
