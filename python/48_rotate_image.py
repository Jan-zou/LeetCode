# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    You are given an n x n 2D matrix representing an image.
    Rotate the image by 90 degrees (clockwise).
Follow up:
    Could you do this in-place?

Tags: Array
Time: O(n^2)
Space: O(1)
'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 先沿着副对角线翻转一次，再沿着水平中线翻转一次(或先沿着水平中线翻转一次，再沿着主对角线翻转一次)
        n = len(matrix)

        # anti-diagonal mirror
        for i in xrange(n):
            for j in xrange(n-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

        # horizontal mirror
        for i in xrange(n/2):
            for j in xrange(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

        return matrix


    def rotate2(self,matrix):
        return [list(reversed(x)) for x in zip(*matrix)]    # zip-按列


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print Solution().rotate(matrix)
