# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
    For example,
    Given the following matrix:
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
    You should return [1,2,3,6,9,8,7,4,5].

Tags: Array
Time: O(m * n); Space: O(1)
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result

        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left <= right and top <= bottom:
            for j in xrange(left, right+1):
                result.append(matrix[top][j])
            for i in xrange(top+1, bottom):
                result.append(matrix[i][right])
            for j in reversed(xrange(left, right+1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(xrange(top+1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left+1, right-1, top+1, bottom-1

        return result


if __name__ == '__main__':
    matrix = [
              [ 1, 2, 3 ],
              [ 4, 5, 6 ],
              [ 7, 8, 9 ]
             ]
    print Solution().spiralOrder(matrix)
