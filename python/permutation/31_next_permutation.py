# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:

    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
    The replacement must be in-place, do not allocate extra memory.
    Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
        1,2,3 → 1,3,2
        3,2,1 → 1,2,3
        1,1,5 → 1,5,1

Tags: Array

一个排列的下一个排列，即两者之间没有其他排列，要求两者有尽可能长的共同前缀，变化限制在尽可能短的后缀上。
假设数组A大小是n:
1.从左到右，找到最后一个A[i]<A[i+1]的数A[i]
2.在A[i+1]到A[n-1]中，找到最小的一个大于A[i]的数A[l]
3.交换A[i]和A[l]; 将A[i+1]到数组末尾的数升序排列

'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0

        for i in xrange(len(nums)-1):
            if nums[i] < nums[i+1]:
                k = i

        if k == -1:
            nums.reverse()
            return

        for i in xrange(k+1, len(nums)):
            if nums[i] > nums[k]:
                l = i

        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[:k:-1]


if __name__ == '__main__':
    print Solution().nextPermutation([1,2])
    print Solution().nextPermutation([1,4,3,2])

