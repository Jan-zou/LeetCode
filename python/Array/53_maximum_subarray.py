# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
    For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
    the contiguous subarray [4,−1,2,1] has the largest sum = 6.
    More practice:
    If you have figured out the O(n) solution,
    try coding another solution using the divide and conquer approach, which is more subtle.

Tags: Array, Dynamic Programming, Divide and Conquer
'''

class Solution(object):
    # O(n) runtime; O(1) space - 局部最优和全局最优解法
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max, local_max = float("-inf"), 0
        for i in nums:
            local_max = max(i, i+local_max)
            global_max = max(local_max, global_max)
        return global_max

    # Divide and Conquer
