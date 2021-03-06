# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Validate if a given string is numeric.
    Some examples:
        "0" => true
        " 0.1 " => true
        "abc" => false
        "1 a" => false
        "2e10" => true

    Note:
        It is intended for the problem statement to be ambiguous.
        You should gather all requirements up front before implementing one.

    Update (2015-02-10):
        The signature of the C++ function had been updated.
        If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

Tags: Math, String

Time: O(), Space: O()
'''


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        # 空格
        while i < len(s) and s[i] == ' ':
            i += 1
        # 正负号
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        while i < len(s):
