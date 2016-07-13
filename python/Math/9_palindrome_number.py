# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Determine whether an integer is a palindrome. Do this without extra space.

    Some hints:
    Could negative integers be palindromes? (ie, -1)
    If you are thinking of converting the integer to string, note the restriction of using extra space.
    You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
    There is a more generic way of solving this problem.

Tags: Math
Time: O(n);    Space: O(1)
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        copy, reverse = x, 0

        # reverse integer
        while copy:
            reverse = reverse * 10 + copy % 10
            copy /= 10

        return x == reverse


if __name__ == '__main__':
    print Solution().isPalindrome(12321)
    print Solution().isPalindrome(-12321)
    print Solution().isPalindrome(12322)
