# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Tags: Dynamic Programming

设f(n)表示爬n阶楼梯的不同方法数，为了爬到第n阶楼梯，有两种选择：
+ 从第n-1阶前进1步
+ 从第n-1阶前进2步
f(n)=f(n-1)+f(n-2)    斐波那契数列

递归；迭代；数学公式
'''
import math


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in xrange(n):
            prev, current = current, prev + current
        return current


if __name__ == "__main__":
    print Solution().climbStairs(2)
