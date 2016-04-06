# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a triangle, find the minimum path sum from top to bottom.
    Each step you may move to adjacent numbers on the row below.
    For example, given the following triangle
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note:
    Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Tags: Array, Dynamic Programming
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        current = triangle[0] + [float('inf')]
        for i in xrange(1, len(triangle)):
            next = []
            for j in xrange(0, i+1):
                next.append(triangle[i][j] + min(current[j-1], current[j]))
            current = next + [float('inf')]
        return reduce(min, current)


if __name__ == '__main__':
    triangle = [
                     [2],
                    [3,4],
                   [6,5,7],
                  [4,1,8,3]
                ]
    print Solution().minimumTotal(triangle)
