# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
    For "(()", the longest valid parentheses substring is "()", which has length = 2.
    Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

Tags: Dynamic Programming, String
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        longest, last = 0, -1
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif not stack:
                last = i
            else:
                stack.pop()
                if not stack:
                    longest = max(longest, i-last)
                else:
                    longest = max(longest, i-stack[-1])
        return longest



if __name__ == '__main__':
    print Solution().longestValidParentheses(')()())')

