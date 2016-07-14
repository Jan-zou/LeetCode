# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    For example, given n = 3, a solution set is:
        "((()))", "(()())", "(())()", "()(())", "()()()"

Tags: Backtracking, String

Time:  O(4^n / n^(3/2)) ~= Catalan numbers
Space: O(n)
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate(result, '', n, n)
        return result

    def generate(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.generate(result, current + '(', left-1, right)
        if left < right:
            self.generate(result, current + ')', left, right-1)

if __name__ == '__main__':
    print Solution().generateParenthesis(3)
