# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree, return the postorder traversal of its nodes' values.
    For example:
        Given binary tree {1,#,2,3},
           1
            \
             2
            /
           3
        return [3,2,1].
Note: Recursive solution is trivial, could you do it iteratively?

Tags: Tree, Stack
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        current, last = root, None

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                parent = stack[-1]
                if parent.right in (None, last):
                    result.append(parent.val)
                    last = stack.pop()
                current = parent.right
        return result

