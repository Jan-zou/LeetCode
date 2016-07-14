# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given an integer, write a function to determine if it is a power of three.
    Follow up:
    Could you do it without using any loop / recursion?

Tags: Math
O(1) runtime; O(1) space
'''

import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 1
        while x <= n:
            if x == n:
                return True
            x = x * 3
        return False

    # without loop - 精度误差小于1e-10
    def isPowerOfThree2(self, n):
        if n > 0:
            a = math.log(n) / math.log(3.0)
        else:
            a = 0.5

        b = round(a)
        if abs(a-b) < 1e-10:
            return True
        else:
            return False

if __name__ == '__main__':
    print Solution().isPowerOfThree(9)
    print Solution().isPowerOfThree2(9)
    print Solution().isPowerOfThree2(8)
