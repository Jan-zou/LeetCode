# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given an array of integers, every element appears twice except for one. Find that single one.

Note:
    Your algorithm should have a linear runtime complexity.
    Could you implement it without using extra memory?

Tags: Hash Table, Bit Manipulation

Time: O(n)
Space: O(1)

异或; 只要出现偶数次, 都能清零.
'''

import operator

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in nums:
            x ^= i
        return x


    def singleNumber2(self, nums):
        return reduce(operator.xor, nums)


if __name__ == '__main__':
    print Solution().singleNumber([1, 2, 2, 5, 5])
    print Solution().singleNumber([1, 1, 2, 2, 3])

