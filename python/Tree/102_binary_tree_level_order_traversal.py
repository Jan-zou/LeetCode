# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
    For example:
        Given binary tree {3,9,20,#,#,15,7},
            3
           / \
          9  20
            /  \
           15   7
        return its level order traversal as:
            [
              [3],
              [9,20],
              [15,7]
            ]

Tags: Tree, Breadth-first Search
Time: O(n); Space: O(n)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = []
        current = [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print Solution().levelOrder(root)
