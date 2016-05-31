# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

    For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
    return ["2", "4->49", "51->74", "76->99"].

    Example Questions Candidate Might Ask:
    Q: What if the given array is empty?
    A: Then you should return [“0->99”] as those ranges are missing.
    Q: What if the given array contains all elements from the ranges?
    A: Return an empty list, which means no range is missing.

Tags: Array
Time: O(n); Space: O(1)
'''


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        pre = lower - 1

        for i in xrange(len(nums) + 1):
            if i == len(nums):
                cur = upper + 1
            else:
                cur = nums[i]

            if cur - pre > 1:
                ranges.append(self.getRange(pre + 1, cur - 1))

            pre = cur
        return ranges

    def getRange(self, lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)


if __name__ == '__main__':
    print Solution().findMissingRanges([], 0, 99)
    print Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99)
    print Solution().findMissingRanges(range(100), 0, 99)
