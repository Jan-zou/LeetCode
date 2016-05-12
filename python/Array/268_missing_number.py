# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

    For example,
    Given nums = [0, 1, 3] return 2.

Note:
    Your algorithm should run in linear runtime complexity.
    Could you implement it using only constant extra space complexity?

Tags: Array, Math, Bit Manipulation

O(n) runtime, O(1) space
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums, reduce(operator.xor, xrange(len(nums) + 1)))
