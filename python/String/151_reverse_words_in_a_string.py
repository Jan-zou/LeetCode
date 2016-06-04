# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given an input string, reverse the string word by word.
    For example,
        Given s = "the sky is blue",
        return "blue is sky the".

    Update (2015-02-12):
        For C programmers: Try to solve it in-place in O(1) space.

    Clarification:
    What constitutes a word?
        A sequence of non-space characters constitutes a word.
    Could the input string contain leading or trailing spaces?
        Yes. However, your reversed string should not contain leading or trailing spaces.
    How about multiple spaces between two words?
        Reduce them to a single space in the reversed string.

Tags: String
Time: O(n), Space: O(n)
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return ' '.join(s.split()[::-1])
        return ' '.join(reversed(s.split()))
