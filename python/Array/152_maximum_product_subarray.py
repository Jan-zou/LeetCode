# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Find the contiguous subarray within an array (containing at least one number) which has the largest product.
    For example, given the array [2,3,-2,4],
    the contiguous subarray [2,3] has the largest product = 6.

Tags: Array, Dynamic Programming
'''

class Solution(object):
    # O(n) runtime; O(1) space
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_min, local_max, global_max = 1, 1, float("-inf")
        for i in nums:
            local_max, local_min = max(i, i*local_max, i*local_min), min(i, i*local_max, i*local_min)
            global_max = max(local_max, global_max)
        return global_max

if __name__ == '__main__':
    print Solution().maxProduct([2,3,-2,4])
