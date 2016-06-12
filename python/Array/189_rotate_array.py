# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Rotate an array of n elements to the right by k steps.
    For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Hint:
    Could you do it in-place with O(1) extra space?

Tags: Array
'''


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # if k == len(nums), k=0; else k
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

if __name__ == '__main__':
    print Solution().rotate([1,2,3,4,5,6,7], 3)
