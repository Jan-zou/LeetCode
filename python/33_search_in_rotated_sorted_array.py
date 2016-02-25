# !/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Description:
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    You are given a target value to search. If found in the array return its index, otherwise return -1.
    You may assume no duplicate exists in the array.

Tags: Array, Binary Search
Time: O(logn)
Space: O(1)
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first, last = 0, len(nums)
        while first != last:
            mid = first + (last - first)/2
            if nums[mid] == target:
                return mid

            if nums[first] <= nums[mid]:
                if nums[first] <= target and target < nums[mid]:
                    last = mid
                else:
                    first = mid + 1
            else:
                if nums[mid] < target and target <= nums[last-1]:
                    first = mid + 1
                else:
                    last = mid

        return -1


if __name__ == '__main__':
    print Solution().search([1], 0)
    print Solution().search([1], 1)
    print Solution().search([3, 5, 1], 3)
    print Solution().search([4, 5, 6, 7, 0, 1, 2], 5)
