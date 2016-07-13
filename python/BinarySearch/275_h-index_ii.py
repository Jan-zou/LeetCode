# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Follow up for H-Index: What if the citations array is sorted in ascending order?
    Could you optimize your algorithm?
Hint:
    Expected runtime complexity is in O(log n) and the input is sorted.

Tags: Binary Search
O(logn) runtime; O(1) space
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid - 1
        return n - left

if __name__ == '__main__':
    print Solution().hIndex([0, 1, 3, 5, 6])
