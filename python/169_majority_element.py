# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given an array of size n, find the majority element.
    The majority element is the element that appears more than ⌊ n/2 ⌋ times.
    You may assume that the array is non-empty and the majority element always exist in the array.

Tags: Divide and Conquer, Array, Bit Manipulation
Time:  O(n)
Space: O(1)
成对消除
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter, item = 0, 0
        for i in nums:
            if counter == 0:
                item = i
                counter += 1
            elif item == i:
                counter += 1
            else:
                counter -= 1
        return item

if __name__ == '__main__':
    Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])
