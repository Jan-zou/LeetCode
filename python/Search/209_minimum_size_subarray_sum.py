# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s.
    If there isn't one, return 0 instead.

    For example, given the array [2,3,1,2,4,3] and s = 7,
    the subarray [4,3] has the minimal length under the problem constraint.

More practice:
    If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

Tags: Array, Two Pointers, Binary Search
'''


class Solution(object):
    # Sliding window; Time: O(n); Space: O(1)
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start, sum = 0, 0
        min_size = float('inf')

        for i in xrange(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_size = min(min_size, i - start + 1)
                sum -= nums[start]
                start += 1
        return min_size if min_size != float('inf') else 0


    # Binary Search; Time: O(logn); Space: O(n)
    def minSubArrayLen2(self, s, nums):

        min_size = float('inf')
        sum_from_start = [n for n in nums]
        for i in xrange(len(sum_from_start) - 1):
            sum_from_start[i + 1] += sum_from_start[i]
        for i in xrange(len(sum_from_start)):
            end = self.binarySearch(lambda x, y: x <= y, sum_from_start, \
                                    i, len(sum_from_start)-1, \
                                    sum_from_start[i] - nums[i] + s)
            if end < len(sum_from_start):
                min_size = min(min_size, end - i + 1)

        return min_size if min_size != float('inf') else 0

    def binarySearch(self, compare, nums, start, end, target):
        while start <= end:
            mid = start + (end - start) / 2
            if compare(target, nums[mid]):
                end = mid - 1
            else:
                start = mid + 1
        return start


if __name__ == '__main__':
    print Solution().minSubArrayLen(7, [2,3,1,2,4,3])
    print Solution().minSubArrayLen2(7, [2,3,1,2,4,3])
