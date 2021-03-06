# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Invert a binary tree.
             4
           /   \
          2     7
         / \   / \
        1   3 6   9
    to
             4
           /   \
          7     2
         / \   / \
        9   6 3   1

> Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

Tags: Tree
Time: O(n); Space: O(h)
'''

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.data = collections.deque()

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.popleft()

    def empty(self):
        return len(self.data) == 0

class Solution(object):
    # DFS, Recursive solution.
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # Stack solution
    def invertTree2(self, root):
        if root is not None:
            nodes = [root]
            while nodes:
                node = nodes.pop()
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)
        return root

    # BFS solution
    def invertTree3(self, root):
        if root is not None:
            nodes = Queue()
            nodes.push(root)
            while not nodes.empty():
                node = nodes.pop()
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    nodes.push(node.left)
                if node.right is not None:
                    nodes.push(node.right)
        return root
