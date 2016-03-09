# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given two strings s and t, write a function to determine if t is an anagram of s.
    For example,
    s = "anagram", t = "nagaram", return true.
    s = "rat", t = "car", return false.
Note:
    You may assume the string contains only lowercase alphabets.
Follow up:
    What if the inputs contain unicode characters? How would you adapt your solution to such case?

Tags: Hash Table, Sort
'''


class Solution(object):
    # Time: O(n); Space: O(1)
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = {}
        for w in s:
            if w.lower() in count:
                count[w.lower()] += 1
            else:
                count[w.lower()] = 1

        for w in t:
            if w.lower() in count:
                count[w.lower()] -= 1
            else:
                count[w.lower()] = -1

            if count[w.lower()] < 0:
                return False

        return True

    # Time: O(nlogn); Space: O(n)
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    Solution().isAnagram('anagram', 'nagaram')
