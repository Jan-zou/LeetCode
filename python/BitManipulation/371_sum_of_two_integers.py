# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
    Example:
    Given a = 1 and b = 2, return 3.

Tags: Bit Manipulation
"半加法"的思想:
    两位单独的位相加其结果可以用"异或"得到, 进位可以用"与"得到. 然后对于两个数字来说同样可以延伸这个思想.
'''

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # iterate till there is no carry
        while b != 0:
            c = a & b     # carry now contains common set bits of x and y
            a = a ^ b     # Sum of bits of x and y where at least one of the bits is not set
            b = c << 1    # Carry is shifted by one so that adding it to x gives the required sum
        return a

if __name__ == '__main__':
    print Solution().getSum(2,3)
