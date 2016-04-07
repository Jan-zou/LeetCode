# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given an index k, return the kth row of the Pascal's triangle.
    For example, given k = 3,
    Return [1,3,3,1].
Note:
    Could you optimize your algorithm to use only O(k) extra space?

Tags: Array
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for i in xrange(rowIndex+1):
            result.append([])
            for j in xrange(i+1):
                if j in (0,i):
                    result[i].append(1)  # two sides
                else:
                    result[i].append(result[i-1][j-1] + result[i-1][j])
        return result[-1]

    def getRow(self, rowIndex):
        result = [0] * (rowIndex + 1)
        for i in xrange(rowIndex + 1):
            old = result[0] = 1
            for j in xrange(1, i + 1):
                old, result[j] = result[j], old + result[j]
        return result
