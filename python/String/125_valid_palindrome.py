# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    For example,
    "A man, a plan, a canal: Panama" is a palindrome.
    "race a car" is not a palindrome.

Note:
    Have you consider that the string might be empty? This is a good question to ask during an interview.
    For the purpose of this problem, we define empty string as valid palindrome.

Tags: Two Pointers, String
'''


class Solution(object):
    # O(n)runtime, O(1)space
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not s[i].isalnum():   #isalnum()方法检测字符串是否由字母和数字组成
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    print Solution().isPalindrome('A man, a plan, a canal: Panama')    # true
    print Solution().isPalindrome('race a car')    # false
    print Solution().isPalindrome('s')    # true
    print Solution().isPalindrome('')    # true
