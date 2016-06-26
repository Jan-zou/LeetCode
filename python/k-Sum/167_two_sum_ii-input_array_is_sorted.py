# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Similar to Question [1. Two Sum], except that the input array is already sorted in ascending order.

Tags: Array, Hash Table
'''

class Solution:
    # binary search; O(nlogn) runtime, O(1) space
    def two_sum_sorted(self, nums, target):
        for i, w in enumerate(nums):
            j = self.binary_search(nums, target-w, i+1)
            if j != -1:
                return (i, j)
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

    # two points; O(n) runtime, O(1) space
    def two_sum_sorted2(self, nums, target):
        i, j = 0, len(nums)-1
        while i < j:
            sum = nums[i] + nums[j]
            if sum == target:
                return (i, j)
            elif sum > target:
                j -= 1
            else:
                i += 1
        return False


    # return all result pairs
    def two_sum_sorted3(self, nums, target):
        i, j = 0, len(nums)-1
        result = []
        while i < j:
            sum = nums[i] + nums[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                result.append((i, j))
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1
        return result

if __name__ == '__main__':
    print "An array of intergers is (2,7,11,15), and the target is 9."
    print "index1=%d, index2=%d" % Solution().two_sum_sorted((2,7,11,15), 9)
    print "index1=%d, index2=%d" % Solution().two_sum_sorted2((2,7,11,15), 9)
    print Solution().two_sum_sorted3((2,2,4,5,7,11,15), 9)
