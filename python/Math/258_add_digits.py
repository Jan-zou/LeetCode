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
    1. A naive implementation of the above process is trivial. Could you come up with other methods?
    2. What are all the possible results?
    3. How do they occur, periodically or randomly?
    4. You may find this [Wikipedia article](https://en.wikipedia.org/wiki/Digital_root) useful.

Tags: Math
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 三位数abc: abc=100a+10b+c=(a+b+c)+(99a+9b) 第一项为0-9之间的数字(即所求)，第二项一定可以被9整除
        # Time: O(1); Space: O(1)
        return (num - 1) % 9 + 1 if num > 0 else 0


    def addDigits2(self, num):
        while num > 9:
            num = num/10 + num%10
        return num

