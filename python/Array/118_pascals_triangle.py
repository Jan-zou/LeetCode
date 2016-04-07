# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given numRows, generate the first numRows of Pascal's triangle.
    For example, given numRows = 5,
    Return
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]

Tags: Array
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in xrange(numRows):
            result.append([])
            for j in xrange(i+1):
                if j in (0,i):
                    result[i].append(1)  # two sides
                else:
                    result[i].append(result[i-1][j-1] + result[i-1][j])
        return result
