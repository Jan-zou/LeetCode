# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a complete binary tree, count the number of nodes.
    Definition of a complete binary tree from Wikipedia:
        In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
        It can have between 1 and 2^h nodes inclusive at the last level h.
    完全二叉树如果左子树最左边的深度，等于右子树最右边的深度，说明这个二叉树是满的，即最后一层也是满的，则以该节点为根的树其节点一共有2^h-1个。


PS:
    + 完全二叉树：深度为h, 除第h层外, 其它各层(1～h-1)的结点数都达到最大个数, 第h层所有的结点都连续集中在最左边.
    + 满二叉树：除叶子结点外的所有结点均有两个子结点, 节点数达到最大值, 所有叶子结点必须在同一层上. 树深h, 总结点数为2^h-1.

Tags: Tree, Binary Search
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # O(h^2) runtime; O(1) space
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        hl, hr = 0, 0
        node_left, node_right = root, root
        while node_left:
            hl += 1
            node_left = node_left.left

        while node_right:
            hr += 1
            node_right = node_right.right

        if hl == hr:
            return 2**hl - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # Binary Search - O(h*logn)=O((logn)^2) runtime; O(1) space
    def countNodes2(self, root):
        if root is None:
            return 0

        node, level = root, 0
        while node.left is not None:
            node = node.left
            level += 1

        # Binary Search
        left, right = 2**level, 2**(level+1)
        while left < right:
            mid = left + (right - left) // 2
            if not self.exist(root, mid):
                right = mid
            else:
                left = mid + 1
        return left - 1

    # Check if the nth node exist.
    def exist(self, root, n):
        k = 1
        while k <= n:
            k <<= 1    # *2
        k >>= 2

        node = root
        while k > 0:
            if (n & k) == 0:
                node = node.left
            else:
                node = node.right
            k >>= 1
        return node is not None

if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    print Solution().countNodes(tree)
    print Solution().countNodes2(tree)
