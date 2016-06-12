# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree, determine if it is height-balanced.
    For this problem, a height-balanced binary tree is defined as a binary tree in which
    the depth of the two subtrees of every node never differ by more than 1.

Tags: Tree, Depth-first Search
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # O(n^2) runtime, O(n) stack space - Brute force top-down recursion
    # recalculating max depth repeatedly for each node
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and \
                self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


    # O(n) runtime, O(n) stack space - Bottom-up recursion
    # avoid the recalculation by passing the depth bottom-up;
    # sentinel value -1: tree is unbalanced
    def isBalanced2(self, root):
        return self.maxDepth2(root) != -1

    def maxDepth2(self, root):
        if root is None:
            return 0

        L = self.maxDepth2(root.left)
        if L == -1:
            return -1

        R = self.maxDepth2(root.right)
        if R == -1:
            return -1

        if abs(L - R) <= 1:
            return max(L, R) + 1
        else:
            return -1
