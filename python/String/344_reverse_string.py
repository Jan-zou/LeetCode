# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Write a function that takes a string as input and returns the string reversed.

Example:
    Given s = "hello", return "olleh".

Tags: Two Pointers, String
'''


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
