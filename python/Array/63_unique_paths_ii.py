# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Follow up for "Unique Paths":
    Now consider if some obstacles are added to the grids. How many unique paths would there be?
    An obstacle and empty space is marked as 1 and 0 respectively in the grid.
    For example,
    There is one obstacle in the middle of a 3x3 grid as illustrated below.

    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    The total number of unique paths is 2.
Note: m and n will be at most 100.

Tags: Array, Dynamic Programming
'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [0]*n

        if obstacleGrid[0][0] == 0:
            f[0] = 1

        for j in xrange(1,n):
            if obstacleGrid[0][j] == 1:
                f[j] = 0
            else:
                f[j] = f[j-1]

        for i in xrange(1,m):
            if obstacleGrid[i][0] == 1:
                f[0] = 0

            for j in xrange(1,n):
                if obstacleGrid[i][j] == 1:
                    f[j] = 0
                else:
                    f[j] = f[j] + f[j-1]

        return f[n - 1]
