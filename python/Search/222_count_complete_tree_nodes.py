# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a complete binary tree, count the number of nodes.
    Definition of a complete binary tree from Wikipedia:
        In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
        It can have between 1 and 2h nodes inclusive at the last level h.
    完全二叉树如果左子树最左边的深度，等于右子树最右边的深度，说明这个二叉树是满的，即最后一层也是满的，则以该节点为根的树其节点一共有2^h-1个。

Tags: Tree, Binary Search
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
