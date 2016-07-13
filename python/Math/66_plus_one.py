# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a non-negative number represented as an array of digits, plus one to the number.
    The digits are stored such that the most significant digit is at the head of the list.

Tags: Array, Math
Time: O(n); Space: O(1)

高精度加法: 一个非负数用一个数组表示，加1。
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(xrange(len(digits))):
            digits[i] += carry
            carry = digits[i] / 10         # 进位
            digits[i] = digits[i] % 10     # mod

        if carry:
            digits.insert(0,carry)

        return digits


if __name__ == "__main__":
    print Solution().plusOne([9, 9, 9, 9])
