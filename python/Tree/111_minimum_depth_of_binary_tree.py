# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree, find its minimum depth.
    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Tags: Tree, Depth-first Search, Breadth-first Search
Time: O(n); Space: O(logn)
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # O(n) runtime, O(logn) space - Depth-first Search
    # traverse all nodes
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # O(n) runtime, O(logn) space - Breadth-first Search
    # When encounter the first leaf node, immediately stop the traversal.
    def minDepth2(self, root):
        if root is None:
            return 0

        queue, depth = [root], 1
        rightMost = root
        while queue:
            node = queue.pop()
            if node.left is None and node.right is None:
                break
            if node.left is not None:
                queue.insert(0, node.left)
            if node.right is not None:
                queue.insert(0, node.right)
            if node == rightMost:
                depth += 1
                if node.right is not None:
                    rightMost = node.right
                else:
                    rightMost = node.left
        return depth


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print Solution().minDepth(root)
    print Solution().minDepth2(root)
