# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
    find the area of largest rectangle in the histogram.
    For example,
        Given heights = [2,1,5,6,2,3], return 10.

Tags: Array, Stack
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """


if __name__ == '__main__':
    print Solution().largestRectangleArea([2,1,5,6,2,3])
    print Solution().largestRectangleArea([2, 0, 2])
