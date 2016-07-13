# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element.
    You may assume no duplicate exists in the array.

Tags: Array, Binary Search
'''

class Solution(object):
    # O(n) runtime; O(1) space
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                return nums[i]
            i += 1
        return nums[0]

    # O(logn) runtime; O(1) space
    def findMin2(self, nums):
        left, right = 0, len(nums)-1
        while left < right and nums[left] > nums[right]:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

if __name__ == '__main__':
    print Solution().findMin([4,5,6,7,0,1,2])
    print Solution().findMin2([4,5,6,7,0,1,2])
