# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given two arrays, write a function to compute their intersection.
    Example:
    Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.
Follow up:
    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

Tags: Binary Search, Hash Table, Two Pointers, Sort
'''

from collections import Counter

class Solution(object):
    # hash table - O(mn) runtime; O(m+n) space
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)

        for key in dict1:
            if key in dict2.keys():
                result.extend([key]*min(dict1[key], dict2[key]))
        return result

    # two point - O(m+n) runtime; O(1) space
    def intersect2(self, nums1, nums2):
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i, j, result = 0, 0, []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return result

    # binary search
    def intersect3(self, nums1, nums2):
        result = []
        nums1 = sorted(nums1)
        nums2 = Counter(nums2)
        for i in nums2:
            count = min(self.binary_search(nums1, i), nums2[i])
            result.extend([i]*count)
        return result

    def binary_search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return 1 + self.binary_search(nums[:mid], target) + self.binary_search(nums[mid+1:], target)
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return 0


if __name__ == '__main__':
    print Solution().intersect([1, 2, 2, 1], [2,2])
    print Solution().intersect2([1, 2, 2, 1], [2,2])
    print Solution().intersect3([1, 2, 2, 1], [2,2])
