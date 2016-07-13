# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Implement int sqrt(int x).
    Compute and return the square root of x. 二分法求平方根

Tags: Math, Binary Search
O(logn) runtime; O(1) space
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        low, high = 1, x - 1
        while low <= high:
            mid = low + (high - low) // 2
            if x//mid < mid:    # 等价于 x < mid*mid
                high = mid - 1
            else:
                low = mid + 1
        return high    # high<low

if __name__ == '__main__':
    print Solution().mySqrt(10)
