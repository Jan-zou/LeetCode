# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
    Did you use extra space?
    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

Tags: Array
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 设置两个数组，记录每行每列是否存在0
        # Time: O(m*n)
        # Space: O(m+n)
        m, n = len(matrix), len(matrix[0])
        row, column = [0]*m, [0]*n        # 1: 行列是否存在0

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    row[i] = column[j] = 1

        # row
        for i in xrange(m):
            if row[i]:
                matrix[i][:] = [0]*n

        # column
        for j in xrange(n):
            if column[j]:
                for i in xrange(m):
                    matrix[i][j] = 0

        return matrix


    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 复用第一行、第一列
        # Time: O(m*n)
        # Space: O(1)
        m, n = len(matrix), len(matrix[0])
        first_col, first_row = 0, 0        # 1: 记录第一行列是否为0

        # 修改第一行列的标记
        for i in xrange(m):
            if matrix[i][0] == 0:
                first_col = 1
        for j in xrange(n):
            if matrix[0][j] == 0:
                first_row = 1

        # 根据其他位置的数值，修改对应第一行列的数值
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 修改第一行列的数值
        if first_col:
            for i in xrange(m):
                matrix[i][0] = 0
        if first_row:
            for j in xrange(n):
                matrix[0][j] = 0

        return matrix


if __name__ == '__main__':
    matrix = [[1, 0, 1, 1],
              [1, 1, 0, 1],
              [1, 1, 1, 0],
              [1, 1, 1, 1]]
    print Solution().setZeroes(matrix)
    matrix = [[1, 0, 1, 1],
              [1, 1, 0, 1],
              [1, 1, 1, 0],
              [1, 1, 1, 1]]
    print Solution().setZeroes2(matrix)
