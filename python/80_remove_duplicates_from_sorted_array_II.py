# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Follow up for "Remove Duplicates":
    What if duplicates are allowed at most twice?
    For example,
    Given sorted array nums = [1,1,1,2,2,3],
    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
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

        last, i, same = 0, 1, False
        while i < len(nums):
            if nums[last] != nums[i] or not same:
                same = nums[last] == nums[i]
                last += 1
                nums[last] = nums[i]
            i += 1

        return last + 1

    def removeDuplicates2(self, nums):
        if not nums:
            return 0

        index, i = 2, 2
        while i < len(nums):
            if nums[i] != nums[index-2]:
                nums[index] = nums[i]
                index += 1
            i += 1
        return index


if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1, 1, 2, 2, 3])
    print Solution().removeDuplicates2([1, 1, 1, 2, 2, 3])


