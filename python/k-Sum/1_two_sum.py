# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given an array of integers, find two numbers such that they add up to a specific target number.
    The function twoSum should return indices of the two numbers such that they add up to the target,
    where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution.
    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2

Tags: Array, Hash Table
'''

class Solution:
    # @return a tuple, (index1, index2)
    # Hash table; O(n) runtime, O(n) space
    def twoSum(self, nums, target):
        searchdict = {}
        for i, w in enumerate(nums):
            if target - w in searchdict:
                return (searchdict[target-w], i)
            searchdict[w] = i
        return False


if __name__ == '__main__':
    print "An array of intergers is (2,7,11,15), and the target is 9."
    print "index1=%d, index2=%d" % Solution().twoSum((2,7,11,15), 9)
