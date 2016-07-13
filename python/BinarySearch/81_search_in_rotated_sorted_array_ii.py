# !/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Description:
    Follow up for "Search in Rotated Sorted Array":
    What if duplicates are allowed?
    Would this affect the run-time complexity? How and why?
    Write a function to determine if a given target is in the array.

Tags: Array, Binary Search
O(logn) runtime; O(1) space

若允许重复元素, 则33题中nums[first] <= nums[mid]时, [1,m]是递增序列不能成立, 如[1,3,1,1,1].
因此将nums[first] <= nums[mid]拆分成两个条件:
    nums[first] < nums[mid]时, [1,m]一定为递增序列
    nums[first] = nums[mid]时, 无法确定, 因此first++往下看一步
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[start] < nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
            elif nums[start] > nums[mid]:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                start += 1
        return False


if __name__ == '__main__':
    print Solution().search([3, 5, 1], 3)
    print Solution().search([2, 2, 3, 3, 4, 1], 5)
    print Solution().search([4, 4, 5, 6, 7, 0, 1, 2], 5)
