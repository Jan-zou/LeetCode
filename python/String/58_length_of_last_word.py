# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
    return the length of last word in the string.
    If the last word does not exist, return 0.
Note:
    A word is defined as a character sequence consists of non-space characters only.
    For example,
    Given s = "Hello World",
    return 5.

Tags: String
'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Splitting an empty string with a specified separator returns ['']; if not separator,returns []
        return len(s.strip().split(' ')[-1])

    def lengthOfLastWord2(self, s):
        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length


if __name__ == '__main__':
    print Solution().lengthOfLastWord('')
    print Solution().lengthOfLastWord(' ')
    print Solution().lengthOfLastWord('Hello World')

