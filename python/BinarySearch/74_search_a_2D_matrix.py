# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Write an efficient algorithm that searches for a value in an m x n matrix.
    This matrix has the following properties:
        + Integers in each row are sorted from left to right.
        + The first integer of each row is greater than the last integer of the previous row.

    For example,
        Consider the following matrix:
        [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        Given target = 3, return true.

Tags: Array, Binary Search
O(logn) runtime; O(1) space
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m*n-1
        while i <= j:
            mid = i + (j - i) // 2
            val = matrix[mid//n][mid%n]
            if target == val:
                return True
            elif val < target:
                i = mid + 1
            else:
                j = mid - 1

        return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    print Solution().searchMatrix(matrix, 3)
