# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a string S, find the length of the longest substring T that contains at most two distinct characters.
    For example,
    Given S = “eceba”,
    T is "ece" which its length is 3.

Tags: Hash Table, String
'''

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start, distinct_count, visited = 0, 0, 0, [0 for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1
            visited[ord(char)] += 1

            while distinct_count > 2:
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1

            longest = max(longest, i - start + 1)
        return longest


if __name__ == '__main__':
    print Solution().lengthOfLongestSubstringTwoDistinct('eceba')
