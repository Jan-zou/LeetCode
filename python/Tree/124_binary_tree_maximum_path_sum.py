# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree, find the maximum path sum. 返回树中任意两点路径的最大值。只要两点间有路径连通就可以。
    For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
    The path does not need to go through the root.
    What if every node contains negative value? Then you should return the single node value that is the least negative.

    For example:
        Given the below binary tree,
               1
              / \
             2   3
        Return 6.

Tags: Tree, Depth-first Search
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
O(n) runtime, O(logn) space
Try the bottom up approach. At each node, the potential maximum path could be one of these cases:
    i. max(left subtree) + node
    ii. max(right subtree) + node
    iii. max(left subtree) + max(right subtree) + node
    iv. the node itself
Then, we need to return the maximum path sum that goes through this node and to either one of its left or right subtree to its parent.
If this maximum happens to be negative, we should return 0,
which means: “Do not include this subtree as part of the maximum path of the parent node”.
'''
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float("-inf")
        self.maxPathSumRecu(root)
        return self.maxSum

    def maxPathSumRecu(self, root):
        if root is None:
            return 0

        left = max(0, self.maxPathSumRecu(root.left))
        right = max(0, self.maxPathSumRecu(root.right))
        self.maxSum = max(self.maxSum, root.val + left + right)
        return root.val + max(left, right)

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print Solution().maxPathSum(root)
