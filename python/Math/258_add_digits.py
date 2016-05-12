# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
    For example:
    Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:
    A naive implementation of the above process is trivial. Could you come up with other methods? Show More Hint

Tags: Math
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num - 1) % 9 + 1 if num > 0 else 0

    def addDigits2(self, num):
        while num > 9:
            num = num/10 + num%10
        return num

