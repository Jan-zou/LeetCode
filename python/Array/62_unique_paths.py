# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    How many possible unique paths are there?
Note: m and n will be at most 100.

Tags: Array, Dynamic Programming
'''


class Solution(object):
    # 深搜, 大集合会超时
    # Time: O(n^4); Space: O(n)
    def uniquePaths(self, m, n):
        if m < 1 or n < 1:
            return 0

        if m == 1 or n == 1:
            return 1

        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    # 动态规划
    # 状态f[i][j]表示从起点(1,1)到达(i,j)的路线条数，
    # 状态转移方程为f[i][j] = f[i-1][j] + f[i][j-1]
    # Time: O(n^2); Space: O(n)
    def uniquePaths2(self, m, n):
        f = [1] * n
        for i in xrange(1, m):
            for j in xrange(1, n):
                f[j] = f[j] + f[j-1]
        return f[n-1]
