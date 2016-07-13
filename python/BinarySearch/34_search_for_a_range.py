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
O(logn)runtime; O(1) Space
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binarySearch(lambda x,y: x <= y, nums, target)  # 找左边界; nums[mid] == target, right=mid, 继续查找左边界
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = self.binarySearch(lambda x,y: x < y, nums, target)  # 找右边界; nums[mid] == target, left=mid, 继续查找右边界
        return [left, right-1]

    def binarySearch(self, compare, nums, target):
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if compare(target,nums[mid]):
                end = mid
            else:
                start = mid + 1
        return start


if __name__ == '__main__':
    print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
