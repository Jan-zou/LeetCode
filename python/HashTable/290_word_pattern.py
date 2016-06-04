# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a pattern and a string str, find if str follows the same pattern.
    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
Examples:
    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
    You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Tags: Hash Table
Time: O(n); Space: O(n)
'''


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()    # Space: O(n)
        if len(pattern) != len(words):
            return False

        w2p, p2w = {}, {}
        for p, w in zip(pattern, words):
            if w not in w2p and p not in p2w:
                # Build mapping. Space: O(c)
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
            # elif p not in p2w or p2w[p]!=w:
                # Contradict mapping.
                return False
        return True


if __name__ == '__main__':
    print Solution().wordPattern('abba', 'dog cat cat dog')
