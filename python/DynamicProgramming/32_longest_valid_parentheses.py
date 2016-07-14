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
    # O(n) runtime; O(n) space
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

    # O() runtime; O(1) space
    def longestValidParentheses2(self, s):
        return max(self.length(xrange(len(s)), -1, '(', s), self.length(reversed(xrange(len(s))), len(s), ')', s))

    def length(self, it, start, c, s):
        depth, longest = 0, 0
        for i in it:
            if s[i] == c:
                depth += 1
            else:
                depth -= 1
                if depth < 0:
                    start, depth = i, 0
                elif depth == 0:
                    longest = max(longest, abs(i - start))
        return longest

if __name__ == '__main__':
    print Solution().longestValidParentheses(')()())')
    print Solution().longestValidParentheses2(')()())')
