# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree, return the inorder traversal of its nodes' values.
    For example:
        Given binary tree {1,#,2,3},
           1
            \
             2
            /
           3
        return [1,3,2].
Note: Recursive solution is trivial, could you do it iteratively?

Tags: Tree, Hash Table, Stack
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root

        while stack or current:
            if current:
                stack.apend(current)
                current = current.left
            else:    # not have left
                current = stack.pop()
                result.append(current.val)
                current = current.right
        return result
