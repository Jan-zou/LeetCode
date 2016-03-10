# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Tags: Stack, String
Time: O(n)
Space: O(n)
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        lookup = {'[':']', '(': ')', '{': '}'}
        for parentnese in s:
            if parentnese in lookup:
                stack.append(parentnese)
            elif len(stack) == 0 or lookup[stack.pop()] != parentnese:
                return False

        return len(stack) == 0

if __name__ == "__main__":
    print Solution().isValid("()[]{}")
    print Solution().isValid("()[{]}")
