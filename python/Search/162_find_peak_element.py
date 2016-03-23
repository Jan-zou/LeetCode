# !/usr/bin/env python
# coding: utf-8

'''
Description:
    A peak element is an element that is greater than its neighbors.
    Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
    The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
    You may imagine that num[-1] = num[n] = -∞.
    For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
Note:
    Your solution should be in logarithmic complexity.

Tags: Array, Binary Search
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(logn); Space: O(1)
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 or nums[mid-1] <= nums[mid]) and \
               (mid == len(nums)-1 or nums[mid+1] <= nums[mid]):
                return mid
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    print Solution().findPeakElement([1,2,3,1])
