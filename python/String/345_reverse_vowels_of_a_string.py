# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Write a function that takes a string as input and reverse only the vowels of a string.
    Example 1:
    Given s = "hello", return "holle".

    Example 2:
    Given s = "leetcode", return "leotcede".

Tags: Two Pointers, String
'''


import re

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

    # Two pointers - Time: O(n), Space: O(n)
    def reverseVowels2(self, s):
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        i, j = 0, len(s)-1
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            else:
                if s[i] not in vowels:
                    i += 1
                if s[j] not in vowels:
                    j -= 1
        return ''.join(s)


if __name__ == '__main__':
    print Solution().reverseVowels('hello')
    print Solution().reverseVowels2('hello')
