# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a sorted integer array without duplicates, return the summary of its ranges.
    For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Tags: Array
Time: O(n); Space: O(1)
'''


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        if not nums:
            return ranges

        start, end = nums[0], nums[0]
        for i in xrange(1, len(nums)+1):
            if i < len(nums) and nums[i] == end + 1:
                end = nums[i]
            else:
                interval = str(start)
                if start != end:
                    interval += '->' + str(end)
                ranges.append(interval)
                if i < len(nums):
                    start = end = nums[i]
        return ranges


if __name__ == '__main__':
    print Solution().summaryRanges([0,1,2,4,5,7])
