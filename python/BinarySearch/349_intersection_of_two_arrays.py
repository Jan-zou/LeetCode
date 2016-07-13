# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given two arrays, write a function to compute their intersection.
    Example:
    Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
Note:
    Each element in the result must be unique.
    The result can be in any order.

Tags: Binary Search, Hash Table, Two Pointers, Sort
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)
        return result

    # two pointers
    def intersection2(self, nums1, nums2):
        result = []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if nums1[i] not in result:
                    result.append(nums1[i])
                i += 1
                j += 1
        return result

    # binary search
    def intersection3(self, nums1, nums2):
        result = []
        nums1 = sorted(nums1)
        for i in nums2:
            status = self.binary_search(nums1, i)
            if status and i not in result:
                result.append(i)
        return result

    def binary_search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        return False

if __name__ == '__main__':
    print Solution().intersection([1, 2, 2, 1], [2,2])
    print Solution().intersection2([1, 2, 2, 1], [2,2])
    print Solution().intersection3([1, 2, 2, 1], [2,2])
