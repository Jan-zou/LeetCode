# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given an array of n integers nums and a target,
    find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
    For example, given nums = [-2, 0, 1, 3], and target = 2.
    Return 2. Because there are two triplets which sums are less than 2:
        [-2, 0, 1]
        [-2, 0, 3]
    Follow up: Could you solve it in O(n^2) runtime?

Tags: Array
Time: O(n^2); Space: O(1)
'''

class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums = sorted(nums)
        result = 0
        i = 0
        while i < len(nums)-2:
            j, k = i+1, len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum >= target:
                    k -= 1
                elif sum < target:
                    result += k - j    # i,j 固定; <=k的数都可以
                    j += 1
            i += 1
        return result


if __name__ == '__main__':
    print Solution().threeSumSmaller([-2,0,1,3], 2)
