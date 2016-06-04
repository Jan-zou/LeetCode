# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given two strings s and t, determine if they are isomorphic.
    Two strings are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters.
    No two characters may map to the same character but a character may map to itself.
    For example,
        Given "egg", "add", return true.
        Given "foo", "bar", return false.
        Given "paper", "title", return true.
    Note: You may assume both s and t have the same length.

Tags: Hash Table
Time: O(n); Space: O(1)
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        lookup = {}
        for i in xrange(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        return True

if __name__ == '__main__':
    print Solution().isIsomorphic('ab', 'aa')
    print Solution().isIsomorphic('foo', 'bar')
