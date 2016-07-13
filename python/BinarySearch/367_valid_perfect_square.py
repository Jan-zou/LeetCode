# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a positive integer num, write a function which returns True if num is a perfect square else False.

    Note: Do not use any built-in library function such as sqrt.
    Example 1:
        Input: 16
        Returns: True
    Example 2:
        Input: 14
        Returns: False

Tags: Binary Search, Math
'''

class Solution(object):
    # 每次比较num/2的平方和num的平方，缩小范围后的数k的平方小于num的平方时；遍历k~2K，看其中是否有数的平方为所求。
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        x = num / 2
        t = x * x
        while t > num:
            x = x / 2
            t = x * x

        i = x
        while i < x * 2:
            if i * i == num:
                return True
            i += 1
        return False

    # 从1搜索到sqrt(num)，看有没有平方正好等于num的数
    def isPerfectSquare2(self, num):
        i = 1
        while i <= num/i:
            if i*i == num:
                return True
            i += 1
        return False

    # binary search
    def isPerfectSquare3(self, num):
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            t = mid * mid
            if t == num:
                return True
            elif t < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

    # 数学性质: 完全平方数是一系列奇数之和 - O(sqrt(n))runtime
    def isPerfectSquare4(self, num):
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


if __name__ == '__main__':
    print Solution().isPerfectSquare(16)
    print Solution().isPerfectSquare2(14)
    print Solution().isPerfectSquare3(16)
    print Solution().isPerfectSquare4(14)
