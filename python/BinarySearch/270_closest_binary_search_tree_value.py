# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
Note:
    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.

Tags: Tree, Binary Search
O(h) runtime; O(1) space
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        gap = float("inf")
        closest = float("inf")
        while root:
            if abs(root.val - target) < gap:
                gap = abs(root.val - target)
                closest = root
            if target == root.val:
                break
            elif target < root.val:
                root = root.left
            else:
                root = root.right
        return closest.val

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    print Solution().closestValue(root, 4.0)
    print Solution().closestValue(root, 5.6)
