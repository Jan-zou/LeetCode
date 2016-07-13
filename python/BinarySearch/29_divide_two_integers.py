# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Divide two integers without using multiplication, division and mod operator.
    If it is overflow, return MAX_INT.

Tags: Math, Binary Search

分析:
    不能用乘除、取模，剩下的只有加减和位运算。
    （位运算中左移1位相当于"x2"）
    直观的方法是: 除数中不断减去被除数; 每次将被除数翻倍，以优化速度。（注意溢出判断）
'''


class Solution(object):
    # O(logn) runtime, O(1) space
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        MAX_INT, MIN_INT = 2**31 - 1, -(2**31)
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            inc = divisor
            i = 0
            while dividend >= inc:
                dividend -= inc
                result += 1 << i
                inc <<= 1
                i += 1
        result = result*sign
        return result if MIN_INT <= result <= MAX_INT else MAX_INT


if __name__ == '__main__':
    print Solution().divide(123, 12)
    print Solution().divide(123, -12)
    print Solution().divide(-123, 12)
    print Solution().divide(-123, -12)
