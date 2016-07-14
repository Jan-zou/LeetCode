# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given an integer, write a function to determine if it is a power of two.

Tags: Math, Bit Manipulation
O(1) runtime; O(1) space
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0
