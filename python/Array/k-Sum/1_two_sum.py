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
    # Hash table; O(n)runtime, O(n)space
    def twoSum(self, nums, target):
        searchdict = {}
        for i, w in enumerate(nums):
            if target - w in searchdict:
                return (searchdict[target-w] + 1, i + 1)
            searchdict[w] = i
        return False

    # if numbers is sorted, binary search; O(nlogn)runtime, O(1)space
    def two_sum_sorted(self, nums, target):
        for i, w in enumerate(nums):
            j = self.binary_search(nums, target-w, i+1)
            if j != -1:
                return (i+1, j+1)
        return False

    def binary_search(self, nums, target, left):
        start = left
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    # if numbers is sorted, two points; O(n)runtime, O(1)space
    def two_sum_sorted2(self, nums, target):
        i, j = 0, len(nums)-1
        while i < j:
            sum = nums[i] + nums[j]
            if sum == target:
                return (i+1, j+1)
            elif sum > target:
                j -= 1
            else:
                i += 1
        return False


# Data Structure Design
class TwoSum:
    def __init__(self):
        self.nums = []
        self.target = 0

    def add(self, input):
        self.nums.append(input)

    def find(self, value):
        self.target = value
        searchdict = {}
        for i, w in enumerate(self.nums):
            if self.target - w in searchdict:
                return True
            searchdict[w] = i
        return False


if __name__ == '__main__':
    print "An array of intergers is (2,7,11,15), and the target is 9."
    print "index1=%d, index2=%d" % Solution().twoSum((2,7,11,15), 9)
    print "index1=%d, index2=%d" % Solution().two_sum_sorted((2,7,11,15), 9)
    print "index1=%d, index2=%d" % Solution().two_sum_sorted2((2,7,11,15), 9)
