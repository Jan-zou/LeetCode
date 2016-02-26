# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
    Find all unique quadruplets in the array which gives the sum of target.

Note:
+ Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
+ The solution set must not contain duplicate quadruplets.

  For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)


Tags: Array, Hash Table, Two Pointers

排序，用字典存储两两为一组的值，简化为2sum，注意去重
'''


import collections

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        nums = sorted(nums)
        result = []
        lookup = collections.defaultdict(list)

        for i in xrange(0, len(nums)-1):
            for j in xrange(i+1, len(nums)):
                lookup[nums[i]+nums[j]].append([i, j])    # key:sum; value:index

        for i in lookup.keys():
            if target-i in lookup:
                for x in lookup[i]:
                    for y in lookup[target-i]:
                        [a,b], [c,d] = x, y
                        if a is not c and b is not d and a is not d and b is not c :
                            # delete duplicate:
                            #   maybe the same key(a,b==c,d);
                            #   a=d or b=c but only one number in list
                            temp = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if temp not in result:
                                result.append(temp)

        return result

if __name__ == '__main__':
    print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)

