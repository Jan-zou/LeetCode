# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
    Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Tags: Array, Two Pointers
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_diff = float("inf")    # 正无穷大
        nums = sorted(nums)
        result = 0
        i = 0

        while i < len(nums)-2:
            if i == 0 or nums[i] != nums[i-1]:
                j, k = i+1, len(nums)-1
                while j < k:
                    gap = nums[i] + nums[j] + nums[k] - target
                    if abs(gap) < min_diff:
                        min_diff = abs(gap)
                        result = nums[i] + nums[j] + nums[k]
                    if gap < 0:
                        j += 1
                    elif gap > 0:
                        k -= 1
                    else:
                        return target
            i += 1
        return result


if __name__ == '__main__':
    print Solution().threeSumClosest([-1, 2, 1, -4], 1)

