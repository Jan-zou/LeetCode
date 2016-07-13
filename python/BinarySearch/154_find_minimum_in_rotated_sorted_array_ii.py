# !/usr/bin/env python
# coding: utf-8

'''
Description:
    > Follow up for "Find Minimum in Rotated Sorted Array":
    > What if duplicates are allowed?
    > Would this affect the run-time complexity? How and why?

    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element.
    The array may contain duplicates.

Tags: Array, Binary Search
'''

class Solution(object):
    # O(logn) runtime; O(1) space
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right and nums[left] >= nums[right]:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[left]:
                left += 1
            else:
                right = mid
        return nums[left]

if __name__ == '__main__':
    print Solution().findMin([4,5,5,7,0,1,1,2])
