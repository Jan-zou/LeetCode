# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given an unsorted array of integers, find the length of longest increasing subsequence.
    For example, Given [10, 9, 2, 5, 3, 7, 101, 18],
    The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
    Note that there may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.
    Follow up: Could you improve it to O(n log n) time complexity?

Tags: Dynamic Programming, Binary Search
'''

class Solution(object):
    # Dynamic Programming; Time: O(n^2); Space: O(n)
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = []  # dp[i]: the length of LIS ends with nums[i]
        for i in xrange(len(nums)):
            dp.append(1)
            for j in xrange(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0


    # Binary Search; Time: O(nlogn); Space: O(n)
    def lengthOfLIS2(self, nums):
        LIS = []

        def insert(target):
            left, right = 0, len(LIS)-1
            while left <= right:
                mid = (left+right)//2
                if LIS[mid] >= target:
                    right = mid -1
                else:
                    left = mid + 1
            if left == len(LIS):
                LIS.append(target)
            else:
                LIS[left] = target

        for num in nums:
            insert(num)
        return len(LIS)


if __name__ == '__main__':
    print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print Solution().lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18])

