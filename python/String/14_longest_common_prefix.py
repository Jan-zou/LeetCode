# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Write a function to find the longest common prefix string amongst an array of strings.

Tags: String
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        lognest = strs[0]
        for string in strs[1:]:
            i = 0
            while i < len(string) and i < len(lognest) and string[i] == lognest[i]:
                i += 1
            lognest = lognest[:i]
        return lognest


if __name__ == '__main__':
    Solution().longestCommonPrefix(["hello", "heaven", "heavy"])
