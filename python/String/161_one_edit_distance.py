# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given two strings S and T, determine if they are both one edit distance apart.

    Hint:
    1. If |n – m| is greater than 1, we know immediately both are not one-edit distance apart.
    2. It might help if you consider these cases separately, m == n and m ≠ n.
    3. Assume that m is always ≤ n, which greatly simplifies the conditional statements.
       If m > n, we could just simply swap S and T.
    4. If m == n, it becomes finding if there is exactly one modified operation.
       If m ≠ n, you do not have to consider the delete operation. Just consider the insert operation in S.

Tags: String
Time: O(m+n); Space: O(1)
'''


class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: String
        :type t: String
        :rtype: Boolean
        """
        '''
        Assume X represents the one-edit character.
        There are three one-edit distance operations that could be applied to S.
        i. Modify operation – Modify a character to X in S.
            S = “abcde”
            T = “abXde”
        ii. Insert operation – X was inserted before a character in S.
            S = “abcde”
            T = “abcXde”
        iii. Append operation – X was appended at the end of S.
￼￼￼￼￼￼￼￼    S = “abcde”
            T = “abcdeX”
        '''
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        if n - m > 1:
            return False

        i, shift = 0, n - m
        while i < m and s[i] == t[i]:
            i += 1
        if shift == 0:
            i += 1
        while i < m and s[i] == t[i+shift]:
            i += 1

        return i == m


if __name__ == '__main__':
    print Solution().isOneEditDistance('teacher', 'teachar')
    print Solution().isOneEditDistance("teacher", "teache")
