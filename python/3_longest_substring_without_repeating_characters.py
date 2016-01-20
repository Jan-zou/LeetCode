# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a string, find the length of the longest substring without repeating characters.
    For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
    For "bbbbb" the longest substring is "b", with the length of 1.

Tags: Hash Table, Two Pointers, String
Time: O(n)
Space: O(1)

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start, visited = 0, 0, [False for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:    # ord() return a ASCII value of a character
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest

    def alengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        # position of last ecountered char
        last_pos = {s[0]: 0}
        # the length of the longest substring ending at this index
        longest_sub = [1] * len(s)

        # Iterating through the string
        for i in range(1, len(s)):
            seen = last_pos.get(s[i], -1)
            # if the current char was last seen outside of longest substring
            # ending on the previous index, we can increase the the longest
            # substring ending at i by 1
            if seen < i - longest_sub[i - 1]:
                longest_sub[i] = longest_sub[i - 1] + 1
            else:
                longest_sub[i] = i - seen
            last_pos[s[i]] = i
        return max(longest_sub)



if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("abcabcbb")
    print Solution().lengthOfLongestSubstring("qwkwwe")
    print Solution().alengthOfLongestSubstring("qwkwwe")

