# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
    The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
    A valid Sudoku board (partially filled) is not necessarily solvable.
    Only the filled cells need to be validated.

Tags: Hash Table
'''


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 大行列
        for i in xrange(9):
            if not self.isValidList([board[i][j] for j in xrange(9)]) or \
               not self.isValidList([board[j][i] for j in xrange(9)]):
               return False

        # 小行列
        for i in xrange(3):
            # 大横行(1~3,3~6,6~9)
            for j in xrange(3):
                # 小格子(3x3): [m][n]先按列后按行 => 横行n
                if not self.isValidList([board[m][n] for n in xrange(3*j,3*j+3) for m in xrange(3*i,3*i+3)]):
                    return False
        return True

    def isValidList(self, slist):
        slist = filter(lambda x: x != '.', slist)
        return len(slist) == len(set(slist))


if __name__ == "__main__":
    board = [[1, '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 2, '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 3, '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 4, '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 5, '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', 6, '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', 7, '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', 8, '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', 9]]
    print Solution().isValidSudoku(board)
