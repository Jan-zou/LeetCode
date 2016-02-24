# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a sorted array of integers, find the starting and ending position of a given target value.
    Your algorithm's runtime complexity must be in the order of O(log n).
    If the target is not found in the array, return [-1, -1].

    For example,
    Given [5, 7, 7, 8, 8, 10] and target value 8,
    return [3, 4].

Tags: Array, Binary Search
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binarySearch(lambda x,y: x <= y, nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = self.binarySearch(lambda x,y: x < y, nums, target)
        return [left, right-1]

    def binarySearch(self, compare, nums, target):
        start, end = 0, len(nums) -1
        while start < end:
            mid = (start + end) // 2
            if compare(target,nums[mid]):
                end = mid - 1
            else:
                start = mid + 1
        return start

