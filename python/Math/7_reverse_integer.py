# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Reverse digits of an integer.
    Example1: x = 123, return 321
    Example2: x = -123, return -321

    Have you thought about this?
    Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
    If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
    Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Tags: Math
Time: O(n); Space: O(1)
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        if x >= 0:
            while x:
                ans = ans * 10 + x % 10
                x /= 10
            return ans if ans <= 2147483647 else 0  # Handle overflow. python int: [-2^31, 2^31-1]
        else:
            return -self.reverse(-x)


if __name__ == '__main__':
    print Solution().reverse(123)
    print Solution().reverse(-321)
