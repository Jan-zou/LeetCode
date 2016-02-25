# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this in place with constant memory.
    For example,
    Given input array nums = [1,1,2],
    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the new length.

Tags: Array, Two Pointers
Time: O(n)
Space: O(1)
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        index, i = 0, 1
        while i < len(nums):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
            i += 1

        return index + 1

if __name__ == '__main__':
    print Solution().removeDuplicates([1,1,2])
