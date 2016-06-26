# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

Note:
+ Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
+ The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
        (-1, 0, 1)
        (-1, -1, 2)

Tags: Array, Two Pointers

Time: O(n^2); Space: O(1)
先排序，然后左右夹逼，跳过重复的数
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)    # O(nlogn)
        result = []
        i = 0

        while i < len(nums)-2:
            if i == 0 or nums[i] != nums[i-1]:    # skip duplicate number
                j,k = i+1, len(nums)-1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:    # skip duplicate
                            j += 1
                        while j < k and nums[k] == nums[k+1]:    # skip duplicate
                            k -= 1
            i += 1
        return result


if __name__ == '__main__':
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])
