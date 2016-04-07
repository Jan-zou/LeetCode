# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    For example,
    given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

Tags: Array, Two Pointers
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # bubble sort
        passnum = len(nums)-1
        exchanges = True
        while passnum > 0 and exchanges:
            exchanges = False
            for i in range(passnum):
                if nums[i] == 0:
                    exchanges = True
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            passnum = passnum - 1

    def moveZeros2(self, nums):
        pos = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
