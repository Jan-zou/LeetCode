# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Tags: Tree, Depth-first Search
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # O(n) runtime, O(logn) stack space – Divide and conquer
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBSTRecu(nums, 0, len(nums))

    def sortedArrayToBSTRecu(self, nums, start, end):
        if start == end:
            return None

        mid = start + (end - start) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTRecu(nums, start, mid)
        node.right = self.sortedArrayToBSTRecu(nums, mid+1, end)
        return node


if __name__ == "__main__":
    num = [1, 2, 3]
    result = Solution().sortedArrayToBST(num)
    print result.val, result.left.val, result.right.val
